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

def changeColorR(value):
    global colorR
    colorR += value
    if colorR > 255:
        colorR = 255
    return colorR

def changeColorG(value):
    global colorG
    colorG += value
    if colorG > 255:
        colorG = 255
    return colorG

def changeColorB(value):
    global colorB
    colorB += value
    if colorB > 255:
        colorB = 255
    return colorB

def changeBgColor():
    global colorR, colorG, colorB
    bgColor = '#' + dec2hex(changeColorR(1)) + dec2hex(changeColorG(2)) + dec2hex(changeColorB(3))

    window.configure(background=str(bgColor))
    window.after(10, changeBgColor)

window = tk.Tk()
window.title('Rainbow')
window.geometry('300x300')
window.after(10, changeBgColor)

window.mainloop()