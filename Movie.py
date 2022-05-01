from tkinter import *
import cx_Oracle
con = cx_Oracle.connect('system/goldblock')
curs = con.cursor()
curs.arraysize = 50

def movwin():
    def addmov():
        def added():
            curs.execute('select max(movieid) from movie')
            e=curs.fetchone()
            movid=int(e[0])+1
            name=bname.get()
            scr=bsal.get()
            length=bcon.get()

            curs.execute('insert into movie values(:1, :2, :3, :4, :5)', (movid,name,scr,length,0))
            curs.execute('commit')
            #con.commit
            print('Inserted')
        add=Tk()
        add.geometry("240x360")

        t = Label(add, text="Add Movie", font=("Helvetica", 15))
        t.place(x=120, y=20, anchor=CENTER)

        lname=Label(add,text="NAME")
        lname.place(x=0,y=60)
        bname=Entry(add)
        bname.place(x=80,y=60)

        lsal=Label(add,text="SCREEN")
        lsal.place(x=0,y=120)
        bsal=Entry(add)
        bsal.place(x=80,y=120)

        lcon=Label(add,text="LENGTH")
        lcon.place(x=0,y=180)
        bcon=Entry(add)
        bcon.place(x=80,y=180)

        badd=Button(add,text="ADD",command=added,bg='black', fg='white')
        badd.place(x=80,y=240)

        add.mainloop()
    def remem():
        def removed():
            #global bname
            movid=bname.get()
            remQuery='DELETE FROM movie WHERE movieid='+str(movid)
            curs.execute(remQuery)
            curs.execute('commit')
            print("Removed!")

        rem=Tk()
        rem.geometry("240x240")

        t = Label(rem, text="Remove Movie", font=("Helvetica", 15))
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
            searchQuery='select * from movie where movieid = '+str(eid)
            curs.execute(searchQuery)
            serDis=Tk()
            serDis.geometry("240x360")
            for c1,c2,c3,c4,c5 in curs.fetchall():
                #print(str(c1)+"      "+str(c2)+"      "+str(c3)+"      "+str(c4)+"\n")
                #Label(serDis, text=str(c1)+"      "+str(c2)+"      "+str(c3)+"      "+str(c4)).place(x=120, y=20, anchor=CENTER)
                Label(serDis, text='Movie ID    :'+str(c1)).grid(row=0,column=0)
                Label(serDis, text='Movie Name  :'+str(c2)).grid(row=1,column=0)
                Label(serDis, text='Screen No.  :'+str(c3)).grid(row=2,column=0)
                Label(serDis, text='Length      :'+str(c4)).grid(row=3,column=0)
                Label(serDis, text='Available Tickets     :'+str(200 - c5)).grid(row=4,column=0)
           # print("found!")

        ser = Tk()
        ser.geometry("240x360")


        t = Label(ser, text="Search Movie", font=("Helvetica", 15))
        t.place(x=120, y=20, anchor=CENTER)

        lid = Label(ser, text="ID")
        lid.place(x=0, y=60)
        bid = Entry(ser)
        bid.place(x=80, y=60)

        bser = Button(ser, text="SEARCH", command=found,bg='black', fg='white')
        bser.place(x=80, y=120)

        ser.mainloop()
    def listem():

        searchQuery='select * from movie'
        curs.execute(searchQuery)
        serDis=Tk()
        serDis.geometry("300x360")
        Label(serDis, text='Movie Id').grid(row=0, column=0)
        Label(serDis, text='Name').grid(row=0, column=1)
        Label(serDis, text='Screen').grid(row=0, column=2)
        Label(serDis, text='Length').grid(row=0, column=3)
        Label(serDis, text='Available Tickets').grid(row=0, column=4)
        i=1
        for c1,c2,c3,c4,c5 in curs.fetchall():
            #Label(serDis, text=str(c1)+"      "+str(c2)+"      "+str(c3)+"      "+str(c4)).place(x=120, y=20+(i*20), anchor=CENTER)
            Label(serDis, text=str(c1)).grid(row=i, column=0)
            Label(serDis, text=str(c2)).grid(row=i, column=1)
            Label(serDis, text=str(c3)).grid(row=i, column=2)
            Label(serDis, text=str(c4)).grid(row=i, column=3)
            Label(serDis, text=str(200 - c5)).grid(row=i, column=4)
            i = i + 1
        #curs.close
        #con.close

    mov = Tk()
    mov.geometry("640x360")

    title = Label(mov, text="Movie Management", font=("Helvetica", 20))
    title.place(x=320, y=20, anchor=CENTER)

    b1 = Button(mov, text="Add Movie", width=20, command=addmov,bg='black', fg='white')
    b1.place(x=245, y=80)

    b2 = Button(mov, text="Remove Movie", width=20, command=remem,bg='black', fg='white')
    b2.place(x=245, y=120)

    b3 = Button(mov, text="List Movies", width=20,command=listem,bg='black', fg='white')
    b3.place(x=245, y=160)

    b4 = Button(mov, text="Search Movie", width=20, command=searchem,bg='black', fg='white')
    b4.place(x=245, y=200)


    con.close
    curs.close
    mov.mainloop()