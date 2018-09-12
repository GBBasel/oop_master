# Pizza.java

from gturtle import *
from math import *

class Pizza():
    def drawDough(self): 
        setPenColor(makeColor(255, 218, 148))
        setPos(0, 0)
        dot(400) 

    def drawTomato(self): 
        setPenColor(makeColor(200, 50, 0))
        dot(350) 
  
    def drawMozzarella(self): 
        setPenColor(makeColor(243, 243, 210))
        for i in range(6):
            setPos(sin(i * pi/3) * 140, cos(i * pi/3) * 140)
            dot(50) 
            
    def createPizza(self): 
        self.drawDough()
        self.drawTomato()
        self.drawMozzarella() 

    def displayPrice(self): 
       setPenColor("blue")
       setPos(-300, -250)
       label(" Please pay  " + str(self.getPrice()) + "0 Fr.")
       
