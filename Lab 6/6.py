from Tkinter import *
root=Tk()
Label(root,text='Enter First Name').pack()
e1=Entry()
e1.pack()
Label(root,text='Enter Last Name').pack()
e2=Entry()
e2.pack()
#def Add():
#    e=(e1.get())+char(e2.get())
#    Label(root,text='Name',command=e).pack()

Button(root,text='Welcome'+e1.get()).pack()
mainloop()
