from Tkinter import *
root=Tk()
Label(root,text='Enter Principle').grid(row = 0)
Principle=Entry(root)
Principle.grid(row = 0, column = 1)
Label(root,text='Enter Rate').grid(row = 1)
Rate=Entry(root)
Rate.grid(row = 1, column = 1)
Label(root,text='Enter Time').grid(row = 2)
Time=Entry(root)
Time.grid(row = 2, column = 1)
root.mainloop()
