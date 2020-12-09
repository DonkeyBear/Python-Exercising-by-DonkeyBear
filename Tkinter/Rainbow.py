import tkinter as tk
from time import sleep as TimeSleep

colorR = 0
colorG = 0
colorB = 0

def dec2hex(inputDec):
    strHex = str(hex(inputDec))[2:]
    if len(strHex) < 2:
        strHex = '0' + strHex
    return strHex

def changeColor():
    global colorR, colorG, colorB
    bgColor = '#' + dec2hex(colorR) + dec2hex(colorG) + dec2hex(colorB)

    window.configure(background=str(bgColor))
    window.after(10, changeColor)

window = tk.Tk()
window.title('Rainbow')
window.geometry('300x300')
window.after(10, changeColor)

window.mainloop()