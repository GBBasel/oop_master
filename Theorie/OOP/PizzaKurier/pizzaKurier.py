# PizzaKurier.py

from gturtle import *
from margarita import Margarita
from prosciutto import Prosciutto
from vegetariana import Vegetariana
from napoli import Napoli

choice = inputString("Margarita, Prosciutto, Vegetariana or Napoli?")
myPizza = None
if choice == "Margarita": 
    myPizza = Margarita()
elif choice == "Prosciutto":
    myPizza = Prosciutto()
elif choice == "Vegetariana": 
    myPizza = Vegetariana()
elif choice == "Napoli": 
    myPizza = Napoli()  
else:
    msgDlg("No pizza of this type!") 
               
if myPizza != None:
    makeTurtle()
    hideTurtle() 
    myPizza.createPizza()
    myPizza.drawIngredients()
    myPizza.displayPrice()
    setTitle(choice)
