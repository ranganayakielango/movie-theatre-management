from tkinter import *
import cx_Oracle
con = cx_Oracle.connect('system/goldblock')
curs = con.cursor()
curs.arraysize = 50

def empwin():
    def addem():
        def added():

            curs.execute('select max(empid) from employee')
            e=curs.fetchone()
            empid=e[0]+1
            name=bname.get()
            sal=bsal.get()
            cont=bcon.get()

            curs.execute('insert into employee values(:1, :2, :3, :4)', (empid,name,sal,cont))
            curs.execute('commit')
            print('Inserted')
            print(empid,name,sal,cont)

        add=Tk()
        add.geometry("240x360")

        t = Label(add, text="Add Employee", font=("Helvetica", 15))
        t.place(x=120, y=20, anchor=CENTER)

        lname=Label(add,text="NAME")
        lname.place(x=0,y=60)
        bname=Entry(add)
        bname.place(x=80,y=60)

        lsal=Label(add,text="SALARY")
        lsal.place(x=0,y=120)
        bsal=Entry(add)
        bsal.place(x=80,y=120)

        lcon=Label(add,text="CONTACT")
        lcon.place(x=0,y=180)
        bcon=Entry(add)
        bcon.place(x=80,y=180)

        badd=Button(add,text="ADD",command=added,bg='black', fg='white')
        badd.place(x=80,y=240)

        add.mainloop()
    def remem():
        def removed():
            #global bname
            empid=bname.get()
            remQuery='DELETE FROM employee WHERE empid='+str(empid)
            curs.execute(remQuery)
            curs.execute('commit')
            print("Removed!")


        rem=Tk()
        rem.geometry("240x240")

        t = Label(rem, text="Remove Employee", font=("Helvetica", 15))
        t.place(x=120, y=20, anchor=CENTER)

        lname = Label(rem, text="ID")
        lname.place(x=0, y=60)
        bname = Entry(rem)
        bname.place(x=80, y=60)

        badd = Button(rem, text="REMOVE", command=removed,bg='black', fg='white')
        badd.place(x=80, y=120)

        rem.mainloop()

    def searchem():
        def found():

            eid=bid.get()
            searchQuery='select * from employee where empid = '+str(eid)
            curs.execute(searchQuery)
            serDis=Tk()
            serDis.geometry("240x360")
            for c1,c2,c3,c4 in curs.fetchall():
                #print(str(c1)+"      "+str(c2)+"      "+str(c3)+"      "+str(c4)+"\n")
                #Label(serDis, text=str(c1)+"      "+str(c2)+"      "+str(c3)+"      "+str(c4)).place(x=120, y=20, anchor=CENTER)
                Label(serDis, text='Employee Id :'+str(c1)).grid(row=0, column=0)
                Label(serDis, text='Name        :'+str(c2)).grid(row=1, column=0)
                Label(serDis, text='Salary      :'+str(c3)).grid(row=2, column=0)
                Label(serDis, text='Contact     :'+str(c4)).grid(row=3, column=0)
           # print("found!")

        ser = Tk()
        ser.geometry("240x360")


        t = Label(ser, text="Search Employee", font=("Helvetica", 15))
        t.place(x=120, y=20, anchor=CENTER)

        lid = Label(ser, text="ID")
        lid.place(x=0, y=60)
        bid = Entry(ser)
        bid.place(x=80, y=60)

        bser = Button(ser, text="SEARCH", command=found,bg='black', fg='white')
        bser.place(x=80, y=120)
        #curs.close
        #con.close

        ser.mainloop()
    def listem():

        searchQuery='select * from employee'
        curs.execute(searchQuery)
        serDis=Tk()
        serDis.geometry("300x360")
        Label(serDis, text='Employee Id').grid(row=0, column=0)
        Label(serDis, text='Name').grid(row=0, column=1)
        Label(serDis, text='Salary').grid(row=0, column=2)
        Label(serDis, text='Contact').grid(row=0, column=3)
        i=1
        for c1,c2,c3,c4 in curs.fetchall():
            #Label(serDis, text=str(c1)+"      "+str(c2)+"      "+str(c3)+"      "+str(c4)).place(x=120, y=20+(i*20), anchor=CENTER)
            Label(serDis, text=str(c1)).grid(row=i, column=0)
            Label(serDis, text=str(c2)).grid(row=i, column=1)
            Label(serDis, text=str(c3)).grid(row=i, column=2)
            Label(serDis, text=str(c4)).grid(row=i, column=3)
            i = i + 1
        #curs.close
        #con.close
        serDis.quit()

    def modem():
        def moded():
            #global bname
            #global bsal
            #global bcon
            empid=bnum.get()
            name=bname.get()
            sal=bsal.get()
            cont=bcon.get()
            modQuery="UPDATE employee SET name = '"+name+"', salary = "+str(sal)+", contact = "+str(cont)+"WHERE empid ="+str(empid)
            curs.execute(modQuery)
            curs.execute('commit')
            print("Value updated")

        mod = Tk()
        mod.geometry("240x360")

        t = Label(mod, text="Mod Employee", font=("Helvetica", 15))
        t.place(x=120, y=20, anchor=CENTER)

        lnum = Label(mod, text="ID")
        lnum.place(x=0, y=60)
        bnum = Entry(mod)
        bnum.place(x=80, y=60)

        lname = Label(mod, text="NAME")
        lname.place(x=0, y=120)
        bname = Entry(mod)
        bname.place(x=80, y=120)

        lsal = Label(mod, text="SALARY")
        lsal.place(x=0, y=180)
        bsal = Entry(mod)
        bsal.place(x=80, y=180)

        lcon = Label(mod, text="CONTACT")
        lcon.place(x=0, y=240)
        bcon = Entry(mod)
        bcon.place(x=80, y=240)

        bmod = Button(mod, text="MODIFY", command=moded,bg='black', fg='white')
        bmod.place(x=80, y=300)

    emp = Tk()
    emp.geometry("640x360")

    title = Label(emp, text="Employee Management", font=("Helvetica", 20))
    title.place(x=320, y=20, anchor=CENTER)

    b1 = Button(emp, text="Add Employee", width=20, command=addem,bg='black', fg='white')
    b1.place(x=245, y=80)

    b2 = Button(emp, text="Remove Employee", width=20, command=remem,bg='black', fg='white')
    b2.place(x=245, y=120)

    b3 = Button(emp, text="List Employees", width=20,command=listem,bg='black', fg='white')
    b3.place(x=245, y=160)

    b4 = Button(emp, text="Search Employee", width=20, command=searchem,bg='black', fg='white')
    b4.place(x=245, y=200)

    b5 = Button(emp, text="Modify Employee", width=20, command=modem,bg='black', fg='white')
    b5.place(x=245, y=240)

    con.close
    curs.close
    emp.mainloop()
