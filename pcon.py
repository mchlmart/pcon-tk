import minimalmodbus
import serial

minimalmodbus.BAUDRATE = 38400       
minimalmodbus.BYTESIZE = 8            
minimalmodbus.STOPBITS = 1            
minimalmodbus.TIMEOUT = 1             
minimalmodbus.PARITY = serial.PARITY_NONE
minimalmodbus.CLOSE_PORT_AFTER_EACH_CALL = True

instrument = minimalmodbus.Instrument('COM5', 2, mode=minimalmodbus.MODE_RTU)
drg1_register = 0x0D00
def servo_on():
    #value to reset the alarm and set the servo on
    ars_value = 0x1100

    instrument.write_register(drg1_register,ars_value,functioncode=6)

def homing():
    #value to home the pcon with the servo on
    homing_value = 0x1010
    instrument.write_register(drg1_register,homing_value,functioncode=6)
