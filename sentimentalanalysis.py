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
#----------------------------------------------------------------------------------------------------
def Predict():
    import numpy as np
    import pandas as pd
    import warnings                                  
    warnings.filterwarnings('ignore')
    from textblob import TextBlob
    review=e2.get()
    b=cb.get()
    if cb.get() == "":
        l15=Label(w,text='plz select movie', font=("Helvetica", 22), fg="RED")
        l15.place(x = 220,y = 270)
    if e2.get() == "":
        l15=Label(w,text='plz give review', font=("Helvetica", 22), fg="RED")
        l15.place(x = 220,y = 320)
    else:
        l15=Label(w,text=b, font=("Helvetica", 22), fg="RED")
        l15.place(x = 220,y = 270)
        print(b)
        blob1=TextBlob(review)
        a=blob1.polarity
        print(a)
        if a==0:
            print('neutral')
            l15=Label(w,text='Neutral review', font=("Helvetica", 22), fg="RED")
            l15.place(x = 190,y = 320)
        elif a>0:
            l15=Label(w,text='Positive review', font=("Helvetica", 22), fg="RED")
            l15.place(x = 190,y = 320)
        else:
            l15=Label(w,text='Negative review', font=("Helvetica", 22), fg="RED")
            l15.place(x = 190,y = 320)   
     
    

#=================================================================================================================================
heading = Label(w, text = "Movie Review-Sentimental Analysis" , font = 'Verdana 20 bold', fg="GREEN")
heading.place(x=40 , y=20)
#----------------------------------------------------------------------------------------------------------------------
l1=Label(w,text="Movie:")
l1.place(x=190,y=100)
cb=ttk.Combobox(w,values=['Avengers','Harry Potter','3 Idiots'],height=10,width=20)
cb.place(x=270,y=100)
#----------------------------------------------------------------------------------------------------------------------
l2=Label(w,text="Review:")
l2.place(x=190,y=160)
e2=Entry(w)
e2.place(x=270,y=160,width=140)
#---------------------------------------------------------------------------------------------------------------
B1=Button(w,text="Submit",font='Helvetica 9 bold',command=Predict)
B1.place(x=270,y=210)
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
w.mainloop()
