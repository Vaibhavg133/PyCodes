from Tkinter import *
root=Tk()
def prin():
    Label(root,text='Nice Job').pack()
def event():
    Button(root,text='Hitted Me',command=prin).pack()
    
Button(root,text='Hit Me',command=event).pack()
root.mainloop()
