from gturtle import *

def onMouseHit(x, y):
    fill(x, y)

makeTurtle(mouseHit=onMouseHit)
setCustomCursor("sprites/alien_1.gif")
addStatusBar(30)
setStatusText("Click to fill a region!")

repeat 9:
    forward(200)
    right(160)