from Tkinter import *
root=Tk()
Label(root,text="Hello World").pack()
Button(root,text='OK',command=root.bell).pack()
def info():
    Label(root,text='Hello Python\n').pack()
Button(root,text='OK',command=info()).pack()
root.mainloop()
