#acPump.py
#DESCRIPTION:File for toggle state based on current input in python
#REQUIREMENTS:
#BUGS:
#AUTHOR: Alok_Jha
#E-mail: jhaalok1984_at_gmail.com
#ORGANIZATION:NPCIL
#VERSION:
#REVISION:
#CREATED:Sunday, 30 September 2018.
#===================================
#      !!ENVIRONMENT VARIABLES!!
#!/usr/bin/python3
#===================================
import os
import subprocess
import tkinter as tk
from tkinter import *

# table lamp on/off actuator
def T_ON():
    if 'T_ON':
        os.system("echo 1 > /sys/class/gpio/gpio9/value")
def T_OFF():
    if 'T_OFF':
        os.system("echo 0 > /sys/class/gpio/gpio9/value")
## LED on/off actuator
def LED_ON():
    if 'LED_ON':
        os.system("echo 1 > /sys/class/gpio/gpio11/value")
def LED_OFF():
    if 'LED_OFF':
        os.system("echo 0 > /sys/class/gpio/gpio11/value")
## PUMP on/off actuator
def P_ON():
    if 'P_ON':
        os.system("echo 1 > /sys/class/gpio/gpio10/value")
def P_OFF():
    if 'P_OFF':
        os.system("echo 0 > /sys/class/gpio/gpio10/value")

root = tk.Tk()
root.wm_title("GPIO OPERATOR GUI")
frame = Frame(root)
frame.pack()

button = tk.Button(frame,
                   text="LAMP.ON",
                   fg="black",
                   bg="red",
                   command=T_ON)
button.pack(side=tk.LEFT)
slogan = tk.Button(frame,
                   text="LAMP.OFF",
                   fg="black",
                   bg="green",
                   command=T_OFF)
slogan.pack(side=tk.LEFT)
button = tk.Button(frame,
                   text="LED.ON",
                   fg="black",
                   bg="red",
                   command=LED_ON)
button.pack(side=tk.LEFT)
slogan = tk.Button(frame,
                   text="LED.OFF",
                   fg="black",
                   bg="green",
                   command=LED_OFF)
slogan.pack(side=tk.LEFT)
button = tk.Button(frame,
                   text="PUMP.ON",
                   fg="black",
                   bg="red",
                   command=P_ON)
button.pack(side=tk.LEFT)
slogan = tk.Button(frame,
                   text="PUMP.OFF",
                   fg="black",
                   bg="green",
                   command=P_OFF)
slogan.pack(side=tk.LEFT)
root.mainloop()
