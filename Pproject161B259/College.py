from Tkinter import *
from tkMessageBox import *
import sqlite3
master=Tk()
master.title('Home')
Label(master,text='JUET Management System',width=25,bd=10,relief='ridge',font='times 20 bold underline',fg='#9C27B0',bg='#F44336').grid(row=0,columnspan=10)
Label(master,text='Please Select Appropriate Options').grid(row=1,columnspan=10)
def Addata():
    Add=Tk()
    Add.title('Add Section')
    Label(Add,text='Select Appropriate Options',font='20').grid(row=0,columnspan=10)
    def Studata():
        Student=Tk()
        Student.title('Student')
        con=sqlite3.Connection('Studata')
        cur=con.cursor()
        def createdb():
            try:
                cur.execute("create table studentadd(Enroll number primary key,Name varchar(20),Course varchar(10),Address varchar(25),Mobile number)")
                con.commit()
                showinfo('Congrats','Database Created Successfully')
            except:
                showerror('Error','Already Created')
        def deletedb():
            try:
                cur.execute("drop table studentadd")
                con.commit()
                showinfo('Congrats','Database Deleted Successfully')
            except:
                showerror('Error','Database Already Deleted')
        Label(Student,text=' Student Info Section',relief='ridge',width=25,bd=10,font='times 20 bold italic underline',bg='orange').grid(row=0,columnspan=10)
        Label(Student,text='Enter Enroll',font='none 15').grid(row=1)
        Enroll=Entry(Student,font='none 15')
        Enroll.grid(row=1,column=1)
        Label(Student,text='Enter Name',font='none 15').grid(row=2)
        Name=Entry(Student,font='none 15')
        Name.grid(row=2,column=1)
        Label(Student,text='Enter Cousre',font='none 15').grid(row=3)
        Course=Entry(Student,font='none 15')
        Course.grid(row=3,column=1)
        Label(Student,text='Enter Address',font='none 15').grid(row=4)
        Address=Entry(Student,font='none 15')
        Address.grid(row=4,column=1)
        Label(Student,text='Enter Mobile',font='none 15').grid(row=5)
        Mobile=Entry(Student,font='none 15')
        Mobile.grid(row=5,column=1)
        Button(Student,text='Create Database',width=13,command=createdb).grid(row=6)
        Button(Student,text='Delete Database',width=12,command=deletedb).grid(row=6,column=1)
        def Insertdata():
            if Enroll.get()=='':
                showerror('Error','Enrollment Number Not found')
            else:
                a=[(Enroll.get(),Name.get(),Course.get(),Address.get(),Mobile.get())]
                cur.executemany("insert into studentadd values (?,?,?,?,?)",a)
                con.commit()
                showinfo('Congrats','Data Inserted Successfully')
        Button(Student,text='Insert Data',width=13,command=Insertdata).grid(row=7)
        def showall():
            cur.execute("select * from studentadd")
            print cur.fetchall()
        Button(Student,text='Show All',width=12,command=showall).grid(row=7,column=1)
        def destroy():
            Student.destroy()
        Button(Student,text='Click Here to Close',width=25,command=destroy).grid(row=8,columnspan=10)
    Button(Add,text='Student',width=10,bd=10,command=Studata).grid(row=1,column=0,columnspan=10)
    def TeacherData():
        Teacher=Tk()
        Teacher.title('Teacher')
        con=sqlite3.Connection('Teacher')
        cur=con.cursor()
        Label(Teacher,text='Techer Info Section',width=25,bd=10,relief='ridge',font='times 20 bold italic underline',bg='orange').grid(row=0,columnspan=10)
        Label(Teacher,text='Enter ID : ',font='none 15').grid(row=1)
        Id=Entry(Teacher,font='none 15')
        Id.grid(row=1,column=1)
        Label(Teacher,text='Enter Name :',font='none 15').grid(row=2)
        Name=Entry(Teacher,font='none 15')
        Name.grid(row=2,column=1)
        Label(Teacher,text='Subject : ',font='none 15').grid(row=3)
        Subject=Entry(Teacher,font='none 15')
        Subject.grid(row=3,column=1)
        Label(Teacher,text='Enter Date of Joining',font='none 15').grid(row=4)
        DOJ=Entry(Teacher,font='none 15')
        DOJ.grid(row=4,column=1)
        Label(Teacher,text='Enter Qualification',font='none 15').grid(row=5)
        Quali=Entry(Teacher,font='none 15')
        Quali.grid(row=5,column=1)
        Label(Teacher,text='Enter Salary',font='none 15').grid(row=6)
        Salary=Entry(Teacher,font='none 15')
        Salary.grid(row=6,column=1)
        def createdb():
            try:
                cur.execute("create table Teacher(ID number primary key,Name varchar(20),Subject varchar(20),DOJ varchar(20),Quali varchar(20),Salary number)")
                con.commit()
                showinfo('Teacher','Database Created Successfully')
            except:
                showerror('Error','Already Created')
        def deletedb():
            try:
                cur.execute("drop table Teacher")
                con.commit()
                showinfo('Teacher','Database Deleted Successfully')
            except:
                showerror('Error','Already Deleted')
        Button(Teacher,text='Create DB',width=15,height=1,bd=2,command=createdb).grid(row=7)
        Button(Teacher,text='Delete DB',width=17,height=1,bd=2,command=deletedb).grid(row=7,column=1)
        def Insert():
            if Id.get()=='':
                showerror('Error','Enrollment Number Not Found')
            else:
                a=[(Id.get(),Name.get(),Subject.get(),DOJ.get(),Quali.get(),Salary.get())]
                cur.executemany("insert into Teacher values(?,?,?,?,?,?)",a)
                con.commit()
                showinfo('Teacher','Data Inserted Successfully')
        Button(Teacher,text='Insert',width=15,height=1,bd=2,command=Insert).grid(row=8)
        def showall():
            try:
                cur.execute('select * from Teacher')
                print cur.fetchall()
            except:
                showerror('Error','Database not Found')
        Button(Teacher,text='Show All',width=17,height=1,bd=2,command=showall).grid(row=8,column=1)
        def maxsal():
            try:
                cur.execute('select max(Salary) from Teacher')
                print cur.fetchall(),"is the Maximum Salary"
            except:
                showerror('Error','Database not found')
        Button(Teacher,text='Maximum Salary',width=15,height=1,bd=2,command=maxsal).grid(row=9)
        def destroy():
            Teacher.destroy()
        Button(Teacher,text='Click Here To Exit',width=17,height=1,bd=2,command=destroy).grid(row=9,column=1)
    Button(Add,text='Teacher',width=10,bd=10,command=TeacherData).grid(row=2,column=0,columnspan=10)
    def Dest():
        Add.destroy()
    Button(Add,text='Click Here to Exit',width=10,bd=10,command=Dest).grid(row=3,column=0,columnspan=10)
Button(master,text='Add Section',width=15,bd=2,font=' 20',command=Addata).grid(row=2)
def Update():
    Update=Tk()
    Update.title('Update')
    Label(Update,text='Please Click Appropriate Options',relief='ridge',font='times 20 bold italic underline',bg='Yellow',bd=5,fg='#E91E63').grid(row=0)
    def Student():
        StuUpdate=Tk()
        StuUpdate.title('Student Update')
        Label(StuUpdate,text='Welcome to the Student Record Update Section',relief='ridge',font='Arial 20 bold italic',bg='orange').grid(row=0)
        def NameChange():
            con=sqlite3.Connection('Studata')
            cur=con.cursor()
            New=Tk()
            New.title('Name Change')
            Label(New,text='Enter Enrollment Number',font='times 20').grid(row=1)
            Enroll=Entry(New,font='none 15')
            Enroll.grid(row=2)
            Label(New,text='Enter Name to change',font='times 20').grid(row=3)
            Name=Entry(New,font='none 15')
            Name.grid(row=4)
            def UpdateName():
                if Enroll.get()=='':
                    showerror('Error','No Enrollment Found')
                else:
                    a=[Name.get(),Enroll.get()]
                    cur.execute('UPDATE Studentadd set Name=? where Enroll=?',a)
                    con.commit()
                    showinfo('Congrats','Updated Successfully')
            Button(New,text='Update',font='times 20',command=UpdateName).grid(row=5,columnspan=10)
            def dest():
                New.destroy()
            Button(New,text='Return',font='times 20',command=dest).grid(row=6)
        Button(StuUpdate,text='Name',command=NameChange).grid(row=1)
        def UpdateCourse():
            Update=Tk()
            Update.title('Course Update')
            con=sqlite3.Connection('Studata')
            cur=con.cursor()
            Label(Update,text='Course Update',relief='ridge',bd=5,font='times 20 bold',fg='Yellow',bg='Green').grid(row=1,columnspan=10)
            Label(Update,text='Enter Enrollment Number',font='times 20').grid(row=2)
            Enroll=Entry(Update,font='none 20')
            Enroll.grid(row=3)
            Label(Update,text='Course',font='times 20').grid(row=4)
            Course=Entry(Update,font='none 20')
            Course.grid(row=5)
            def Coursee():
                if Enroll.get()=='':
                    showerror('Error','No Enrollment Found')
                else:
                    a=[Course.get(),Enroll.get()]
                    cur.execute('UPDATE Studentadd set Course=? where Enroll=?',a)
                    con.commit()
                    showinfo('Congrats','Data Updated Successfully')
            Button(Update,text='Update',font='times 15',command=Coursee).grid(row=6,columnspan=10)
            def dest():
                Update.destroy()
            Button(Update,text='Return',font='times 15',command=dest).grid(row=7,columnspan=10)
            Update.mainloop()
        Button(StuUpdate,text='Course',command=UpdateCourse).grid(row=2)
        def MobileUpdate():
            Mobilee=Tk()
            Mobilee.title('Mobile Update')
            con=sqlite3.Connection('Studata')
            cur=con.cursor()
            Label(Mobilee,text='Mobile Number Updation',bd=5,relief='ridge',font='times 20',bg='Blue',fg='Green').grid(row=0)
            Label(Mobilee,text='Enter Enrollment',font='times 15').grid(row=1)
            Enroll=Entry(Mobilee,font='none 15')
            Enroll.grid(row=2)
            Label(Mobilee,text='Enter Mobile Number',font='times 15').grid(row=3)
            Mobile=Entry(Mobilee,font='none 15')
            Mobile.grid(row=4)
            def Change():
                if Enroll.get=='':
                    showerror('Error','No Enrollment Number Provided')
                else:
                    a=[Mobile.get(),Enroll.get()]
                    cur.execute('update Studentadd set Mobile=? where Enroll=?',a)
                    con.commit()
                    showinfo('Congratualtions','Updated Successfully')
            Button(Mobilee,text='Update',font='times 10',bd=5,command=Change).grid(row=5)
            def dest():
                Mobilee.destroy()
            Button(Mobilee,text='Return',font='times 10',bd=5,command=dest).grid(row=6)
            Mobilee.mainloop()
        Button(StuUpdate,text='Mobile',command=MobileUpdate).grid(row=3)
        def AddressChange():
            Addr=Tk()
            Addr.title('Address Change')
            con=sqlite3.Connection('Studata')
            cur=con.cursor()
            Label(Addr,text='Address Update Section',font='times 20',bg='Yellow',fg='Red').grid(row=0)
            Label(Addr,text='Enter Enrollment',font='times 18').grid(row=1)
            Enroll=Entry(Addr,font='none 18')
            Enroll.grid(row=2)
            Label(Addr,text='Enter Address',font='times 18').grid(row=3)
            Address=Entry(Addr,font='none 18')
            Address.grid(row=4)
            def Modify():
                if Enroll.get()=='':
                    showerror('Error','Enrollment Not Found')
                else:
                    a=[Address.get(),Enroll.get()]
                    cur.execute('update Studentadd set Address=? where Enroll=?',a)
                    con.commit()
                    showinfo('Congrats','Updated Successfully')
            Button(Addr,text='Update',font='times 15',command=Modify).grid(row=5)
            def dest():
                Addr.destroy()
            Button(Addr,text='Return',font='times 15',command=dest).grid(row=6)
        Button(StuUpdate,text='Address',command=AddressChange).grid(row=4)
        def destroy():
            StuUpdate.destroy()
        Button(StuUpdate,text='Click Here To Exit',command=destroy).grid(row=5)
    Button(Update,text='Student',command=Student).grid(row=1)
    def TeaUp():
        Tea=Tk()
        Tea.title('Teacher Database Update')
        Label(Tea,text='Teacher Database',font='times 20 bold',relief='ridge',bg='Yellow',fg='Green',bd=5).grid(row=0,columnspan=10)
        def NameUp():
            Nam=Tk()
            con=sqlite3.Connection('Teacher')
            cur=con.cursor()
            Nam.title('Teacher Name Update')
            Label(Nam,text='Teacher Name Change',font='times 25 bold',bd=10,relief='ridge',bg='Yellow',fg='Green').grid(row=0,columnspan=10)
            Label(Nam,text='Enter ID',font='times 15').grid(row=1,columnspan=10)
            ID=Entry(Nam,font='none 15')
            ID.grid(row=2,columnspan=10)
            Label(Nam,text='Enter Name',font='times 15').grid(row=3,columnspan=10)
            Name=Entry(Nam,font='none 15')
            Name.grid(row=4,columnspan=10)
            def Up():
                if ID.get()=='':
                    showerror('Error','Enrollment Number Not Found')
                else:
                    a=[Name.get(),ID.get()]
                    cur.execute('update Teacher set Name=? where ID=?',a)
                    con.commit()
                    showinfo('Congrats','Updated Successfully')
            Button(Nam,text='Update',font='times 15',command=Up).grid(row=5,columnspan=10)
            def dest():
                Nam.destroy()
            Button(Nam,text='Return',font='times 15',command=dest).grid(row=6,columnspan=10)
            Nam.mainloop()
        Button(Tea,text='Name',font='times 15',width=15,bd=2,padx=5,command=NameUp).grid(row=1,column=0)
        def SubUp():
            Sub=Tk()
            Sub.title('Subject Change')
            con=sqlite3.Connection('Teacher')
            cur=con.cursor()
            Label(Sub,text='Subject Update',font='times 25 bold',relief='ridge',bd=10,bg='Yellow',fg='Green').grid(row=0,columnspan=10)
            Label(Sub,text='Enter ID',font='times 15 bold').grid(row=1,columnspan=10)
            ID=Entry(Sub,font='none 15')
            ID.grid(row=2,columnspan=10)
            Label(Sub,text='Enter Subject',font='times 15 bold').grid(row=3,columnspan=10)
            Subject=Entry(Sub,font='none 15')
            Subject.grid(row=4,columnspan=10)
            def Up():
                if ID.get()=='':
                    showerror('Error','No Enrollment Found')
                else:
                    a=[Subject.get(),ID.get()]
                    cur.execute('update Teacher set Subject=? where ID=?',a)
                    con.commit()
                    showinfo('Congrats','Updated Successfully')
            Button(Sub,text='Submit',font='times 15 bold',command=Up).grid(row=5,columnspan=10)
            def dest():
                Sub.destroy()
            Button(Sub,text='Return',font='times 15 bold',command=dest).grid(row=6,columnspan=10)
            Sub.mainloop()
        Button(Tea,text='Subject',font='times 15',width=15,bd=2,command=SubUp).grid(row=1,column=1)
        def DOJUp():
            DJ=Tk()
            DJ.title('DOB Changer')
            con=sqlite3.Connection('Teacher')
            cur=con.cursor()
            Label(DJ,text='DOJ Changer',font='times 25 bold',relief='ridge',bd=10,fg='Yellow',bg='Green').grid(row=0,columnspan=10)
            Label(DJ,text='Enter ID',font='times 20 bold').grid(row=1,columnspan=10)
            ID=Entry(DJ,font='none 20')
            ID.grid(row=2,columnspan=10)
            Label(DJ,text='Enter DOJ in dd/mm/yyyy',font='times 20 bold',padx=10).grid(row=3,columnspan=10)
            DOJ=Entry(DJ,font='none 20')
            DOJ.grid(row=4,columnspan=10)
            def DJUP():
                if ID.get()=='':
                    showerror('Error','Enrollment Not Found')
                else:
                    a=[DOJ.get(),ID.get()]
                    cur.execute('update Teacher set DOJ=? where ID=?')
                    con.commit()
                    showinfo('Congrats','Updated Successfully')
            Button(DJ,text='Submit',font='times 19',command=DJUP).grid(row=5,columnspan=10)
            def dest():
                DJ.destroy()
            Button(DJ,text='Return',font='times 19',command=dest).grid(row=6,columnspan=10)
            DJ.mainloop()
        Button(Tea,text='DOJ',font='times 15',width=15,bd=2,padx=5,command=DOJUp).grid(row=2,column=0)
        def QualiUp():
            Quali=Tk()
            Quali.title('Qualification Changer')
            con=sqlite3.Connection('Teacher')
            cur=con.cursor()
            Label(Quali,text='Qualification Changer',font='times 25 bold',relief='ridge',bd='10',fg='Red',bg='Yellow').grid(row=0,columnspan=10)
            Label(Quali,text='Enter ID',font='times 20').grid(row=1,columnspan=10)
            ID=Entry(Quali,font='none 20')
            ID.grid(row=2,columnspan=10)
            Label(Quali,text='Enter Qualification',font='times 20').grid(row=3,columnspan=10)
            Qualif=Entry(Quali,font='none 20')
            Qualif.grid(row=4,columnspan=10)
            def UPP():
                if ID.get()=='':
                    showerror('Error','Enrollment Not Found')
                else:
                    a=[Qualif.get(),ID.get()]
                    cur.execute('update Teacher set Quali=? where ID=?',a)
                    con.commit()
                    showinfo('Congrats','Updated Successfully')
            Button(Quali,text='Update',font='times 20',command=UPP).grid(row=5,columnspan=10)
            def dest():
                Quali.destroy()
            Button(Quali,text='Return',font='times 20',command=dest).grid(row=6,columnspan=10)
            Quali.mainloop()
        Button(Tea,text='Qualification',font='times 15',width=15,bd=2,command=QualiUp).grid(row=2,column=1)
        def SalaryUp():
            Sal=Tk()
            Sal.title('Salary Update')
            con=sqlite3.Connection('Teacher')
            cur=con.cursor()
            Label(Sal,text='Salary Update',font='times 25 bold',relief='ridge',bd=10,bg='Yellow',fg='Green').grid(row=0,columnspan=10)
            Label(Sal,text='Enter ID',font='times 20 bold').grid(row=1,columnspan=10)
            ID=Entry(Sal,font='none 20')
            ID.grid(row=2,columnspan=10)
            Label(Sal,text='Salary',font='times 20 bold').grid(row=3,columnspan=10)
            Salary=Entry(Sal,font='none 20')
            Salary.grid(row=4,columnspan=10)
            def SalUP():
                if ID.get()=='':
                    showerror('Error','No Enrollment Found')
                else:
                    a=[Salary.get(),ID.get()]
                    cur.execute('update Teacher set Salary=? where ID=?',a)
                    con.commit()
                    showinfo('Congrats','Updated Successfully')
            Button(Sal,text='Update',font='times 20',command=SalUP).grid(row=5,columnspan=10)
            def dest():
                Sal.destroy()
            Button(Sal,text='Return',font='times 20',command=dest).grid(row=6,columnspan=10)
            Sal.mainloop()
        Button(Tea,text='Salary',font='times 15',width=15,bd=2,padx=5,command=SalaryUp).grid(row=3)
        def dest():
            Tea.destroy()
        Button(Tea,text='Exit',width=16,font='times 15',bd=2,padx=5,command=dest).grid(row=3,column=1)
        Tea.mainloop()
    Button(Update,text='Teacher',command=TeaUp).grid(row=2)
    def destroy():
        Update.destroy()
    Button(Update,text='Click Here to Exit',command=destroy).grid(row=3)
Button(master,text='Update Section',width=15,bd=2,font=' 20',command=Update).grid(row=2,column=1)
def SalrySec():
    Sala=Tk()
    Sala.title('Salary Section')
    Label(Sala,text='Account Department',width=25,font='times 25 bold',relief='ridge',bd=10,bg='Green',fg='Red').grid(row=0,columnspan=10)
    def MaxSal():
        con=sqlite3.Connection('Teacher')
        cur=con.cursor()
        cur.execute('select Name,max(Salary) from Teacher')
        a=cur.fetchall()
        showinfo('Congrats',a)
    Button(Sala,text='Max Salary',bd=10,font='times 20',width=15,command=MaxSal).grid(row=1)
    def MinSal():
        con=sqlite3.Connection('Teacher')
        cur=con.cursor()
        cur.execute('select Name,min(Salary) from Teacher')
        a=cur.fetchall()
        showinfo('Congrats',a)
    Button(Sala,text='Min Salary',bd=10,font='times 20',width=15,command=MinSal).grid(row=1,column=1)
    Button(Sala,text='Tax Calc.',bd=10,font='times 20',width=15).grid(row=2)
    def dest():
        Sala.destroy()
    Button(Sala,text='Exit',font='times 20',bd=10,width=15,command=dest).grid(row=2,column=1)
    Sala.mainloop()
Button(master,text='Salary Section',width=15,bd=2,font=' 20',command=SalrySec).grid(row=3)
def Dele():
    DEL=Tk()
    DEL.title('Remove Zone')
    Label(DEL,text='Delete Zone',font='times 25',relief='ridge',bd=10,bg='Yellow',fg='Brown').grid(row=0,columnspan=10)
    def STUDENT():
        S=Tk()
        S.title('Student Delete')
        con=sqlite3.Connection('Studata')
        cur=con.cursor()
        Label(S,text='Student Delete',font='times 25',relief='ridge',bd=10,bg='Red',fg='yellow').grid(row=0,columnspan=10)
        Label(S,text='Enter Enroll',font='times 20').grid(row=1,columnspan=10)
        Enroll=Entry(S,font='none 20')
        Enroll.grid(row=2,columnspan=10)
        def Sub():
            if Enroll.get()=='':
                showerror('Error','No Enrollment Found')
            else:
                a=[Enroll.get()]
                cur.execute('delete from Studentadd where Enroll=?',a)
                con.commit()
                showinfo('Congrats','Deleted Successfully')
        Button(S,text='Delete',width=15,bd=5,font='times 15',command=Sub).grid(row=3,columnspan=10)
        def dest():
            S.destroy()
        Button(S,text='Return',width=15,bd=5,font='times 15',command=dest).grid(row=4,columnspan=10)
    Button(DEL,text='Student',font='times 20',width=15,bd=5,command=STUDENT).grid(row=1,columnspan=10)
    def TEACHER():
        TEACH=Tk()
        TEACH.title('Teacher Delete')
        con=sqlite3.Connection('Teacher')
        cur=con.cursor()
        Label(TEACH,text='Teacher Delete',font='times 25',relief='ridge',bd=10,bg='Yellow',fg='Red').grid(row=0,columnspan=10)
        Label(TEACH,text='Enter Enroll',font='times 20').grid(row=1,columnspan=10)
        ID=Entry(TEACH,font='none 20')
        ID.grid(row=2,columnspan=10)
        def DT():
            if ID.get()=='':
                showerror('Error','Enrollment Not Found')
            else:
                a=[ID.get()]
                cur.execute('delete from Teacher where ID=?',a)
                con.commit()
                showinfo('Congrats','Deleted Successfully')
        Button(TEACH,text='Delete',font='times 15',width=15,bd=5,command=DT).grid(row=3,columnspan=10)
        def dest():
            TEACH.destroy()
        Button(TEACH,text='Return',font='times 15',width=15,bd=5,command=dest).grid(row=4,columnspan=10)
    Button(DEL,text='Teacher',font='times 20',width=15,bd=5,command=TEACHER).grid(row=2,columnspan=10)
    def dest():
        DEL.destroy()
    Button(DEL,text='Return ',font='times 20',width=15,bd=5,command=dest).grid(row=3,columnspan=10)
Button(master,text='Delete Account',width=15,bd=2,font=' 20',command=Dele).grid(row=3,column=1)
def Search():
    Search=Tk()
    Search.title('Searching Center')
    Label(Search,text='Search Zone',relief='ridge',bd=10,font='times 20 bold',bg='yellow',fg='green').grid(row=0,columnspan=10)
    def StuSearch():
        Stu=Tk()
        Stu.title('Student Search Zone')
        con=sqlite3.Connection('Studata')
        cur=con.cursor()
        Label(Stu,text='Student Search',font='times 25',relief='ridge',bd=5,bg='Green',fg='Yellow').grid(row=0,columnspan=10)
        Label(Stu,text='Enter Enrollment',font='times 20').grid(row=1,columnspan=10)
        Enroll=Entry(Stu,font='none 20')
        Enroll.grid(row=2,columnspan=10)
        def SE():
            a=[Enroll.get()]
            cur.execute('select * from Studentadd where Enroll=?',a)
            b=cur.fetchall()
            showinfo('Congrats',b)
        Button(Stu,text='Search',font='times 20',command=SE).grid(row=3,columnspan=10)
        def dest():
            Stu.destroy()
        Button(Stu,text='Return',font='times 20',command=dest).grid(row=4,columnspan=10)
        Stu.mainloop()
    Button(Search,text='Student',font='times 15',bd=5,command=StuSearch).grid(row=1)
    def TeaSear():
        TS=Tk()
        TS.title('Teacher Search Zone')
        con=sqlite3.Connection('Teacher')
        cur=con.cursor()
        Label(TS,text='Teacher Search',font='times 25',relief='ridge',bd=5,bg='Yellow',fg='Green').grid(row=0,columnspan=10)
        Label(TS,text='Enter ID',font='times 20').grid(row=1,columnspan=10)
        ID=Entry(TS,font='none 20')
        ID.grid(row=2,columnspan=10)
        def SS():
            a=[ID.get()]
            cur.execute('select * from Teacher where ID=?',a)
            b=cur.fetchall()
            showinfo('Congrats',b)
        Button(TS,text='Search',font='times 15',command=SS).grid(row=3,columnspan=10)
        def dest():
            TS.destroy()
        Button(TS,text='Return',font='times 15',command=dest).grid(row=4,columnspan=10)
    Button(Search,text='Teacher',font='times 15',bd=5,command=TeaSear).grid(row=1,column=1)
    def dest():
        Search.destroy()
    Button(Search,text='Main Menu',font='times 15',bd=2,command=dest).grid(row=2,columnspan=10)
    Search.mainloop()
Button(master,text='Search Zone',width=15,bd=2,font=' 20',command=Search).grid(row=4)
def Logout():
    master.destroy()
    Add.destroy()
    Student.destroy()
    Teacher.destroy()
    Update.destroy()
    StuUpdate.destroy()
    New.destroy()
    Update.destroy()
    Mobilee.destroy()
    Addr.destroy()
    Tea.destroy()
    Nam.destroy()
    Sub.destroy()
    DJ.destroy()
    Quali.destroy()
    Sal.destroy()
    Sala.destroy()
    DEL.destroy()
    TEACH.destroy()
    Search.destroy()
    TS.destroy()
Button(master,text='Sign Out',width=15,bd=2,font=' 20',command=Logout).grid(row=4,column=1)
master.mainloop()
