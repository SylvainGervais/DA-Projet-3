import json
import random

import setup

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

    def getPositions(self, content):
        """return coordinates list of labyrinth's cells corresponding content argument"""
        positions = []
        for i, line in enumerate(self.map) :
            for j, cell in enumerate(line) :
                if cell == content :
                    positions.append([i,j])
        return positions

    def replaceCell(self, cellLine, cellColumn, content):
        """replace cell's content with coordonates [line, column] by content argument"""
        for i, line in enumerate(self.map):
            if i == cellLine:
                for j, column in enumerate(line):
                    if j == cellColumn:
                        line[j]=content
                       
    def placeItem(self, nbItem):
        """place items randomly in labyrinth"""
        freeCells = self.getPositions(setup.FREE_SPACE)
        itemCells = random.sample(freeCells, k=nbItem) 
        for cell in itemCells:
            itemLine = cell[0]
            itemColumn = cell[1]
            self.replaceCell(itemLine, itemColumn,setup.ITEM)
             
    def cellContent(self, position):
        """return cell's content in labyrinth position in argument"""
        linePosition = position[0]
        columnPosition = position[1]

        for i, line in enumerate(self.map):
            if i == linePosition :
                content = line[columnPosition]
        return content

        


