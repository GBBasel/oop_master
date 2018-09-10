from gturtle import *

LEFT = 37
RIGHT = 39
UP = 38
DOWN = 40
SPACE = 32 

def onKeyPressed(key):
   if key == LEFT:
      setHeading(-90)
   elif key == RIGHT:
      setHeading(90)
   elif key == UP:
      setHeading(0)
   elif key == DOWN:
      setHeading(180)
   elif key == SPACE:
     fill()   

makeTurtle(keyPressed = onKeyPressed)
wrap()
while True:
    forward(10)
    

