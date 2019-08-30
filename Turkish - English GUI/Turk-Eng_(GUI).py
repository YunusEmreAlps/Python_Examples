# English - Turkish Dictionary (GUI)

words = {} # <class 'dict'>

# Read Function
with open("Turk-Eng2.txt","r+") as file:
    for line in file:
        splitline = line.split()
        words[splitline[0]] = ",".join(splitline[1:]) # !!!
    
        
# Search Word
def Search(first,last):

    word = first.get()
    word = word.title() # first letter is capital
    
    if word in words.keys(): # English Word 
        last.insert(0,f" {words[word]} ")
    else:
        last.insert(0," This word is not found ")
    
# Add Word
def Add(first,last):
    A = " "
    word = first.get()
    word = word.title() # first letter is capital   
    syn = False
    #For Example your word  is  Hello World
    if word.count(' ') > 0: # This code diversify -> Hello_world 
        for i in word:
            if i == ' ':
                i = '_'
            A += i
        word = A
  
    for i in word:
       if syn != True: 
           if((i =='ü' or i=='Ü')or(i =='ğ' or i =='Ğ')or(i == 'ö' or i=='Ö')
           or (i =='ş' or i=='Ş')or(i == 'ç' or i=='Ç')or(i == 'ı')):
               print("Syntax Error")
               syn = True
    
    if syn == True:
        last.insert(0," Syntax Error ")
    else:
         A = " "
         mean = last.get()
         mean = mean.lower() # all letter is lower
         if mean.count(" ") > 0:
             for i in mean:
                 if i == " ":
                     i = '_'
                 A += i
             mean = A
         A = " "
         if mean.count(",") > 0: # This code diversify -> Hello_world 
             for i in range(len(mean)):
                 cind = mean.index(",") 
                 if (i == cind):
                     A += '' 
                     
                 if ((i != (cind-1) and mean[i] != '_')or(i != (cind+1) and mean[i] != '_')):
                    A += mean[i]    
             mean = A
             
         if word in words:
             last.insert(0," You have this word ")
         else:
             # Append Word
             with open("Turk-Eng2.txt","a") as file:
                 file.writelines(f" {word} ")
                 
             words[word] = mean
                 
             # Append Word
             with open("Turk-Eng2.txt","a") as file:
                 file.writelines(f" {mean} \n") 
         
# Delete Word
def Delt(first,last):
    word = first.get()
    word = word.title() # first letter is capital
    
    if word in words.keys():
        last.insert(0,f" {words[word]} ")
        
        # Append Word
        with open("Turk-Eng2.txt","r") as file:
             lines = file.readlines()
             
        # Append Word
        with open("Turk-Eng2.txt","w") as file:
            for line in lines:
                splitline = line.split()
                if word != splitline[0]:
                    file.write(line)
        
        words.pop(word)
    else:
        last.insert(0," This word is not found ")

   
# Graphical Part
        
from tkinter import * # GUI : Graphical User Interface
import tkinter 

def S_window():
        S_wind = tkinter.Tk() # Basic window
        S_wind.title("Search")
        S_wind.resizable(width=False,height=False) # window size
        
        theLabel1 = tkinter.Label(S_wind,text="Word :",font="arial",bg="white",fg="red")
        
        theLabel2 = tkinter.Label(S_wind,text="Mean :",font="arial",bg="white",fg="red")
        
        theLabel1.grid(row=0)
        theLabel2.grid(row=1)
        
        theEntry1 = tkinter.Entry(S_wind,width=30)
        theEntry2 = tkinter.Entry(S_wind,width=30)
        
        theEntry1.grid(row=0,column=1)
        theEntry2.grid(row=1,column=1)
        
        theButton = tkinter.Button(S_wind,width=30,text="Search",command=lambda:Search(theEntry1,theEntry2))
        theButton.grid(row=2,column=1)
        
def A_window():
        A_wind = tkinter.Tk() # Basic window
        A_wind.title("Add")
        A_wind.resizable(width=False,height=False) # window size
        
        theLabel1 = tkinter.Label(A_wind,text="Word :",font="arial",bg="white",fg="red")
        
        theLabel2 = tkinter.Label(A_wind,text="Mean :",font="arial",bg="white",fg="red")
        
        theLabel1.grid(row=0)
        theLabel2.grid(row=1)
        
        theEntry1 = tkinter.Entry(A_wind,width=30)
        theEntry2 = tkinter.Entry(A_wind,width=30)
        
        theEntry1.grid(row=0,column=1)
        theEntry2.grid(row=1,column=1)
        
        theButton = tkinter.Button(A_wind,width=30,text="Add",command=lambda:Add(theEntry1,theEntry2))
        theButton.grid(row=2,column=1)

def D_window():
        D_wind = tkinter.Tk() # Basic window
        D_wind.title("Delete")
        D_wind.resizable(width=False,height=False)
        
        theLabel1 = tkinter.Label(D_wind,text="Word :",font="arial",bg="white",fg="red")
        
        theLabel2 = tkinter.Label(D_wind,text="Mean :",font="arial",bg="white",fg="red")
        
        theLabel1.grid(row=0)
        theLabel2.grid(row=1)
        
        theEntry1 = tkinter.Entry(D_wind,width=30)
        theEntry2 = tkinter.Entry(D_wind,width=30)
        
        theEntry1.grid(row=0,column=1)
        theEntry2.grid(row=1,column=1)
        
        theButton = tkinter.Button(D_wind,width=30,text="Delete",command=lambda:Delt(theEntry1,theEntry2))
        theButton.grid(row=2,column=1)

def Sh_window():
        Sh_wind = tkinter.Tk() # Basic window
        Sh_wind.title("Show")
        theList = tkinter.Listbox(Sh_wind,width=60)
        Sh_wind.resizable(width=False,height=False)
        theList.pack()
     
        a = 0
        for i in words:
            theList.insert(a,f" {i} : {words[i]}")
            a += 1

        #theButton = tkinter.Button(Sh_wind,width=30,text="Show",command=lambda:Show(theList))
        #theButton.grid(row=2,column=1)


# Main Function
root = tkinter.Tk() # Basic window

root.resizable(width=False,height=False) # window size

theButton1 = tkinter.Button(root,width=30,height=5,text="Search",
             bg="white",fg="red",activebackground="black",activeforeground="white",command=S_window)
theButton2 = tkinter.Button(root,width=30,height=5,text="Add",
             bg="white",fg="red",activebackground="black",activeforeground="white",command=A_window)
theButton3 = tkinter.Button(root,width=30,height=5,text="Delete",
             bg="white",fg="red",activebackground="black",activeforeground="white",command=D_window)
theButton4 = tkinter.Button(root,width=30,height=5,text="Show",
             bg="white",fg="red",activebackground="black",activeforeground="white",command=Sh_window)

theButton1.grid(row=0)
theButton2.grid(row=1)
theButton3.grid(row=2)
theButton4.grid(row=3)

root.mainloop()














        
        