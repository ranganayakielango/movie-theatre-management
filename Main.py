from tkinter import *
import cx_Oracle
con = cx_Oracle.connect('system/goldblock')
curs = con.cursor()
curs.arraysize = 50

def tick():
    def bookTic():
        mid=bname.get()
        num=int(bnum.get())
        bookQuery='select ticketsBooked from movie where movieid = '+str(mid)
        curs.execute(bookQuery)
        Tick=curs.fetchone()
        availTick=200-int(Tick[0])
        print(availTick)
        if(num>availTick):
            Label(tickwin, text="Tickets Unavailable!").place(x=55, y=250)
        else:
            Label(tickwin, text="Booked!").place(x=80, y=250)
            tickBooked = int(Tick[0]) + num
            modQuery = 'UPDATE movie SET ticketsBooked = ' + str(tickBooked) + 'where movieid = ' + str(mid)
            curs.execute(modQuery)
            curs.execute('commit')

    tickwin=Tk()
    tickwin.geometry("240x360")

    title = Label(tickwin, text="BOOK TICKETS", font=("Helvetica", 20))
    title.place(x=120, y=20, anchor=CENTER)

    lname = Label(tickwin, text="MOVIE ID")
    lname.place(x=0, y=60)
    bname = Entry(tickwin)
    bname.place(x=100, y=60)

    lnum = Label(tickwin, text="NO. OF TICKETS")
    lnum.place(x=0, y=120)
    bnum = Entry(tickwin)
    bnum.place(x=100, y=120)

    b3 = Button(tickwin, text="Book", command=bookTic,bg='black', fg='white')
    b3.place(x=100, y=190, anchor=CENTER)

    tickwin.mainloop()

def viewcin():
    searchQuery = 'select * from movie'
    curs.execute(searchQuery)
    serDis = Tk()
    serDis.geometry("300x360")
    Label(serDis, text='Movie Id').grid(row=0, column=0)
    Label(serDis, text='Name').grid(row=0, column=1)
    Label(serDis, text='Screen').grid(row=0, column=2)
    Label(serDis, text='Length').grid(row=0, column=3)
    Label(serDis, text='Available Tickets').grid(row=0, column=4)
    i = 1
    #Label(serDis, text='Movie ID    Name    Screen  Available Tickets').place(x=120, y=10, anchor=CENTER)
    for c1, c2, c3, c4, c5 in curs.fetchall():
        #Label(serDis, text=str(c1) + "      " + str(c2) + "      " + str(c3)+"      "+str(200-c5)).place(x=120,y=20 + (i * 20),anchor=CENTER)
        Label(serDis, text=str(c1)).grid(row=i,column=0)
        Label(serDis, text=str(c2)).grid(row=i, column=1)
        Label(serDis, text=str(c3)).grid(row=i, column=2)
        Label(serDis, text=str(c4)).grid(row=i, column=3)
        Label(serDis, text=str(200-c5)).grid(row=i, column=4)
        i = i + 1


window=Tk()
window.geometry("640x360")

title=Label(window,text="THE CINEMAS",font=("Helvetica", 20))
title.place(x=320,y=20,anchor=CENTER)

b1=Button(window,text="View Movies",command=viewcin,bg='black', fg='white')
b1.place(x=320,y=100,anchor=CENTER)

b2=Button(window,text="Book Tickets",command=tick,bg='black', fg='white')
b2.place(x=320,y=140,anchor=CENTER)

con.close
curs.close
window.mainloop()