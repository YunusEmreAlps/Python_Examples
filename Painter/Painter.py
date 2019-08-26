# Painter

import turtle # Graphical package
import time


turtle.hideturtle()

# Screen
window = turtle.Screen()
window.title("Painter")
window.bgcolor("white")
window.setup(width=600,height=600)

p_img = "C:/Users/Dell/Desktop/Basic_PythonExamples/Painter/pen.gif"

window.addshape(p_img)

# Pen 
pen = turtle.Turtle()
pen.speed(0)
pen.shape(p_img)
pen.color("black")
pen.pensize(3)

def Rem():
    window.onclick(pen.goto)


# Pen Move
def U(): # Up
    y = pen.ycor()
    pen.sety(y+20)
def D(): # Down
    y = pen.ycor()
    pen.sety(y-20)
def R(): # Right
    x = pen.xcor()
    pen.setx(x+20)
def L(): # Left
    x = pen.xcor()
    pen.setx(x-20)
    
# Pen Color
def Dark():
    pen.pencolor("black")
def Light():
    pen.pencolor("white")
def Red():
    pen.pencolor("red")
def Blue():
    pen.pencolor("blue")
def Green():
    pen.pencolor("green")

# Shape
def Sq(): # Square
    while True:
        ang = int(input("Please enter square length ? :"))
        if ang > 0 :
            break
        
    for i in range(4):
        pen.fd(ang)
        pen.left(90)
        
def Cir(): # Circle
    while True:
        ang = int(input("Please enter a radius ? :"))
        if ang > 0 :
            break
    pen.circle(50)        

def Tri(): # Triangle
    while True:
        ang = int(input("Please enter triangle length ? :"))
        if ang > 0 :
            break
    
    for i in range(3):
       pen.fd(ang)
       pen.left(120)

# penup and pendown
def pup(): # penup
    pen.penup()
def pdown(): # pendown
    pen.pendown()
    
# Keyboard 
def key():
    window.onkeypress(U,"Up")
    window.onkeypress(D,"Down")
    window.onkeypress(R,"Right")
    window.onkeypress(L,"Left")
# Other Control schema
    window.onkeypress(U,"w")
    window.onkeypress(D,"s")
    window.onkeypress(R,"d")
    window.onkeypress(L,"a")
# Color Control
    window.onkeypress(Dark,"1")
    window.onkeypress(Light,"2")
    window.onkeypress(Red,"3")
    window.onkeypress(Blue,"4")
    window.onkeypress(Green,"5")    
    
# Draw a basic shape
    window.onkeypress(Sq,"6")
    window.onkeypress(Cir,"7")
    window.onkeypress(Tri,"8")

# penup and pendown
    window.onkeypress(pup,"p")
    window.onkeypress(pdown,"o")
    window.listen()
    
while True:
    window.update()
    key()
    Rem()
    time.sleep(0.01)


window.mainloop()