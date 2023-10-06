from tkinter import *
from tkinter.ttk import *
from time import strftime

top=Tk()
top.title("Digital Clock")
def digitalClock():
    text=strftime(' %H:%M:%S %p ')
    lbl.config(text=text)
    lbl.after(1000,digitalClock)
lbl=Label(top,font=('digital-7' ,50,'bold'),background='white',foreground='purple')
lbl.pack(anchor='center')
digitalClock()
mainloop()