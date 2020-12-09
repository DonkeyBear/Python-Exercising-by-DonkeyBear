import tkinter as tk
from time import sleep as TimeSleep

bgInt = 0

def hex2str(inputHex):
    strHex = inputHex
    return strHex[2:]

def changeColor():
    global bgInt
    bgStr = str(bgInt)
    while len(bgStr) < 6:
        bgStr = '0' + bgStr
    bgColor = '#'+ bgStr
    window.configure(background=str(bgColor))
    window.after(10, changeColor)
    bgInt += 1

window = tk.Tk()
window.title('Rainbow')
window.geometry('300x300')
window.after(10, changeColor)

window.mainloop()