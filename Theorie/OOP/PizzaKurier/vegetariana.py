# Vegetariana.java

from gturtle import *
from pizza import Pizza
           
class Vegetariana(Pizza):
    def drawIngredients(self):
        setPenColor(makeColor(65, 116, 65))
        setPos(0, 0)
        dot(220)

    def getPrice(self):
        return 18.00
