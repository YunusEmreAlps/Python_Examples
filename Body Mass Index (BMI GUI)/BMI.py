# Body Mass Index (BMI)
    
import tkinter # GUI : Graphical User Interface

def cal():
    hght = float(theEntry1.get()) # height
    wght = float(theEntry2.get()) # weight
    
    if hght < 0:
        hght *= -1
    if wght < 0:
        wght *= -1
    
    if hght > 3.0:
        hght = hght/100
    result = wght / (hght**2) # numeric calculation
    
    if result <= 18.5:
        result2 = "Underweight"
        stcolor = "red"
    elif result > 18.5 and result <= 25:
        result2 = "Normal weight"
        stcolor = "green"
    elif result > 25 and result < 30:
        result2 = "Overweight"
        stcolor = "orange"
    else:
        result2 = "Obesity"
        stcolor = "red"
    
    theLabel3 = tkinter.Label(root,font="arial 14",fg=f"{stcolor}",text=f"{result2}")
    theLabel3.place(x=50,y=200,width=320,height=30)
    theEntry3 = tkinter.Entry(root,font="arial 14",bd=2)
    theEntry3.insert(0,f"{result}")
    theEntry3.place(x=170,y=250,width=200,height=30)
    
    

root = tkinter.Tk() # Basic window
root.title("Body Mass Index (BMI)") 
root.configure(background = "white")
root.minsize(width=500,height=330)
root.resizable(width=False,height=False)

theLabel1 = tkinter.Label(root,font="arial 14",text="Height")
theLabel1.place(x=50,y=50,width=100,height=30)

theEntry1 = tkinter.Entry(root,font="arial 14",bd=2) # bd : border
theEntry1.place(x=170,y=50,width=200,height=30)

theLabel2 = tkinter.Label(root,font="arial 14",text="Weight")
theLabel2.place(x=50,y=100,width=100,height=30)

theEntry2 = tkinter.Entry(root,font="arial 14",bd=2) # bd : border
theEntry2.place(x=170,y=100,width=200,height=30)

theButton1 = tkinter.Button(root,font="arial 14",text="Calculate",command=cal)
theButton1.place(x=170,y=150,width=200,height=30)

root.mainloop()
    

