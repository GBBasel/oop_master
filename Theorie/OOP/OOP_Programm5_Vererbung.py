from gamegrid import *
from java.awt import Point

# ---------------- class Animal ----------------
class Animal():
    def __init__(self, imgPath): 
        self.imagePath = imgPath 
    def showMe(self, x, y): 
         bg.drawImage(self.imagePath, x, y)

# ---------------- class Pet ----------------
class Pet(Animal):   # Von Animal abgeleitete Klasse - man kann auch mehrere Basisklassen verwenden.
    def __init__(self, imgPath, name):  
        self.imagePath = imgPath 
        self.name = name #Instanzvariable für den Namen
    def tell(self, x, y): #Zusätzliche Methode, um den Namen anzuzeigen
        bg.drawText(self.name, Point(x, y))

makeGameGrid(600, 600, 1, False)
setBgColor(Color.green)
show()
doRun()
bg = getBg()
bg.setPaintColor(Color.black)

for i in range(5):
    myPet = Pet("sprites/pet.gif", "Trixi")
    myPet.showMe(50 + 100 * i, 100) #Methode ist gar nicht in Pet definiert. Aber pet ist auch ein animal (is-a-relation zwischen pet und animal)
    myPet.tell(72 + 100 * i, 145)

