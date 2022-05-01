from tkinter import *
import cx_Oracle
con = cx_Oracle.connect('system/goldblock')
curs = con.cursor()
curs.arraysize = 50

def adwin():
    def addem():
        def added():
            admid=bname.get()
            pswd=bpass.get()

            curs.execute('insert into admin values(:1, :2)', (admid,pswd))
            curs.execute('commit')

        add=Tk()
        add.geometry("240x360")

        t = Label(add, text="Add Admin", font=("Helvetica", 15))
        t.place(x=120, y=20, anchor=CENTER)

        lname=Label(add,text="ID")
        lname.place(x=0,y=60)
        bname=Entry(add)
        bname.place(x=80,y=60)

        lpass = Label(add, text="PASSWORD")
        lpass.place(x=0, y=120)
        bpass = Entry(add,show='*')
        bpass.place(x=80, y=120)

        badd = Button(add, text="ADD", command=added,bg='black', fg='white')
        badd.place(x=80, y=180)

        add.mainloop()
    def remem():
        def removed():
            #global bname
            admid=bname.get()
            remQuery='DELETE FROM admin WHERE empid='+str(admid)
            curs.execute(remQuery)
            curs.execute('commit')
            print("Removed!")

        rem=Tk()
        rem.geometry("240x240")

        t = Label(rem, text="Remove Admin", font=("Helvetica", 15))
        t.place(x=120, y=20, anchor=CENTER)

        lname = Label(rem, text="ID")
        lname.place(x=0, y=60)
        bname = Entry(rem)
        bname.place(x=80, y=60)

        badd = Button(rem, text="REMOVE", command=removed,bg='black', fg='white')
        badd.place(x=80, y=120)

        rem.mainloop()

    adm = Tk()
    adm.geometry("640x360")

    title = Label(adm, text="Administrator Management", font=("Helvetica", 20))
    title.place(x=320, y=20, anchor=CENTER)

    b1 = Button(adm, text="Add Admin", width=20, command=addem,bg='black', fg='white')
    b1.place(x=245, y=80)

    b2 = Button(adm, text="Remove Admin", width=20, command=remem,bg='black', fg='white')
    b2.place(x=245, y=120)

    con.close
    curs.close
    adm.mainloop()

