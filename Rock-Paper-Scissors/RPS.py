# Rock - Paper - Scissors
    
import tkinter # GUI : Graphical User Interface
import random 

# computer choice
game = ("Rock","Paper","Scissors") # <class 'tuple'>

# score variables 
score_you = 0
score_cmp = 0

def win(player1,player2):
   
    # define score variables
    global score_you
    global score_cmp
    
    # Write your and computer choice
    thelabel3 = tkinter.Label(root,font="arial 14",text=f"{player1}")
    thelabel4 = tkinter.Label(root,font="arial 14",text=f"{player2}")
    thelabel3.place(x=170,y=100,width=200,height=30)
    thelabel4.place(x=170,y=150,width=200,height=30)
    
    # Who is Winner this game ? 
    
    # You
    if((player1 == "Rock" and player2 == "Scissors")or(player1 == "Paper" and player2 == "Rock")
    or(player1 == "Scissors" and player2 == "Paper")):
          thelabel5 = tkinter.Label(root,font="arial 14",text="You Wins")
          thelabel5.place(x=50,y=250,width=300,height=30)
              
          score_you += 1 # You Wins 
          thelabel6 = tkinter.Label(root,font="arial 14",text=f"You:{score_you}")
          thelabel6.place(x=50,y=300,width=300,height=30)
    # Tie 
    elif player1 == player2:
        theLabel5 = tkinter.Label(root,font="arial 14",text="Tie")
        theLabel5.place(x=50,y=250,width=300,height=30)
    # Computer
    else:
        thelabel5 = tkinter.Label(root,font="arial 14",text="Computer Wins")
        thelabel5.place(x=50,y=250,width=300,height=30)
        
        score_cmp += 1 # Computer Wins
        
        theLabel7 = tkinter.Label(root,font="arial 14",text=f"Computer:{score_cmp}")
        theLabel7.place(x=50,y=350,width=300,height=30)

# --------- 

def res1(): # thebutton1 Listener (Rock)
    you = "Rock"
    computer = random.choice(game) # computer = game[random.randint(0,2)] 
    win(you,computer)

def res2(): # thebutton2 Listener (Paper)
    you = "Paper"
    computer = random.choice(game) # computer = game[random.randint(0,2)] 
    win(you,computer)
   
def res3(): # thebutton3 Listener (Scissors)
    you = "Scissors"
    computer = random.choice(game) # computer = game[random.randint(0,2)] 
    win(you,computer)

# --------- 
        
root = tkinter.Tk() # window
root.title("Rock-Paper-Scissors") 
root.configure(background="white")
root.minsize(width=500,height=500) # size
root.resizable(width=False,height=False)


thebutton1 = tkinter.Button(root,bg="white",font="arial 14",text="Rock",
                            activebackground="black",activeforeground="white",
                            command=res1)
thebutton2 = tkinter.Button(root,bg="white",font="arial 14",text="Paper",
                            activebackground="black",activeforeground="white",
                            command=res2)
thebutton3 = tkinter.Button(root,bg="white",font="arial 14",text="Scissors",
                            activebackground="black",activeforeground="white",
                            command=res3)

thebutton1.place(x=50,y=50,width=100,height=30)
thebutton2.place(x=170,y=50,width=100,height=30)
thebutton3.place(x=290,y=50,width=100,height=30)

thelabel1 = tkinter.Label(root,bg="white",font="arial 14",text="You : ")
thelabel2 = tkinter.Label(root,bg="white",font="arial 14",text="Computer : ")

thelabel1.place(x=50,y=100,width=100,height=30)
thelabel2.place(x=50,y=150,width=100,height=30)

root.mainloop()