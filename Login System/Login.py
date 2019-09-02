# Login System

# File 
person = {} #<class 'list'>
with open("Login.txt","r+") as file:
    for line in file:
        splitline = line.split()
        person[splitline[0]] = ','.join(splitline[1:]) # !!


import tkinter # GUI : Graphical User Interface
import tkinter.messagebox

def Sign_up(): # Sign up (Kaydol)
    
    nm = theEntry1.get() # Name
    nm = nm.title() # first letter is capital
    ps = theEntry2.get() # Password
    A = ''
    if nm.count(' ') > 0: # This code diversify -> Hello_world 
        for i in nm:
            if i == ' ':
                i = '_'
            A += i
        nm = A
    A = ''
    if ps.count(' ') > 0: # This code diversify -> Hello_world 
        for i in ps:
            if i == ' ':
                i = '_'
            A += i
        ps = A
  
    
    if nm in person:  
        tkinter.messagebox.showerror("Error","Another user have this username")
    
    elif  person.keys() != nm:   
        person[nm] = ps  
        with open("Login.txt","a") as file:
            file.writelines(f" {nm} ")
        
        with open("Login.txt","a") as file:
            file.writelines(f" {ps} \n")
    

def Sign_in(): # Sign in (Oturum aç)
    
    nm = theEntry1.get() # Name
    nm = nm.title() # first letter is capital
    ps = theEntry2.get() # Password
    A = ''
    if nm.count(' ') > 0: # This code diversify -> Hello_world 
        for i in nm:
            if i == ' ':
                i = '_'
            A += i
        nm = A
    if ps.count(' ') > 0: # This code diversify -> Hello_world 
        for i in ps:
            if i == ' ':
                i = '_'
            A += i
        ps = A
   
    if nm in person.keys():
        if person[nm] == ps:
            tkinter.messagebox.showinfo("Log in message","Access is success")
        else:
            tkinter.messagebox.showerror("Log in message","Access denied")
    else:
        tkinter.messagebox.showerror("Log in message","Access denied")
    


root = tkinter.Tk() # Basic window

root.configure(background="white")
root.iconbitmap("C:/Users/Dell/Desktop/Basic_PythonExamples/Login System/person.ico")
root.title("Login System")
root.minsize(width=500,height=300)
root.resizable(width=False,height=False)

# Username
User = tkinter.Label(root,font="arial 14",fg="red",text="Username : ",bg="white")
User.place(x=100,y=20,width=100,height=30)
# x and y coordinates

theEntry1 = tkinter.Entry(root,font="arial 14",fg="black",bd=2)
theEntry1.place(x=220,y=20,width=200,height=30)

# Password
Pass = tkinter.Label(root,font="arial 14",fg="red",text="Password : ",bg="white")
Pass.place(x=100,y=60,width=100,height=30)
# x and y coordinates

theEntry2 = tkinter.Entry(root,font="arial 14",fg="black",bd=2,show="*")
theEntry2.place(x=220,y=60,width=200,height=30)

# Sign in Button
Log = tkinter.Button(root,font="arial 14",fg="white",text="Sign in",bd=0,bg="#64c4ed",command=Sign_in)
Log.place(x=220,y=100,width=200,height=30)

# Sign up Button
Log = tkinter.Button(root,font="arial 14",fg="white",text="Sign up",bd=0,bg="#64c4ed",command=Sign_up)
Log.place(x=220,y=140,width=200,height=30)

root.mainloop()