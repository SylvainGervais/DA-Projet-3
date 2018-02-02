import json
import random

class Labyrinth:
    def __init__(self, map):
        """initialyze labyrinth from file"""
        self.load(map)
                   
    def load(self, mapFile):
        """load a json file in Labyrinth object"""
        try:
            with open(mapFile,"r") as f:
                self.map = json.load(open(mapFile))
                print("Loading map : ",mapFile ,".......OK")
                
        except OSError as e:
            print("Problem with file :", e)

    def print(self) :
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
        for i, line in enumerate(self.map) :
            for j, cell in enumerate(line) :
                if cell == "   " :
                    freeCells.append([i,j])
        return freeCells

    def replaceCell(self, cellLine, cellColumn, content):
        """replace cell's content with coordonates [line, column] by content argument"""
        for i, line in enumerate(self.map):
            if i == cellLine:
                for j, column in enumerate(line):
                    if j == cellColumn:
                        line[j]=content
                       
    def placeItem(self, nbItem, avatar = "<->"):
        """place items randomly in labyrinth"""
        #répéter nb Item fois :
        freeCells = self.getPassages()
        itemCells = random.sample(freeCells, k=nbItem) #choisir parmis les cellules libres une cellule au hasard
        for cell in itemCells:
            itemLine = cell[0]
            itemColumn = cell[1]
            self.replaceCell(itemLine, itemColumn, avatar)
             
            

        


