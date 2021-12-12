from tkinter import *
from tkinter import ttk
import tkinter.messagebox as tkMessageBox
import sqlite3
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
w = Tk()
w.geometry('600x600')
w.title("Prathamesh- Sentimental Analysis")
#-----------------------------------------------------------------------
def shift():
    x1,y1,x2,y2 = canvas.bbox("marquee")
    if(x2<0 or y1<0): 
        x1 = canvas.winfo_width()
        y1 = 420
        canvas.coords("marquee",x1,y1)
    else:
        canvas.move("marquee", -2, 0)
    canvas.after(1000//fps,shift)
canvas=Canvas(w)
canvas.pack(fill=BOTH, expand=1)
text_var="CREATED BY @ PRATHAMESH KASHID"
text=canvas.create_text(0,-2000,text=text_var,font=('Times New Roman',20,'bold'),fill='orange',tags=("marquee",),anchor='w')
x1,y1,x2,y2 = canvas.bbox("marquee")
width = x2-x1
height = y2-y1
canvas['width']=width
canvas['height']=height
fps=40  
shift()
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

conn = sqlite3.connect('SIGNUP.db')
c=conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS SIGNUP( NAME TEXT, PASSWORD TEXT)""")
conn.commit()
conn.close()
#-----------------------------------------------------------
def Register():
    Database()
    if USERNAME.get == "" or PASSWORD.get() == "" or FIRSTNAME.get() == "" or LASTNAME.get == "":
        lbl_result2.config(text="Please complete the required field!", fg="orange")
    else:
        cursor.execute("SELECT * FROM `member` WHERE `username` = ?", (USERNAME.get(),))
        if cursor.fetchone() is not None:
            lbl_result2.config(text="Username is already taken", fg="red")
        else:
            cursor.execute("INSERT INTO `member` (username, password, firstname, lastname) VALUES(?, ?, ?, ?)", (str(USERNAME.get()), str(PASSWORD.get()), str(FIRSTNAME.get()), str(LASTNAME.get())))
            conn.commit()
            USERNAME.set("")
            PASSWORD.set("")
            FIRSTNAME.set("")
            LASTNAME.set("")
            lbl_result2.config(text="Successfully Created!", fg="black")
        cursor.close()
        conn.close()
def Login():
    Database()
    if USERNAME.get == "" or PASSWORD.get() == "":
        lbl_result1.config(text="Please complete the required field!", fg="orange")
    else:
        cursor.execute("SELECT * FROM `member` WHERE `username` = ? and `password` = ?", (USERNAME.get(), PASSWORD.get()))
        if cursor.fetchone() is not None:
            lbl_result1.config(text="You Successfully Login", fg="blue")
        else:
            lbl_result1.config(text="Invalid Username or password", fg="red")
	
#-------------------------------------------------------------------------------------------------------------------------------------------------
def sinup():
    s1=e1.get()
    s2=e2.get()
    conn = sqlite3.connect('SIGNUP.db')
    c=conn.cursor()
    if e1.get == "" or e2.get() == "":
        l14=Label(w,text="Empty Input!!!", font=("Helvetica", 22), fg="RED")
        l14.place(x = 20,y = 250)
    else:
        print("s")
        sql='''INSERT INTO SIGNUP (NAME,PASSWORD) VALUES (?,?)'''
        val=(s1,s2)
        c.execute(sql, val)
        conn.commit()
        l12=Label(w,text="Signup Successfull", font=("Helvetica", 20), fg="GREEN" )
        l12.place(x = 20,y = 250)
        conn.close()
        def clear():
            e1.delete(0,END)
            e2.delete(0,END)
        def close():
            w.destroy()
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def login():
    s3=e3.get()
    s4=e4.get()
    conn = sqlite3.connect('SIGNUP.db')
    c=conn.cursor()
    if e3.get == "" or e4.get() == "":
        l14=Label(w,text="Empty Input!!!", font=("Helvetica", 22), fg="RED")
        l14.place(x = 350,y = 250)
    else:
        s=f"SELECT NAME from SIGNUP WHERE NAME='{e3.get()}' AND PASSWORD = '{e4.get()}';"
        c.execute(s)
        if not c.fetchone():
            print("Login Failed")
            l14=Label(w,text="LOGIN FAILED", font=("Helvetica", 22), fg="RED")
            l14.place(x = 300,y = 250)
        else:
            print("Login Successful")
            l15=Label(w,text="LOGIN SUCCESSFUL", font=("Helvetica", 22), fg="GREEN")
            l15.place(x = 300,y = 250)
            import HomePage
            conn.commit()
        
    
#=================================================================================================================================
heading = Label(w, text = "SIGNUP & LOGIN" , font = 'Verdana 20 bold', fg="GREEN")
heading.place(x=150 , y=20)
#----------------------------------------------------------------------------------------------------------------------------------------------------------
l2=Label(w,text="Name :")
l2.place(x=20,y=100)
e1=Entry(w)
e1.place(x=90,y=100)

#----------------------------------------------------------------------------------------------------------------------
l2=Label(w,text="Password :")
l2.place(x=20,y=130)
e2=Entry(w, show='*')
e2.place(x=90,y=130)
#---------------------------------------------------------------------------------------------------------------------
l1=Label(w,text="Name :")
l1.place(x=340,y=100)
e3=Entry(w)
e3.place(x=410,y=100)
#----------------------------------------------------------------------------------------------------------------------
l2=Label(w,text="Password :")
l2.place(x=340,y=130)
e4=Entry(w, show='*')
e4.place(x=410,y=130)
#---------------------------------------------------------------------------------------------------------------
B1=Button(w,text="SIGNUP",font='Helvetica 9 bold',command=sinup)
B1.place(x=90,y=180)
B2 = Button(w, text = "LOGIN", font='Helvetica 9 bold',command=login)
B2.place(x =400,y = 180)
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
w.mainloop()
