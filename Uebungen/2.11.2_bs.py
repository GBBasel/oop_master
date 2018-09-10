from gturtle import *

tf = TurtleFrame()

child = Turtle(tf)
child.setColor("red")
child.setPenColor("red")
child.setPos(0, 10)

mother = Turtle(tf)
mother.setColor("green")
mother.setPenColor("green")
mother.setPos(200, 0)
child.speed(-1)
mother.speed(-1)


while True:
    mother.leftArc(50, 6)
    direction = child.towards(mother.getX(), mother.getY())
    child.setHeading(direction)
    child.fd(2)
    