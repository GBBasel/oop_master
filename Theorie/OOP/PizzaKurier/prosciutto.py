# Prosciutto.py

from gturtle import *
from pizza import Pizza
         
class Prosciutto(Pizza):
    def drawIngredients(self):
        setPenColor(makeColor(171, 87, 84))
        setPos(0, 0)
        dot(220)

    def getPrice(self):
        return 19.50
