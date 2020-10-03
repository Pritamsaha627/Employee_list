# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 21:07:35 2020

@author: Pritam Saha
"""

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3
root = Tk()
root.minsize(800,800)
root.title("Employee Details")
f55 = None
def register():
    f3 = Frame(bg = "pink")
    f3.place(x=0,y=0,width = 800,height = 800)
    r1=StringVar()
    r2=StringVar()
    r3=StringVar()
    un1 = Label(f3,text="Employee ID",bg="blue",fg="white")
    un1.place(x=100,y=100)
    e1 = Entry(f3,font=("",10),textvariable=r1)
    e1.place(x=220,y=100)
    un2 = Label(f3,text="Name",bg="blue",fg="white")
    un2.place(x=100,y=150)
    e2 = Entry(f3,font=("",10),textvariable=r2)
    e2.place(x=220,y=150)
    un3 = Label(f3,text="Password",bg="blue",fg="white")
    un3.place(x=100,y=200)
    e3 = Entry(f3,font=("",10),textvariable=r3)
    e3.place(x=220,y=200)
    def regis1():
        db=sqlite3.connect("employee_list.db")
        cr = db.cursor()
        try:
            cr.execute("insert into register values('"+r1.get()+"','"+r2.get()+"','"+r3.get()+"')")
            messagebox.showinfo('Title','Registered Successfully!!')
        except (sqlite3.IntegrityError):
            messagebox.showinfo('Title','Employee ID already exist')
        db.commit()
        db.close()
        r1.set("")
        r2.set("")
        r3.set("")

    b1 = Button(f3,text="Back",command=main)
    b1.place(x=0,y=0,width=60,height=30)
    b2 = Button(f3,text="Register",command = regis1)
    b2.place(x=250,y=250,width=60,height=30)
def menu(x):
    n=ttk.Notebook()
    n.place(x=0,y=0,width=800,height=800)
    insertdata(x,n)
    showall(n)
    search(n)
    updatedata(n)
    logout(n)
def insertdata(x,n):
    f4 = Frame(bg="cyan")
    n.add(f4,text="Insert")
    i1=StringVar()
    i2=StringVar()
    i3=StringVar()
    un4 = Label(f4,text=f"Welcome {x}",font=("",20),bg="blue",fg="white")
    un4.place(x=0,y=0)
    un1 = Label(f4,text="Mobile No.",bg="blue",fg="white")
    un1.place(x=100,y=100)
    e1 = Entry(f4,font=("",10),textvariable=i1)
    e1.place(x=220,y=100)
    un2 = Label(f4,text="Email",bg="blue",fg="white")
    un2.place(x=100,y=150)
    e2 = Entry(f4,font=("",10),textvariable=i2)
    e2.place(x=220,y=150)
    un3 = Label(f4,text="Salary",bg="blue",fg="white")
    un3.place(x=100,y=200)
    e3 = Entry(f4,font=("",10),textvariable=i3)
    e3.place(x=220,y=200)
    def insert1(x):
        db=sqlite3.connect("employee_list.db")
        cr = db.cursor()
        try:
            cr.execute("insert into ins(insert_by,mobile,email,salary) values('"+x+"','"+i1.get()+"','"+i2.get()+"','"+i3.get()+"')")
            messagebox.showinfo('Title','Data insert Successfully!!')
        except:
            messagebox.showinfo('Title','Error')
        db.commit()
        db.close()
        i1.set("")
        i2.set("")
        i3.set("")
        showalldata1(f55)
    b2 = Button(f4,text="Insert",command=lambda : insert1(x))
    b2.place(x=250,y=250,width=60,height=30)
    
def showall(n):
    f5 = Frame(bg="cyan")
    global f55
    f55 = f5
    n.add(f5,text="Show All")
    showalldata1(f5)
def showalldata1(f5):
    u1 = Label(f5,text="Insert By",font=("",11),bg="blue",fg="white")
    u1.place(x=0,y=0,width=120)
    u2 = Label(f5,text="Mobile No.",font=("",11),bg="blue",fg="white")
    u2.place(x=120,y=0,width=120)
    u3 = Label(f5,text="Email ID",font=("",11),bg="blue",fg="white")
    u3.place(x=240,y=0,width=200)
    u4 = Label(f5,text="Salary",font=("",11),bg="blue",fg="white")
    u4.place(x=440,y=0,width=120)
    u3 = Label(f5,text="Last Edit",font=("",11),bg="blue",fg="white")
    u3.place(x=560,y=0,width=120)
    db=sqlite3.connect("employee_list.db")
    cr = db.cursor()
    r = cr.execute("select * from ins")
    x=0
    y=60
    for r1 in r:
        Label(f5,text=r1[0],font=("",11),bg="white",fg="black").place(x=x,y=y,width=120)
        x += 120
        Label(f5,text=r1[1],font=("",11),bg="white",fg="black").place(x=x,y=y,width=120)
        x += 120
        Label(f5,text=r1[2],font=("",11),bg="white",fg="black").place(x=x,y=y,width=200)
        x += 200
        Label(f5,text=r1[3],font=("",11),bg="white",fg="black").place(x=x,y=y,width=120)
        x += 120
        Label(f5,text=r1[4],font=("",11),bg="white",fg="black").place(x=x,y=y,width=120)


        y += 40
        x = 0 
    db.commit()
    db.close()
    

def search(n):
    f6 = Frame(bg="cyan")
    n.add(f6,text="Search")
    s1 = StringVar()
    un1 = Label(f6,text="Employee ID",bg="blue",fg="white")
    un1.place(x=100,y=50,height=24)
    e1 = Entry(f6,font=("",12),textvariable=s1)
    e1.place(x=180,y=50,height=24)
    def search1():
        db=sqlite3.connect("employee_list.db")
        cr = db.cursor()
        r = cr.execute("select * from ins where mobile='"+s1.get()+"'")
        for r1 in r:
            u1 = Label(f6,text="Insert By:",font=("",11),bg="white",fg="black")
            u1.place(x=100,y=100,width=120)
            u2 = Label(f6,text=r1[0],font=("",11),bg="white",fg="black")
            u2.place(x=200,y=100,width=120)
            u3 = Label(f6,text="Mobile No.:",font=("",11),bg="white",fg="black")
            u3.place(x=100,y=150,width=120)
            u4 = Label(f6,text=r1[1],font=("",11),bg="white",fg="black")
            u4.place(x=200,y=150,width=120)
            u5 = Label(f6,text="Email:",font=("",11),bg="white",fg="black")
            u5.place(x=100,y=200,width=120)
            u6 = Label(f6,text=r1[2],font=("",11),bg="white",fg="black")
            u6.place(x=200,y=200,width= 200)
            u7 = Label(f6,text="Salary:",font=("",11),bg="white",fg="black")
            u7.place(x=100,y=250,width=120)
            u8 = Label(f6,text=r1[3],font=("",11),bg="white",fg="black")
            u8.place(x=200,y=250,width=120)
            u9 = Label(f6,text="Last Edit By:",font=("",11),bg="white",fg="black")
            u9.place(x=100,y=300,width=120)
            u10 = Label(f6,text=r1[4],font=("",11),bg="white",fg="black")
            u10.place(x=200,y=300,width=120)
            break
        else:
            messagebox.showinfo('Title','Invalid Information/n No Data Found')
            u1 = Label(f6,text="Insert By:",font=("",11),bg="white",fg="black")
            u1.place(x=100,y=100,width=120)
            u2 = Label(f6,text="",font=("",11),bg="white",fg="black")
            u2.place(x=200,y=100,width=120)
            u3 = Label(f6,text="Mobile No.:",font=("",11),bg="white",fg="black")
            u3.place(x=100,y=150,width=120)
            u4 = Label(f6,text="",font=("",11),bg="white",fg="black")
            u4.place(x=200,y=150,width=120)
            u5 = Label(f6,text="Email:",font=("",11),bg="white",fg="black")
            u5.place(x=100,y=200,width=120)
            u6 = Label(f6,text="",font=("",11),bg="white",fg="black")
            u6.place(x=200,y=200,width=120)
            u7 = Label(f6,text="Salary:",font=("",11),bg="white",fg="black")
            u7.place(x=100,y=250,width=120)
            u8 = Label(f6,text="",font=("",11),bg="white",fg="black")
            u8.place(x=200,y=250,width=120)
            u9 = Label(f6,text="Last Edit By:",font=("",11),bg="white",fg="black")
            u9.place(x=100,y=300,width=120)
            u10 = Label(f6,text="",font=("",11),bg="white",fg="black")
            u10.place(x=200,y=300,width=120)
        db.commit()
        db.close()
    b2 = Button(f6,text="Search",command = search1)
    b2.place(x=380,y=50,height=24,width = 40)
def updatedata(n):
    f7 = Frame(bg="cyan")
    n.add(f7,text="Update")
def logout(n):
    f8 = Frame(bg="cyan")
    n.add(f8,text="Logout")
    b2 = Button(f8,text="Logout",command=main)
    b2.place(x=250,y=250,width=60,height=30)

def main():
    n = ttk.Notebook()
    n.place(x = 0,y = 0,width = 800,height = 800)
    g1 = StringVar()
    g2 = StringVar()
    f1 = Frame(bg = "cyan")
    n.add(f1,text = "Home")
    f2 = Frame(bg = "cyan")
    n.add(f2,text = "Log In")
    un1 = Label(f2,text="Employee ID",bg="blue",fg="white")
    un1.place(x=100,y=100)
    e1 = Entry(f2,font=("",10),textvariable=g1)
    e1.place(x=220,y=100)
    un2 = Label(f2,text="Password",bg="blue",fg="white")
    un2.place(x=100,y=150)
    e2 = Entry(f2,font=("",10),show="*",textvariable=g2)
    e2.place(x=220,y=150)
    def login1():
        db=sqlite3.connect("employee_list.db")
        cr = db.cursor()
        r = cr.execute("select * from register where emp_id='"+g1.get()+"'AND password='"+g2.get()+"'")
        for r1 in r:
            x=r1[1]
            menu(x)
            break
        else:
            messagebox.showinfo('Title',"Invalid Employee ID and Password")
        db.commit()
        db.close()
        g1.set("")
        g2.set("")
    b2 = Button(f2,text="Login",command=login1)
    b2.place(x=250,y=200,width=60,height=30)
    b3 = Button(f2,text="Register",command = register)
    b3.place(x=180,y=200,width=60,height=30)
    

main()



root.mainloop()
