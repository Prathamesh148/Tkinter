from tkinter import*
w=Tk()
c=Canvas(w,height=1000,width=1000)
c.create_line(20,40,180,40,fill='blue',activefill='red')
c.create_rectangle(260,140,380,250,fill='purple', activefill='green')
c.create_arc(120,220,180,340, start=0, extent=130, fill='orange')
c.create_oval(20,120,80,240, fill='Indigo')
c.create_polygon(650,100,150,200,250,300,350,400, fill='yellow')
c.create_text(130,20,text='line, rectangle, arc, oval drawing by tkinter- ', fill='black')
c.pack()
w.mainloop()