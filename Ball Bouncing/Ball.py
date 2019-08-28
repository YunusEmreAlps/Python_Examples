# Ball Bouncing

import turtle # Graphical package
import random # Random package 

turtle.hideturtle() # invisible

# Screen
window = turtle.Screen()
window.title("Ball Bouncing")
window.bgcolor("black") # bg : background
window.setup(width=800,height=620)
window.tracer(0)

# Ball
shapes = ("square","triangle","circle")
colors = ("red","blue","orange","lime","white","gray","pink","purple")

balls = []

number = random.randint(10,25)

for i in range(number):
    balls.append(turtle.Turtle())

gravity = 0.01

for ball in balls:
    ball.shape(random.choice(shapes))
    ball.color(random.choice(colors))
    ball.penup()  
    ball.speed(0)
    x = random.randint(-290,290)
    y = random.randint(-290,290)
    ball.goto(x,y)
    ball.dy = 0
    ball.dx = random.randint(-3,3)
    ball.da = random.randint(-3,3)
   

   
while True:
    window.update()
    for i in balls:
        i.dy -= gravity
        i.rt(i.da)
        i.sety(i.ycor()+i.dy)
        i.setx(i.xcor()+i.dx)
        
        if i.xcor() > 300:
            i.dx *= -1
            i.da *= -1
        if i.xcor() < -300:
            i.dx *= -1
            i.da *= -1

        if i.ycor() < -300:
            i.dy *= -1
            i.da *= -1



