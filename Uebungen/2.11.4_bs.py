from gturtle import *

s = 100

makeTurtle()
setPos(-s/2, -s/2)

def drawLine(a, b):
    ax = a.getX()
    ay = a.getY()
    ah = a.heading()
    a.moveTo(b.getX(), b.getY())
    a.setPos(ax, ay)
    a.heading(ah)
    
# generate Turtle clone
t1 = clone() 
t1.speed(-1)
forward(s)
right(60)
t2 = clone()
t2.speed(-1)
forward(s)
right(60)
t3 = clone()
t3.speed(-1)
forward(s)
right(60)
t4 = clone()
t4.speed(-1)
forward(s)
right(60)
hideTurtle()
t5 = clone()
t5.speed(-1)
forward(s)
right(60)
hideTurtle()
t6 = clone()
t6.speed(-1)
forward(s)
right(60)
hideTurtle()

while True:
    t1.setHeading(t1.towards(t2))
    t2.setHeading(t2.towards(t3))
    t3.setHeading(t3.towards(t4))
    t4.setHeading(t4.towards(t5))
    t5.setHeading(t5.towards(t6))
    t6.setHeading(t6.towards(t1))
   
    drawLine(t1, t2)
    drawLine(t2, t3)
    drawLine(t3, t4)
    drawLine(t4, t5)
    drawLine(t5, t6)
    drawLine(t6, t1)

    t1.forward(5)
    t2.forward(5)
    t3.forward(5)
    t4.forward(5)
    t5.forward(5)
    t6.forward(5)

