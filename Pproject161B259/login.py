from Tkinter import*
from tkMessageBox import*
import os
splash=Tk()
Label(splash,text="Name : Vaibhav Goel",fg="white",bg='black').grid()
Label(splash,text="Enroll : 161B259",fg="white",bg='black').grid()
Label(splash,text="Subject : Python",fg="white",bg='black').grid()
splash.configure(background="black")
def VBS(event):
    splash.destroy()
    root=Tk()
    root.geometry('1366x768+0+0')
    Label(root,text="JUET Management System",relief='ridge',font="times 32 bold",padx=340).grid(row=0,column=0,columnspan=2)
    Label(root,text="Admin ID",font="times 20 bold").grid(row=3,column=0)
    l1=Entry(root,font="times 20 bold")
    l1.grid(row=3,column=1)
    Label(root,text="Password",font="times 20 bold",bd=5).grid(row=4,column=0)
    l2=Entry(root,show='+',bd=5,font="times 20 bold")
    l2.grid(row=4,column=1)

    def log():
        if l2.get() == "161B259" and l1.get() == 'Admin' :
            l2.delete(0,END)
            Label(root,text='Successfull Login').grid()
            os.startfile("College.py")
        else :
            Label(root,text='Wrong Password').grid()
            

    Button(root,text='Login',command=log,bd=5,font="times 22 bold",pady=3,padx=5,bg='paleturquoise').grid(row=5,column=1,sticky=W+S+N)
    root.mainloop()
lb=Label(splash,text="Move")
lb.bind("<Motion>",VBS)
lb.grid()
splash.mainloop()
