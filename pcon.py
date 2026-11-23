import minimalmodbus
import serial
import time

minimalmodbus.BAUDRATE = 38400       
minimalmodbus.BYTESIZE = 8            
minimalmodbus.STOPBITS = 1            
minimalmodbus.TIMEOUT = 1             
minimalmodbus.PARITY = serial.PARITY_NONE
minimalmodbus.CLOSE_PORT_AFTER_EACH_CALL = True

instrument = minimalmodbus.Instrument('COM5', 2, mode=minimalmodbus.MODE_RTU)
drg1_register = 0x0D00
dss1_register = 0x9005
def status():
    s = instrument.read_register(dss1_register)
    return {
        "servo_on":      bool(s & (1 << 12)),
        "alarm_major":   bool(s & (1 << 10)),
        "alarm_minor":   bool(s & (1 << 9)),
        "homing_done":   bool(s & (1 << 4)),
        "move_done":     bool(s & (1 << 3)),
    }


def reset_alarm():
    instrument.write_register(drg1_register, 0x0100, functioncode=6)
    time.sleep(0.2)
    instrument.write_register(drg1_register, 0x0000, functioncode=6)
    time.sleep(0.2)

def servo_on():
        try:
            alarm_st = None
            st = status()
            if st["alarm_minor"] or st["alarm_major"]:
                alarm_st =  hex(instrument.read_register(0x9002))
                reset_alarm()
                st = status()
                if st["alarm_minor"] or st["alarm_major"]:
                     return f"alarm {alarm_st} not cleared, code: {hex(instrument.read_register(0x9002))}"
            ars_value = 0x1000
            instrument.write_register(drg1_register,ars_value,functioncode=6)
            if alarm_st:
                return f"alarm {alarm_st} cleared, servo ON sent"
            else:
                return "servo ON sent"
        except Exception as e:
            return f"error: {type(e).__name__}"

def homing():
        try:
            alarm_st = None
            st = status()
            if st["alarm_minor"] or st["alarm_major"]:
                alarm_st =  hex(instrument.read_register(0x9002))
                reset_alarm()
                st = status()
                if st["alarm_minor"] or st["alarm_major"]:
                        return f"alarm {alarm_st} not cleared, code: {hex(instrument.read_register(0x9002))}"
            homing_value = 0x1010
            instrument.write_register(drg1_register,homing_value,functioncode=6)
            if alarm_st:
                return f"alarm {alarm_st} cleared, homing started"
            else:
                return "homing started"
        except Exception as e:
            return f"error: {type(e).__name__}"
