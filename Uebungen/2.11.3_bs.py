from gturtle import *

def step(t):
    repeat 4:
        t.forward(50)
        t.right(90)
    t.penUp()
    t.forward(70)
    t.penDown()
    
tf = TurtleFrame()

laura = Turtle(tf, "sprites/beetle.gif")
laura.setPos(0, -50)
pepe = Turtle(tf, "sprites/cuteturtle.gif")
pepe.setPos(25, -95)
pepe.setFillColor("green")

repeat 7:
    step(laura)
    pepe.penUp()
    pepe.forward(70)
    pepe.fill()
    