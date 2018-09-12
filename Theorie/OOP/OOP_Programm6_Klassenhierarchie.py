from gamegrid import *

# ---------------- class Animal ----------------
class Animal():
    def __init__(self, imgPath): 
        self.imagePath = imgPath 
    def showMe(self, x, y):  
         bg.drawImage(self.imagePath, x, y) 
         
# ---------------- class Pet ----------------
class Pet(Animal): #Basisklasse Animal: Pet is an Animal
    def __init__(self, imgPath, name): 
        Animal.__init__(self, imgPath) #äquivalent zu: self.imagePath = imgPath: : Die Initialisierung der Instanzvariablen erfolgt durch den Konstruktor der Basisklasse   
        self.name = name
    def tell(self, x, y):
        bg.drawText(self.name, Point(x, y))

# ---------------- class Dog ----------------
class Dog(Pet): #Basisklasse Pet: Dog is a Pet is an Animal
    def __init__(self, imgPath, name): 
        Pet.__init__(self, imgPath, name)  #äquivalent zu: self.imagePath = imgPath
    def tell(self, x, y): #Überschreiben der Methode aus Pet
        bg.setPaintColor(Color.blue)
        bg.drawText(self.name + " tells 'Waoh'", Point(x, y))

# ---------------- class Cat ----------------
class Cat(Pet): #Basisklasse Pet: Cat is a Pet is an Animal
    def __init__(self, imgPath, name):
        Pet.__init__(self, imgPath, name) #äquivalent zu: self.imagePath = imgPath
    def tell(self, x, y): #Überschreiben der Methode aus Pet
        bg.setPaintColor(Color.gray)
        bg.drawText(self.name + "  tells 'Meow'", Point(x, y))

makeGameGrid(600, 600, 1, False)
setBgColor(Color.green)
show()
doRun()
bg = getBg()

alex = Dog("sprites/dog.gif", "Alex")
alex.showMe(100, 100) 
alex.tell(200, 130)  #Überschriebene Methode wird aufgerufen

rex = Dog("sprites/dog.gif", "Rex")
rex.showMe(100, 300) 
rex.tell(200, 330)  #Überschriebene Methode wird aufgerufen

xara = Cat("sprites/cat.gif", "Xara")
xara.showMe(100, 500) 
xara.tell(200, 530)  #Überschriebene Methode wird aufgerufen

