# Napoli.java

from gturtle import *
from math import *
from prosciutto import Prosciutto
           
class Napoli(Prosciutto):
    def drawIngredients(self):
        Prosciutto.drawIngredients(self)
        self.addFungi() 
        self.addOlives()
                 
    def addFungi(self):
        setPenColor(makeColor(190, 190, 190))
        setPos(0, 0)
        dot(100)
  
    def addOlives(self): 
        setPenColor("black")
        for i in range(1, 5):
            setPos(sin(i * pi/2) * 85, cos(i * pi/2) * 85)
            dot(25)
            
    def getPrice(self):
        return 22.50
