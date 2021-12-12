from tkinter import *
from tkinter import ttk
import sqlite3
w = Tk()
w.title("Prathamesh-Registration form")
w.geometry("650x900")
#========================================================================================================================
conn = sqlite3.connect('PK.db')
print("Opened database successfully")
c=conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS PK( NAME TEXT, ADDRESS TEXT, GENDER TEXT,FOOD TEXT,LANGUAGE TEXT,MOVIE TEXT )""")
print("Table Created successfully")
conn.commit()
conn.close()
#==========================================================================================================================
def insert():
    print("Loading>>>>>>>>>>")
#-------------------------------------------------------------------------------------
    s1=e1.get()
    l8=Label(w,text="Your Name is :"+ s1)
    l8.place(x=60,y=350)
#-------------------------------------------------------------------------------------

    s2=e2.get()
    l9=Label(w,text="Your Address is :"+ s2)
    l9.place(x=60,y=380)
#--------------------------------------------------------------------------------------
    s3=v.get()
    if s3==1:
        l10=Label(w,text="Your gender is male")
        l10.place(x=60,y=410)
    elif s3==2:
        l11=Label(w,text="Your gender is female")
        l11.place(x=60,y=410)
    else:
        l12=Label(w,text="plz select ur gender!!!!")
        l12.place(x=60,y=410)
#----------------------------------------------------------------------------------------
    s4=v1.get()
    s5=v2.get()
    s6=v3.get()
    if s4==1 and s5==1 and s6==1 :
        l15=Label(w,text="Your favourite game is cricket, tennis & football")
        l15.place(x=60,y=440)
    elif s4==1 and s5==1 :
        l15=Label(w,text="Your favourite game is cricket & tennis")
        l15.place(x=60,y=440)
    elif s5==1 and s6==1 :
        l15=Label(w,text="Your favourite game is tennis & football")
        l15.place(x=60,y=440)
    elif s4==1:
        l13=Label(w,text="Your favourite game is cricket")
        l13.place(x=60,y=440)
    elif s5==1:
        l14=Label(w,text="Your favourite game is football")
        l14.place(x=60,y=440)
    elif s6==1:
        l15=Label(w,text="Your favourite game is tennis")
        l15.place(x=60,y=440)
    else:
        l16=Label(w,text="plz select ur fav game!!!")
        l16.place(x=60,y=440)
#-----------------------------------------------------------------------------------------------             
    s7=sb.get()
    if lb.get(0):
        l17=Label(w,text='your fav food is:'+ s7)
        l17.place(x=60,y=470)
    elif lb.get(1):
        l18=Label(w,text='your fav food is:'+ s7)
        l18.place(x=60,y=470)
    elif lb.get(2):
        l19=Label(w,text='your fav food is:'+ s7)
        l19.place(x=60,y=470)
    else:
        l20=Label(w,text='your fav food is:'+s7)
        l20.place(x=60,y=470)
#--------------------------------------------------------------------------------------------
    s8=cb.get()
    if lb.get(0):
        l17=Label(w,text='your fav movie is:'+ s8)
        l17.place(x=60,y=500)
    elif lb.get(1):
        l18=Label(w,text='your fav movie is:'+ s8)
        l18.place(x=60,y=500)
    elif lb.get(2):
        l19=Label(w,text='your fav movie is:'+ s8)
        l19.place(x=60,y=500)
    else:
        l20=Label(w,text='your fav movie is:'+s8)
        l20.place(x=60,y=500)
#--------------------------------------------------------------------------------          
    s9=lb.get(ACTIVE)
    if lb.get(ACTIVE):
        l21=Label(w,text='your fav lang is:'+ s9)
        l21.place(x=60,y=530)
#----------------------------------------------------------------------------------------
    conn = sqlite3.connect('PK.db')
    print("Opened database successfully")
    c=conn.cursor()
    if s3==1:
        s3='Male'
    elif s3==2:
        s3='Female'
    sql='''INSERT INTO PK (NAME,ADDRESS,GENDER,FOOD,LANGUAGE,MOVIE) VALUES (?,?,?,?,?,?)'''
    val=(s1,s2,s3,s4,s7, s8)
    c.execute(sql, val)
    conn.commit()
    l12=Label(w,text="Record Inserted Successfully!!!!!",fg="red")
    l12.place(x = 60,y = 550)
    print("Records Inserted successfully with values ",(s1,s2,s3,s4,s7,s8))
    conn.close()
#=============================================================================================================================
def view():
          conn = sqlite3.connect('PK.db') 
          c=conn.cursor()
          c.execute("""SELECT * FROM PK""")
          s=c.fetchall()
          s1=str(s)
          print("Records in Database are",s)
          l6=Label(w, text=("Records in Database are-"))
          l6.place(x=400,y=350)
          T = Text(w, height=10, width=80)
          T.place(x=400,y=380)
          T.insert(INSERT,s1)
          conn.commit()
          conn.close()
#=================================================================================================================================
def delete():
          conn = sqlite3.connect('PK.db') 
          c=conn.cursor()
          n1=e6.get()
          print(n1)
          sql = 'DELETE FROM PK WHERE NAME=?'
          c.execute(sql, (n1,))
          print("Records Deleted Successfully with Name =", n1)
          l8=Label(w,text="Record deleted successfully!!!!!!!!!!",fg="red")
          l8.place(x=150,y=650)
          conn.commit()
#-------------------------------------------------------------------------------------------------------------------------
def home():
    import HomePage
#-----------------------------------------------------------------------------------------------------------------------
l10=Label(w,text="Registration Form", font=("Helvetica", 35), fg="green")
l10.place(x = 20,y = 20)
#------------------------------------------------------------------------------------------------------------------------
l1=Label(w,text="Enter your Name")
l1.place(x=20,y=90)
e1=Entry(w)
e1.place(x=130,y=90)
#----------------------------------------------------------------------------------------------------------------------
l2=Label(w,text="Enter your Address")
l2.place(x=20,y=120)
e2=Entry(w)
e2.place(x=130,y=120)
#------------------------------------------------------------------------------------------------------------------------
l3=Label(w,text="Select your gender")
l3.place(x=20,y=150)
v=IntVar()
r1=Radiobutton(w,text="Male",variable=v, value =1)
r2=Radiobutton(w,text="Female",variable=v, value =2)
r1.place(x=130,y=150)
r2.place(x=190,y=150)
#------------------------------------------------------------------------------------------------------------------------
l4=Label(w,text="Select your favourite sport")
l4.place(x=20,y=180)
v1=IntVar()
v2=IntVar()
v3=IntVar()
c1=Checkbutton(w,text="Cricket",variable=v1)
c2=Checkbutton(w,text="Football",variable=v2)
c3=Checkbutton(w,text="Tennis",variable=v3)
c1.place(x=135,y=180)
c2.place(x=200,y=180)
c3.place(x=280,y=180)
#---------------------------------------------------------------------------------------------------------------
l6=Label(w,text="Select your Favourite Food")
l6.place(x=20,y=210)
sb=Spinbox(w,value=['Chinese','Indian','Continental','Italian'])
sb.place(x=200,y=210)
#------------------------------------------------------------------------------------------------------------------
l5=Label(w,text="Select your Favourite Language")
l5.place(x=20,y=240)
lb=Listbox(w,height=2,width=20)
lb.insert(0,'Python')
lb.insert(1,'Java')
lb.insert(2,'C++')
lb.insert(3,'C')
lb.place(x=200,y=240)
#----------------------------------------------------------------------------------------------------------------
l7=Label(w,text="Select your Favourite Movie")
l7.place(x=20,y=290)
cb=ttk.Combobox(w,values=['Avengers','Harry Potter','Home Alone','3 Idiots'],height=10,width=20)
cb.place(x=200,y=290)
#--------------------------------------------------------------------------------------------------
l8=Label(w,text="SELECT DATA TO DELETE:")
l8.place(x=20,y=580)
e6=Entry(w)
e6.place(x=170,y=580)
#---------------------------------------------------------------------------------------------------------------
B1=Button(w,text="INSERT DATA IN DATABASE",font='Helvetica 9 bold',command=insert)
B1.place(x=60,y=320)

B2 = Button(w, text = "VIEW DATABASE RECORD:", font='Helvetica 9 bold', command=view)
B2.place(x =400,y = 320)

B3 = Button(w, text = "DELETE RECORD FROM DATABASE", font='Helvetica 9 bold', command=delete)
B3.place(x =60,y = 610)

B4 = Button(w, text = "Back to Home Page", font='Helvetica 9 bold', command=home)
B4.place(x =400,y = 610)


w.mainloop()
