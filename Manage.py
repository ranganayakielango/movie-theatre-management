import cx_Oracle
from tkinter import *
import Employee
import Admin
import Movie

def mainwin():
    def manemp():
        Employee.empwin()
    def manmov():
        Movie.movwin()
    def manad():
        Admin.adwin()
    def reset():
        con = cx_Oracle.connect('system/goldblock')
        curs = con.cursor()
        curs.arraysize = 50
        curs.execute('UPDATE movie SET ticketsBooked = 0')
        curs.execute('commit')
        con.close
        curs.close
    managewin=Tk()
    managewin.geometry("640x360")

    title = Label(managewin, text="WELCOME ADMIN", font=("Helvetica", 20))
    title.place(x=320, y=20, anchor=CENTER)

    b1=Button(managewin,text="Manage Employee",width=20,command=manemp, bg='black', fg='white')
    b1.place(x=245,y=100)

    b2 = Button(managewin, text="Manage Movie",width=20,command=manmov, bg='black', fg='white')
    b2.place(x=245, y=150)

    b3 = Button(managewin, text="Add Admin",width=20,command=manad, bg='black', fg='white')
    b3.place(x=245, y=200)

    b4 = Button(managewin, text="Reset Bookings", command=reset, width=20, bg='black', fg='white')
    b4.place(x=245, y=250)

    managewin.mainloop()