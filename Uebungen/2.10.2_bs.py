from gturtle import *

def onMouseMoved(x, y):
    setHeading(towards(x, y))
    forward(10)
    
def onMouseDragged(x, y):
    penDown()
    setHeading(towards(x, y))
    forward(10)
    
def onMouseReleased(x, y):
    penUp()


makeTurtle( mouseMoved = onMouseMoved, mouseDragged = onMouseDragged, mouseReleased = onMouseReleased)
speed(-10)
penUp()