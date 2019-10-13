from Tkinter import *
root=Tk()
Label(root,text='CheckButton Demo',relief='ridge',font='times 20 bold italic',bg='green').pack()
v2=IntVar()
v3=IntVar()
v4=IntVar()
Checkbutton(root,text='10th',variable=v2,onvalue=10).pack()
Checkbutton(root,text='12th',variable=v3,onvalue=12).pack()
Checkbutton(root,text='B.Tech',variable=v4,onvalue=16).pack()
def cchoice():
    Label(root,text=str(v2.get())+' '+str(v3.get())+' '+str(v4.get())).pack()
Button(root,text='Choice',command=cchoice).pack()
mainloop()
