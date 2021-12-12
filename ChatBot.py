from tkinter import *
root = Tk()
def send():
    send = "You:"+ e.get()
    text.insert(END,"\n" + send)
    if(e.get()=='hi'):
        text.insert(END, "\n" + "Bot: hello")
    elif(e.get()=='hello'):
        text.insert(END, "\n" + "Bot: hi")
    elif(e.get()=='whats ur name?'):
        text.insert(END, "\n" + "Bot: my name is PK")
    elif(e.get()=='PK who created u?'):
        text.insert(END, "\n" + "Bot: My master Prathamesh created me")
    elif (e.get() == 'how are u?'):
        text.insert(END, "\n" + "Bot: I'm fine and you?")
    elif (e.get() == "I'm fine too"):
        text.insert(END, "\n" + "Bot: nice to hear that")
    elif(e.get()=='bye'):
        text.insert(END, "\n" + "Bot:I'm glad to see u again")
    else:
        text.insert(END, "\n" + "Bot: Sorry I didnt get it.")
    import numpy as np
    import pandas as pd
    import warnings
    warnings.filterwarnings('ignore')
    df = pd.read_csv("https://raw.githubusercontent.com/Prathamesh148/ML/main/Sales.csv")
text = Text(root,bg='light blue')
text.grid(row=0,column=0,columnspan=2)
e = Entry(root,width=80)
send = Button(root,text='Send',bg='blue',width=20,command=send).grid(row=1,column=1)
e.grid(row=1,column=0)
root.title('PERSONAL CHATBOT by Prathamesh')
root.mainloop()
