from gturtle import *

def line(x1, y1, x2, y2):
    setPos(x1, y1)
    moveTo(x2, y2)

def onMouseMoved(x, y):
    setHeading(towards(x, y))
    forward(10)
    
def onMouseDragged(x, y):
    penDown()
    x1, y1 = getPos()
    line(x1, y1, x, y)
    line(-x1, -y1, -x,-y)
    line(-x1, y1, -x, y)
    line(x1, -y1, x, -y)
    setPos(x, y)
    
def onMouseReleased(x, y):
    penUp()


makeTurtle( mouseMoved = onMouseMoved, mouseDragged = onMouseDragged, mouseReleased = onMouseReleased)
hideTurtle()
speed(-10)
penUp()