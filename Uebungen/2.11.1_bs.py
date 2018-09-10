from gturtle import *

def star(t):
    repeat 2:
        t.forward(50)
        t.right(144)
    
tf = TurtleFrame()

maya = Turtle(tf)
maya.setPos(0, 0)
pepe = Turtle(tf)
pepe.setPos(100, 0)
pepe.setColor("red")
hans = Turtle(tf)
hans.setPos(200, 0)
hans.setColor("green")



repeat 3:
 star(maya)
 star(pepe)
 star(hans)