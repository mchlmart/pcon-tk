import tkinter as tk
import pcon as pcon

class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.width = 140
        self.height = 200
        self.button_width = 100
        self.root.geometry(f"{self.width}x{self.height}")
        self.button_servo = tk.Button(self.root,text="servo ON",font=("Times",15),command=pcon.servo_on)
        self.button_servo.place(x=self.width-20-self.button_width, y=(1/3)*self.height,width=self.button_width)
        self.button_homing = tk.Button(self.root,text="homing",font=("Times",15),command=pcon.homing)
        self.button_homing.place(x=self.width-20-self.button_width, y=(1/3)*self.height+50,width=self.button_width)
        
        self.root.mainloop()
GUI()