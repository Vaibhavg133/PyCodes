from Tkinter import *
root=Tk()
Label(root,text='Gender Choice',relief='ridge',font='times 20 bold italic',bg='green').pack()
Label(root,text='Select Your Gender').pack()
v1=IntVar()
r=Radiobutton(root,text='Male',variable=v1,value=1)
r.pack()
r1=Radiobutton(root,text='Female',variable=v1,value=2)
r1.pack()
r2=Radiobutton(root,text='Third',variable=v1,value=3)
r2.pack()
def choice():
    if v1.get()==1:
        Label(root,text='You Selected Male').pack()
    elif v1.get()==2:
        Label(root,text='You Selected Female').pack()
    elif v1.get()==3:
        Label(root,text='You Selected Third').pack()
    else:
        Label(root,text='Invalid Choice')
Button(root,text='Choice',command=choice).pack()
mainloop()
