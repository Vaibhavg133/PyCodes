from Tkinter import *
root=Tk()
Label(root,text='Checkbox Check',relief='ridge',font='times 20 bold italic',bg='green').pack()
v2=IntVar()
v3=IntVar()
v4=IntVar()
Checkbutton(root,text='Red',variable=v2,onvalue=1).pack()
Checkbutton(root,text='Blue',variable=v3,onvalue=2).pack()
Checkbutton(root,text='Yellow',variable=v4,onvalue=3).pack()
def Choice():
    if v2.get()==1:
        Label(root,text='You Selected Red',bg='red')
    else:
        Label(root,bg='Yellow').pack()
Button(root,text='Choice',command=Choice).pack()
mainloop()
