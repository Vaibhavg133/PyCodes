from Tkinter import *
def mget():
	print(var1.get(),var2.get(),var3.get(),var4.get())
root=Tk()
var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
Checkbutton(root,text='check1',variable=var1).pack()
Checkbutton(root,text='check2',variable=var2).pack()
Checkbutton(root,text='check3',variable=var3).pack()
Checkbutton(root,text='check4',variable=var4).pack()
Button(root,text='get Vals',command=mget).pack()
Button(root,text='quit',command=root.destroy).pack()
root.mainloop()
