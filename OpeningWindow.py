from tkinter import *
import Manage
import cx_Oracle

def validate():
    global win
    global idEntry
    global pdEntry
    global curs
    eid=idEntry.get()
    pswd=pdEntry.get()
    s1='select * from admin where empid='+str(eid)
    curs.execute(s1)
    f=0
    for c1,c2 in curs.fetchall():
        if(c2==pswd):
            f=1
    if f==0:
        l3 = Label(win, text="INVALID", anchor=CENTER, font=("Helvetica", 10))
        l3.place(x=295,y=260)
    else:
        Manage.mainwin()


con = cx_Oracle.connect('system/goldblock')
curs = con.cursor()
win=Tk()
win.geometry("640x360")

title=Label(win,text="ADMIN LOGIN",font=("Helvetica", 20))
title.place(x=320,y=20,anchor=CENTER)

l=Label(win,text="ID",anchor=CENTER,font=("Helvetica", 10))
l.place(x=220, y=140, anchor="center")
idEntry=Entry(win)
idEntry.place(x=340,y=130)

l2=Label(win,text="PASSWORD",anchor=CENTER,font=("Helvetica", 10))
l2.place(x=210, y=160)
pdEntry=Entry(win, show="*")
pdEntry.place(x=340,y=160)

B=Button(win,text="LOGIN",command=validate,activebackground='violet',activeforeground='blue',bg='black', fg='white')
B.place(x=300,y=200)
win.mainloop()
