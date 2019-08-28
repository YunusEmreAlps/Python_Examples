# Spotlight 2 (class)

import turtle # Graphical package
import time

turtle.hideturtle() # invisible

# Screen
window = turtle.Screen()
window.title("Spotlight")
window.bgcolor("black")
window.setup(width=600,height=600) 

class Spotlight():
    def __init__(self,x,y):
        
        # Pen
        self.pen = turtle.Turtle()
        self.pen.speed(0)
        self.pen.shape("turtle")
        self.pen.color("yellow")
        self.pen.penup()
        self.pen.goto(x,y) 
        self.pen.hideturtle()
        
        # Rectangle
        for i in range(4): # 0,1,2,3
            self.pen.pendown()
            if(i%2 == 0):
                self.pen.fd(80)
            else:
                self.pen.fd(160)
            self.pen.right(90)
            self.pen.penup()
        
        self.red_1 = turtle.Turtle()
        self.yel_1 = turtle.Turtle()
        self.gre_1 = turtle.Turtle()  
            
        self.red_1.speed(0)
        self.yel_1.speed(0)
        self.gre_1.speed(0)
           
        self.red_1.shape("circle")
        self.yel_1.shape("circle")
        self.gre_1.shape("circle")
            
        self.red_1.color("gray")
        self.yel_1.color("gray")
        self.gre_1.color("gray")
            
        self.red_1.penup()
        self.yel_1.penup()
        self.gre_1.penup()
            
        self.red_1.goto(x+40,y-40)
        self.yel_1.goto(x+40,y-80)
        self.gre_1.goto(x+40,y-120)
    
    def change(self,color):
        self.red_1.color("gray")
        self.yel_1.color("gray")
        self.gre_1.color("gray")
            
        if color == "red":
            self.red_1.color("red")
        elif color == "yellow":
            self.yel_1.color("yellow")
        elif color == "green":
            self.gre_1.color("green")

            
s_1 = Spotlight(-200,100)
s_2 = Spotlight(-80,100)
s_3 = Spotlight(40,100)

# Main Function
while True:
    window.update()
    
    s_1.change("red")
    s_2.change("yellow")
    s_3.change("green")
    time.sleep(1)
    s_1.change("yellow")
    s_2.change("green")
    s_3.change("red")    
    time.sleep(1)
    s_1.change("green")
    s_2.change("red")
    s_3.change("yellow")
    time.sleep(1)
    
    
window.mainloop() # ! important

