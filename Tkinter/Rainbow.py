import tkinter as tk
from random import randint

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
    global colorR, colorStateR
    value = randint(0, value)
    if colorStateR == 1:
        colorR += value
        if colorR > 255:
            colorR = 255
            colorStateR = 0
    else:
        colorR -= value
        if colorR < 0:
            colorR = 0
            colorStateR = 1
    return colorR

def changeColorG(value):
    global colorG, colorStateG
    value = randint(0, value)
    if colorStateG == 1:
        colorG += value
        if colorG > 255:
            colorG = 255
            colorStateG = 0
    else:
        colorG -= value
        if colorG < 0:
            colorG = 0
            colorStateG = 1
    return colorG

def changeColorB(value):
    global colorB, colorStateB
    value = randint(0, value)
    if colorStateB == 1:
        colorB += value
        if colorB > 255:
            colorB = 255
            colorStateB = 0
    else:
        colorB -= value
        if colorB < 0:
            colorB = 0
            colorStateB = 1
    return colorB

def changeBgColor():
    bgColor = '#' + dec2hex(changeColorR(7)) + dec2hex(changeColorG(2)) + dec2hex(changeColorB(3))

    window.configure(background=str(bgColor))
    window.after(15, changeBgColor)

window = tk.Tk()
window.title('Rainbow')
window.geometry('300x300')
window.after(10, changeBgColor)

window.mainloop()