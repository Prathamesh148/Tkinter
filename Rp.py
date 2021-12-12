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
    Name=['Ajinkya','Aditya','Devang','Prathamesh','siddesh']
    Internal=[20,25,30,35,40]
    Pratical=[10,20,30,40,50]
    Written=[30,35,40,45,55]
    Result=['Fail','Just pass','Pass','Pass','Topper']
    d={"Name":Name,"Internal":Internal,"Pratical":Pratical,"Written":Written,"Result":Result}
    data=pd.DataFrame(d)
    print(data)
    exam= ['Internal', 'Pratical', 'Written' ]                              
    Input= data[exam]                                              
    Result = ['Result']                                                                                              
    Output= data['Result']                                         
    numeric_feature_names = ['Internal', 'Pratical', 'Written']
    print(numeric_feature_names)
    print(Input[numeric_feature_names])
    Internal_Range=40-20
    print("Internal_Range:",Internal_Range)
    Practical_Range=50-10
    print("Practical_Range:",Practical_Range)
    Written_Range=55-30
    print("Written_Range:",Written_Range)
    print(Input.describe())
    from sklearn.preprocessing import StandardScaler
    ss = StandardScaler()
    ss.fit(Input[numeric_feature_names])
    Input[numeric_feature_names]= ss.transform(Input[numeric_feature_names]) 
    print(Input[numeric_feature_names])
    print(Output)
    print(set(Input))
    from sklearn.linear_model import LogisticRegression
    lr = LogisticRegression()
    model = lr.fit(Input, np.array(Output))
    print(model)
    pred_Output = model.predict(Input)
    actual_Output = np.array(Output)
    from sklearn.metrics import accuracy_score, classification_report
    print(accuracy_score(actual_Output,pred_Output ))
    print(classification_report(actual_Output,pred_Output ))
    import joblib
    import os
    if not os.path.exists("Model"):
        os.mkdir("Model")
    if not os.path.exists("Scaler"):
        os.mkdir("Scaler")
    joblib.dump(model, r'Model/model.pickle')
    joblib.dump(ss, r'Scaler/scaler.pickle')
    import joblib
    model= joblib.load(r'Model/model.pickle')
    scaler= joblib.load(r'Scaler/scaler.pickle')
    print(model)
    print(scaler)
    new_data = pd.DataFrame([
    {"Name":e1.get(),"Internal":e2.get(),"Pratical":e3.get(),"Written":e4.get()}
    ])
    print(new_data)
    prediction_features = new_data[exam]
    print(prediction_features)
    prediction_features[exam] = scaler.transform(prediction_features[exam])
    print(prediction_features)
    print(len(prediction_features))
    predictions = model.predict(prediction_features)
    print(predictions)
    new_data['Result'] = predictions
    print(new_data['Result'])
    l15=Label(w,text=predictions, font=("Helvetica", 22), fg="RED")
    l15.place(x = 230,y = 260)   
#=================================================================================================================================
heading = Label(w, text = "Result prediction Model" , font = 'Verdana 20 bold', fg="GREEN")
heading.place(x=120 , y=20)
#----------------------------------------------------------------------------------------------------------------------------------------------------------
l1=Label(w,text="Name:")
l1.place(x=200,y=100)
e1=Entry(w)
e1.place(x=260,y=100)

#----------------------------------------------------------------------------------------------------------------------
l2=Label(w,text="Internal:")
l2.place(x=200,y=160)
e2=Entry(w)
e2.place(x=260,y=160)
#---------------------------------------------------------------------------------------------------------------------
l3=Label(w,text="Practical:")
l3.place(x=200,y=130)
e3=Entry(w)
e3.place(x=260,y=130)
#----------------------------------------------------------------------------------------------------------------------
l4=Label(w,text="Written:")
l4.place(x=200,y=190)
e4=Entry(w)
e4.place(x=260,y=190)
#---------------------------------------------------------------------------------------------------------------
B1=Button(w,text="Predict Result",font='Helvetica 9 bold',command=Predict)
B1.place(x=250,y=220)
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
w.mainloop()
