import tkinter as tk
from time import sleep as TimeSleep

colorR = 0
colorG = 0
colorB = 0
colorStateR = 1
colorStateG = 1
colorStateB = 1

def dec2hex(inputDec):
    strHex = str(hex(inputDec))[2:]
    if len(strHex) < 2:
        strHex = '0' + strHex
    return strHex

def changeColor(color, value):
    color += value
    if color > 255:
        color = 255
    return color


def changeBgColor():
    global colorR, colorG, colorB
    bgColor = '#' + dec2hex(changeColor(colorR, 1)) + dec2hex(changeColor(colorG, 2)) + dec2hex(changeColor(colorB, 3))

    window.configure(background=str(bgColor))
    window.after(10, changeBgColor)

window = tk.Tk()
window.title('Rainbow')
window.geometry('300x300')
window.after(10, changeBgColor)

window.mainloop()