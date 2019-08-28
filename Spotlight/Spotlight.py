# Spotlight

import turtle # Graphical package
import time

turtle.hideturtle() # invisible

# Screen
window = turtle.Screen()
window.title("Spotlight")
window.bgcolor("black")
window.setup(width=600,height=600) 

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("turtle")
pen.color("yellow")
pen.penup()
pen.goto(-200,100) 
pen.hideturtle()

# Rectangle
for i in range(4): # 0,1,2,3
    pen.pendown()
    if(i%2 == 0):
        pen.fd(80)
    else:
        pen.fd(160)
    pen.right(90)
    pen.penup()
    
# Red
red_1 = turtle.Turtle()
red_1.speed(0)
red_1.shape("circle")
red_1.color("gray")
red_1.penup()
red_1.goto(-160,60)

# Yellow
yel_1 = turtle.Turtle()
yel_1.speed(0)
yel_1.shape("circle")
yel_1.color("gray")
yel_1.penup()
yel_1.goto(-160,20)

# Green
gre_1 = turtle.Turtle()
gre_1.speed(0)
gre_1.shape("circle")
gre_1.color("gray")
gre_1.penup()
gre_1.goto(-160,-20)

# Pen 2
pen_1 = turtle.Turtle()
pen_1.speed(0)
pen_1.shape("turtle")
pen_1.color("yellow")
pen_1.penup()
pen_1.goto(-80,100) 
pen_1.hideturtle()

# Rectangle
for i in range(4): # 0,1,2,3
    pen_1.pendown()
    if(i%2 == 0):
        pen_1.fd(80)
    else:
        pen_1.fd(160)
    pen_1.right(90)
    pen_1.penup()
    
# Red
red_2 = turtle.Turtle()
red_2.speed(0)
red_2.shape("circle")
red_2.color("gray")
red_2.penup()
red_2.goto(-40,60)

# Yellow
yel_2 = turtle.Turtle()
yel_2.speed(0)
yel_2.shape("circle")
yel_2.color("gray")
yel_2.penup()
yel_2.goto(-40,20)

# Green
gre_2 = turtle.Turtle()
gre_2.speed(0)
gre_2.shape("circle")
gre_2.color("gray")
gre_2.penup()
gre_2.goto(-40,-20)

# Pen 3
pen_2 = turtle.Turtle()
pen_2.speed(0)
pen_2.shape("turtle")
pen_2.color("yellow")
pen_2.penup()
pen_2.goto(40,100) 
pen_2.hideturtle()

# Rectangle
for i in range(4): # 0,1,2,3
    pen_2.pendown()
    if(i%2 == 0):
        pen_2.fd(80)
    else:
        pen_2.fd(160)
    pen_2.right(90)
    pen_2.penup()
    
# Red
red_3 = turtle.Turtle()
red_3.speed(0)
red_3.shape("circle")
red_3.color("gray")
red_3.penup()
red_3.goto(80,60)

# Yellow
yel_3 = turtle.Turtle()
yel_3.speed(0)
yel_3.shape("circle")
yel_3.color("gray")
yel_3.penup()
yel_3.goto(80,20)

# Green
gre_3 = turtle.Turtle()
gre_3.speed(0)
gre_3.shape("circle")
gre_3.color("gray")
gre_3.penup()
gre_3.goto(80,-20)

# Main Function
while True:
    window.update()
    

    red_1.color("red")
    yel_2.color("yellow")
    gre_3.color("green")
    time.sleep(1)
    red_1.color("gray")
    yel_2.color("gray")
    gre_3.color("gray")
    
    yel_1.color("yellow")
    gre_2.color("green")
    red_3.color("red")
    time.sleep(1)
    yel_1.color("gray")
    gre_2.color("gray")
    red_3.color("gray")
    
    gre_1.color("green")
    red_2.color("red")
    yel_3.color("yellow")
    time.sleep(1)
    gre_1.color("gray")
    red_2.color("gray")
    yel_3.color("gray")
    
window.mainloop() # ! important