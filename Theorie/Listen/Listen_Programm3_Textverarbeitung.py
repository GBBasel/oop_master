from gpanel import *

BS = 8
SPACE = 32
DEL = 127
#Infobalken
def showInfo(key):
    text = "List length = " + str(len(letterList))
    if key != "":
        text += ". Last key code = " + str(ord(key))
    setStatusText(text)  
        
def updateGraphics():
    clear()#löscht Fensterinhalt (füllt mit Hintergrundfarbe) und setzt Cursor auf (0, 0)
    for i in range(len(letterList)):
        text(i, 2, letterList[i], Font("Courier", Font.PLAIN, 24), 
              "blue", "light gray") #text(x, y, string, font, textColor, bgColor) 
    line(cursorPos - 0.2, 1.7, cursorPos - 0.2, 2.7) #line(x1, y1, x2, y2)

def onMousePressed(x, y):
    setCursor(x)
    updateGraphics()

def setCursor(x):
    global cursorPos
    pos = int(x + 0.7)
    if pos <= len(letterList):    
       cursorPos = pos

makeGPanel(-1, 30, 0, 12, mousePressed = onMousePressed)

letterList = []
cursorPos = 0
addStatusBar(30)
setStatusText("Enter Text. Backspace to delete. Mouse to set cursor.")
lineWidth(3) #setzt die Stiftdicke (in Pixel)

while True:
    delay(10) #Programm um Zeit time (Millisekunden) anhalten
    key = getKey() #holt den letzten Tastendruck ab und liefert String zurück (leer, falls illegale Taste)
    if key == "":
        continue
    keyCode = ord(key) #ord() gibt den integer des Unicodes zurück für den jeweiligen key.
    if keyCode == BS:  # backspace
        if cursorPos > 0:
            cursorPos -= 1
            letterList.pop(cursorPos)
    elif keyCode >= SPACE and keyCode != DEL:      
        letterList.insert(cursorPos, key)
        cursorPos += 1
    updateGraphics()
    showInfo(key)

