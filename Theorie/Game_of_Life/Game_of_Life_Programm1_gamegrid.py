from gamegrid import *

class Game(GameGrid): 
    def __init__(self):
        GameGrid.__init__(self, s, s, 800 // s, Color.gray)
        self.setTitle("Game of Life")
        self.reset()
        self.show()
        
s = 50 # Number of cells in each direction
Game()       
