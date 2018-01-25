import json

class Labyrinth:
    def __init__(self, map):
        """initialyze labyrinth from file"""
           
    def load(self, mapFile):
        """return a table which represent a map from a json file"""
        try:
            with open(mapFile,"r") as f:
                self.map = json.load(open(mapFile))
                print("Loading map : ",mapFile ,".......OK")
                
        except OSError as e:
            print("Problem with file :", e)

    def printLabyrinth(self) :
        """print labyrinth in terminal"""
        print()
        for line in self.map :
            for cell in line :
                print(cell, end="")
            print()  
        print()

    def getPassages(self):
        """return coordinates of labyrinth's free cells in a table"""
        freeCells = []
        lineCount = 0
        columnCount = 0
        for line in self.map : #pour chaque ligne du labyrinthe chargé:
            for cell in line :
                if cell == "   ":
                    freeCells.append([lineCount , columnCount])
                columnCount += 1
            columnCount = 0
            lineCount += 1
        print(freeCells)
        print()

if __name__ == '__main__':
    
    print("enter a map file (ex : my_map.json) :")
    mapFile = input()
    
    #initialize map argument for labyrinth object
    map = [] 

    labyrinth = Labyrinth(map)

    #load json file map in labyrinth's map argument
    labyrinth.load(mapFile)

    #print labyrinth in terminal
    labyrinth.printLabyrinth()
   
    #recover free cells in map
    labyrinth.getPassages()




