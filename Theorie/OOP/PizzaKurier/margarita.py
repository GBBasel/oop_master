# Margarita.java

from gturtle import *
import random
from pizza import Pizza
       
class Margarita(Pizza):
    def drawIngredients(self):
        setPenColor(makeColor(23, 67, 0))
        for i in range(70):
            setPos(random.random() * 200 - 100, random.random() * 200 - 100)
            dot(10)  

    def getPrice(self):
        return 15.50
    
