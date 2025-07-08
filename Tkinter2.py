
from tkinter import *

windows=Tk()

windows.title("Entry_Box & Grid")
windows.geometry("800x1000")
label1=Label(windows,text="Mail")
label2=Label(windows,text="Password")
e1=Entry(windows,width=40, borderwidth=5)
e2=Entry(windows,width=40, borderwidth=5)
label1.grid(column=1, row=0)
label2.grid(column=1, row=1)
e1.grid(column=2, row=0)
e2.grid(column=2, row=1)
mainloop()