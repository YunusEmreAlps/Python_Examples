# Turtle Race

import turtle # Graphical package
import random

turtle.hideturtle()

# Screen
window = turtle.Screen()
window.title("Turtle Race")
window.bgcolor("white") # bg : background
window.setup(width=850,height=800)

r_img = "C:/Users/Dell/Desktop/Basic_PythonExamples/Race/r_car.gif"
b_img = "C:/Users/Dell/Desktop/Basic_PythonExamples/Race/b_car.gif"

window.addshape(r_img)
window.addshape(b_img)

# Race Area
race = turtle.Turtle()
race.speed(0)
race.shape("arrow")
race.color("black")
race.penup()
race.goto(-300,300)
race.hideturtle()

for i in range(9): # row
    for j in range(31):
        if i == 0:
            race.write(j)
            race.fd(20)
        else:
            race.write("|")
            race.fd(20)
    y=race.ycor()
    x=-300
    race.goto(x,y-20)

# Racer 1 (Red Team)
r1 = turtle.Turtle()
r1.speed(0)
r1.shape(r_img)
r1.color("red")
r1.penup()
r1.goto(-300,250)
r1.pendown()

# Racer 2 (Blue Team)
r2 = turtle.Turtle()
r2.speed(0)
r2.shape(b_img)
r2.color("blue")
r2.penup()
r2.goto(-300,200)
r2.pendown()

r1_gas = 0 
r2_gas = 0

r1_c = 0 # Racer 1 counter
r2_c = 0 # Racer 2 counter

while 1 :
    w_guess = input("Who is win this race? (Blue or Red) : ") 
    w_guess = w_guess.title() # Blue or Red
    if((w_guess == "Blue")or(w_guess == "Red")):
        break


# Race
while 1 :
    r1_gas = random.randint(1,5)
    r2_gas = random.randint(1,5)
    
    r1_c += r1_gas
    r2_c += r2_gas
    
    r1.fd(r1_gas*20)
    r2.fd(r2_gas*20)
    
    if(r1_c >= 30):
        break
    elif(r2_c >= 30):
        break

# Score
pen = turtle.Turtle()
pen.speed(0)
pen.shape("arrow")
pen.penup()
pen.goto(0,350)
pen.hideturtle()

# Score 2
pen1 = turtle.Turtle()
pen1.speed(0)
pen1.shape("arrow")
pen1.color("black")
pen1.penup()
pen1.goto(0,0)
pen1.hideturtle()

# Score 3
pen2 = turtle.Turtle()
pen2.speed(0)
pen2.shape("arrow")
pen2.color("black")
pen2.penup()
pen2.goto(0,-50)
pen2.hideturtle()

if(r1_c > r2_c):
    pen.color("red")
    pen.write("Red Win !!!",align="center",font=("arial",24,"normal"))
    pen1.write("Red Score : {} \nBlue Score : {}".format(r1_c,r2_c),align="center",font=("arial",24,"normal"))
    if w_guess == "Red":
        pen2.write("Congratulations :)",align="center",font=("arial",24,"normal"))    
    else:
        pen2.write("Sorry  :(",align="center",font=("arial",24,"normal"))
    
elif(r2_c > r1_c):   
    pen.color("blue")
    pen.write("Blue Win !!!",align="center",font=("arial",24,"normal"))
    pen1.write("Red Score : {} \nBlue Score : {}".format(r1_c,r2_c),align="center",font=("arial",24,"normal"))
    if w_guess == "Blue":
        pen2.write("Congratulations :)",align="center",font=("arial",24,"normal"))    
    else:
        pen2.write("Sorry  :(",align="center",font=("arial",24,"normal"))
    
    
else:
    pen.color("black")
    pen.write("Draw !!!",align="center",font=("arial",24,"normal"))
    pen1.write("Red Score : {} \nBlue Score : {}".format(r1_c,r2_c),align="center",font=("arial",24,"normal"))

window.mainloop()
