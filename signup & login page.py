from tkinter import *
from tkinter import ttk
import sqlite3
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
w = Tk()
w.geometry('600x600')
w.title("login & signup page")
w.configure(background='light green')
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
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
conn = sqlite3.connect('SIGNUP.db')
print("Opened database successfully")
c=conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS SIGNUP( NAME TEXT, PASSWORD TEXT)""")
print("Table Created successfully")
conn.commit()
conn.close()


	
#-------------------------------------------------------------------------------------------------------------------------------------------------
def sinup():
    s1=e1.get()
    s2=e2.get()
    conn = sqlite3.connect('SIGNUP.db')
    print("Opened database successfully")
    c=conn.cursor()
    sql='''INSERT INTO SIGNUP (NAME,PASSWORD) VALUES (?,?)'''
    val=(s1,s2)
    c.execute(sql, val)
    conn.commit()
    l12=Label(w,text="Signup Successfull", font=("Helvetica", 20), fg="GREEN" )
    l12.place(x = 20,y = 250)
    print("Records Inserted successfully with values ",(s1,s2))
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
    print("Opened database successfully")
    c=conn.cursor()
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
        import fe
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
