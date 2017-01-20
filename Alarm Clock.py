from Tkinter import * #gives us access to everything in the Tkinter class
import tkMessageBox
from PIL import Image, ImageTk
from datetime import datetime
from threading import *









def countdown(count): 
    label['text'] = count

    if count > 0:
        top.after(1000, countdown,count-1)

top = tkinter.Tk()
top.geometry("700x100")
hoursT=tkinter.Label(top, text="Hours:")
hoursE=tkinter.Entry(top)
minuteT=tkinter.Label(top, text="Minutes:")
minuteE=tkinter.Entry(top)
secondT=tkinter.Label(top, text="Seconds:")
secondE=tkinter.Entry(top)
hoursT.grid(row=1,column=1)
hoursE.grid(row=1,column=2)
minuteT.grid(row=1,column=3)
minuteE.grid(row=1,column=4)
secondT.grid(row=1,column=5)
secondE.grid(row=1,column=6)
label = tkinter.Label(top)
label.grid(row=3)

t=(int(hoursE.get())*360+int(minuteT.get())*60+int(secondE.get())
button=tkinter.Button(top,text="Start Timer",command=lambda:None)
button.grid(row=2)

def updateButton():
    hour,min,sec=hoursE.get(),minuteT.get(),secondE.get()
    if hour.isdigit() and min.isdigit() and sec.isdigit():
        time=int(hour)*360+int(min)*60+int(sec)
        button.configure(command=lambda count=time:countdown(count))

for widget in (hoursE,minuteT,secondE):
    widget.bind("<FocusOut>", updateButton)
mainloop() #causes the windows to display on the screen until program closes
