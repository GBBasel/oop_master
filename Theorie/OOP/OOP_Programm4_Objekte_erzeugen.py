from gamegrid import *

# ---------------- class Animal ----------------
class Animal(): #Klasse Animal wird definiert.
    def __init__(self, imgPath): #Der Konstruktor mit dem Bildpfad als Parameter wird definiert
        self.imagePath = imgPath  #Die Instanzvariable.
    def showMe(self, x, y):  #Methode wird definiert.
         bg.drawImage(self.imagePath, x, y)#Zeichnungsmethode aus der Klasse GameGrid

def pressCallback(e): #Callback für den Mouse-Event
    myAnimal = Animal("sprites/animal.gif") #Hier wird ein Objekt mit dem entsprechend Bildpfad erstellt. 
    myAnimal.showMe(e.getX(), e.getY())  #Die Methode wird aufgerufen, wobei der Parameter self durch das Objekt ersetzt wird.

makeGameGrid(600, 600, 1, False, mousePressed = pressCallback)
setBgColor(Color.green)
show()
doRun()
bg = getBg() #gibt die Referenz auf GGBackground zurück

