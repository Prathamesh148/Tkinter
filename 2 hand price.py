from tkinter import *
from tkinter import ttk
import sqlite3
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
w = Tk()
w.geometry('600x600')
w.title("Home Page")
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
#--------------------------------------------------------------------------------------------------------------------------------------------
conn = sqlite3.connect('CAR.db')
print("Opened database successfully")
c=conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS CAR( MILEAGE REAL, LUXURY REAL, HIGHWAY_MPG REAL,YEAR_OLD REAL,CITY_MPG REAL)""")
print("Table Created successfully")
conn.commit()
conn.close()	
#----------------------------------------------------------------------------------------------------
def Predict():
    s1=e1.get()
    s2=e2.get()
    s3=e3.get()
    s4=e4.get()
    s5=e5.get()
    conn = sqlite3.connect('CAR.db')
    print("Opened database successfully")
    c=conn.cursor()
    sql='''INSERT INTO CAR (MILEAGE, LUXURY, HIGHWAY_MPG,YEAR_OLD,CITY_MPG ) VALUES (?,?,?,?,?)'''
    val=(s1,s2,s3,s4,s5)
    c.execute(sql, val)
    conn.commit()
    l12=Label(w,text="Price for 2 hand car:", font=("Helvetica", 20), fg="RED" )
    l12.place(x = 180,y = 220)
    print("Records Inserted successfully with values ",(s1,s2,s3,s4,s5))
    conn.close()
    def clear():
        e1.delete(0,END)
        e2.delete(0,END)
    def close():
        w.destroy(s1)
    a=int(s1)
    print(a)
    b=int(s2)
    print(b)
    c=int(s3)
    print(c)
    d=int(s4)
    print(d)
    e=int(s5)
    print(e)
    price=float(11.3940+(-5.4996*(a))+(0.0133*(b))+(-0.0489*(c))+(-0.0569*(d))+(0.3272*(e)))
    l15=Label(w,text=price, font=("Helvetica", 22), fg="RED")
    l15.place(x = 230,y = 260)
    print("Done")
    
    
#=================================================================================================================================
heading = Label(w, text = "Result prediction Model" , font = 'Verdana 20 bold', fg="GREEN")
heading.place(x=120 , y=20)
#----------------------------------------------------------------------------------------------------------------------------------------------------------
l1=Label(w,text="Mileage:")
l1.place(x=20,y=100)
e1=Entry(w)
e1.place(x=90,y=100)

#----------------------------------------------------------------------------------------------------------------------
l2=Label(w,text="Luxury:")
l2.place(x=20,y=130)
e2=Entry(w)
e2.place(x=90,y=130)
#---------------------------------------------------------------------------------------------------------------------
l3=Label(w,text="Highway_mpg :")
l3.place(x=320,y=100)
e3=Entry(w)
e3.place(x=410,y=100)
#----------------------------------------------------------------------------------------------------------------------
l4=Label(w,text="Year_old:")
l4.place(x=320,y=130)
e4=Entry(w)
e4.place(x=410,y=130)
#----------------------------------------------------------------------------------------------------------------------
l5=Label(w,text="City_mpg:")
l5.place(x=20,y=160)
e5=Entry(w)
e5.place(x=90,y=160)
#---------------------------------------------------------------------------------------------------------------
B1=Button(w,text="Predict Price",font='Helvetica 9 bold',command=Predict)
B1.place(x=250,y=180)
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
w.mainloop()
