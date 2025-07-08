# step1: import tkinter
from tkinter import *

#step2: gui interaction
windows =Tk()

#step3: adding inputs
windows.title("Simple")
windows.geometry("500x700")
windows.config(bg="Yellow")
frame1=Frame(windows,width=300,height=300, cursor="dot")
frame2=Frame(windows,width=300,height=300, cursor="dotbox")
button1=Button(frame1,text="Button1", bg="red")
button2=Button(frame2,text="Button1", bg="pink")
button3=Button(frame1,text="Button1", bg="blue")

frame1.pack(side=TOP)
frame2.pack(side=BOTTOM)
button1.pack()
button2.pack()
button3.pack()
#step4: main loop
mainloop()