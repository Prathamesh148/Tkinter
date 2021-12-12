from tkinter import *
from tkinter import ttk
w = Tk()
w.geometry('600x600')
w.title("Prathamesh- Home Page")
w.configure(background='light green')
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
def Registration():
    import Registration
def fromtoexcel():
    import fromtoexcel
def billingsystem():
    import foodbillingsystem
def chatbot():
    import ChatBot
def result():
    import resultprediction
def sentimental():
    import sentimentalanalysis 
    
heading = Label(w, text = "My Projects" , font = 'Verdana 20 bold', fg="GREEN")
heading.place(x=200 , y=20)
B1=Button(w,text="Registration Form",font='Helvetica 9 bold',command=Registration)
B1.place(x=355,y=100)
B2 = Button(w, text = "From To Excel", font='Helvetica 9 bold',command=fromtoexcel)
B2.place(x =255,y = 100)
B3=Button(w,text="Billing System",font='Helvetica 9 bold',command=billingsystem)
B3.place(x=90,y=100)
B4 = Button(w, text = "chatbot", font='Helvetica 9 bold',command=chatbot)
B4.place(x =190,y = 100)
B3=Button(w,text="Result pretiction",font='Helvetica 9 bold',command=result)
B3.place(x=90,y=150)
B4 = Button(w, text = "Sentimental Analysis", font='Helvetica 9 bold',command=sentimental)
B4.place(x =200,y = 150)
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
w.mainloop()
