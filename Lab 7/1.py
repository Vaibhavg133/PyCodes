from Tkinter import *
root=Tk()
Label(root,text='Enter Temp in Celcius').pack()
cel=Entry()
cel=IntVar()
def convert():
    fah=IntVar()
    fah=1.8*cel+32;
    Label(root,text=fah).pack()
Button(root,text=convert).pack()
mainloop()
