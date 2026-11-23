import tkinter as tk
import pcon

class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.width = 600
        self.height = 400
        self.button_width = 100
        self.root.geometry(f"{self.width}x{self.height}")
        self.button_servo = tk.Button(self.root,text="servo ON",font=("Times",15),command=self.servo_on)
        self.button_servo.place(x=self.width-20-self.button_width, y=(1/3)*self.height,width=self.button_width)
        self.button_homing = tk.Button(self.root,text="homing",font=("Times",15),command=self.homing)
        self.button_homing.place(x=self.width-20-self.button_width, y=(1/3)*self.height+50,width=self.button_width)
        self.log_box = tk.Text(self.root,font=("Times",15),state="disabled")
        self.log_box.place(x = 20, y = 2*self.height/3,width=self.width - self.button_width-60,height=self.height/3-20)
        
        self.root.mainloop()

    def log(self,text):
        self.log_box.config(state="normal")
        self.log_box.insert("end",text + "\n")
        self.log_box.see("end")
        self.log_box.config(state="disabled")

    def servo_on(self):
        self.log(pcon.servo_on())

    def homing(self):
        msg = pcon.homing()
        self.log(msg)
        if msg.endswith("homing started"):
            self.homing_ticks = 0
            self.root.after(1000, self.check_homing)

    def check_homing(self):
        try:
            done = pcon.status()["homing_done"]
        except Exception as e:
            self.log(f"error: {type(e).__name__}")
            return
        if done:
            self.log("homing completed")
        elif self.homing_ticks > 300:
            self.log("homing timeout")
        else:
            self.homing_ticks += 1
            self.root.after(200, self.check_homing)
GUI()