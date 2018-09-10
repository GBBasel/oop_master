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
    
def onMouseHit(x, y):
    if isRightMouseButton():
       fill(x, y)

makeTurtle( mouseMoved = onMouseMoved, mouseDragged = onMouseDragged, mouseReleased = onMouseReleased, mouseHit = onMouseHit)
speed(-10)
penUp()