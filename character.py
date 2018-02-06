import labyrinth
import setup

class Character:
    def __init__(self, labyrinth):
        self.position = labyrinth.getPositions(setup.MAC_GYVER)[0]
        self.pickupItem = 0
                       
    def move(self, labyrinth, direction):
        """for move a character in the labyrinth, it can move front, back, left, right"""
        origin = list(self.position)
        freeCells = labyrinth.getPositions(setup.FREE_SPACE)
        itemCells = labyrinth.getPositions(setup.ITEM)
        guardianCell = labyrinth.getPositions(setup.GUARDIAN)
        
        #initialyse destination for not modify self.position if move is prohibited
        destination = list(self.position)
       
        #destination calculation
        if direction == setup.MOVE_FRONT:
            destination[0] -= 1    
        if direction == setup.MOVE_BACK:
            destination[0] += 1
        if direction == setup.MOVE_LEFT:
            destination[1] -= 1
        if direction == setup.MOVE_RIGHT:
            destination[1] += 1

        if destination in freeCells or destination in itemCells or destination in guardianCell :
            #new character position
            self.position = destination
            
            #get origin and destination cells content
            originCellContent = labyrinth.cellContent(origin)
            destinationCellContent = labyrinth.cellContent(destination)

            #pickup item
            if destinationCellContent == setup.ITEM :
                self.pickupItem += 1

            #modify origin and destination  cell content
            labyrinth.replaceCell(origin[0], origin[1], setup.FREE_SPACE)
            labyrinth.replaceCell(destination[0], destination[1], setup.MAC_GYVER)

            """ 
            #modify origin cell content in labyrinth
            if originCellContent == setup.ON_ITEM :
                labyrinth.replaceCell(origin[0], origin[1], setup.ITEM)
            elif originCellContent == setup.WITH_GUARDIAN :
                labyrinth.replaceCell(origin[0], origin[1], setup.GUARDIAN)
            else :
                labyrinth.replaceCell(origin[0], origin[1], setup.FREE_SPACE)


            #modify destinaion cell content in labyrinth
            if destinationCellContent == setup.ITEM:
                labyrinth.replaceCell(destination[0], destination[1], setup.ON_ITEM)
            elif destinationCellContent == setup.GUARDIAN :
                labyrinth.replaceCell(destination[0], destination[1], setup.WITH_GUARDIAN)
            else :
                labyrinth.replaceCell(destination[0], destination[1], setup.MAC_GYVER)
            """

            labyrinth.print()
        else :
            print("This move is not permitted, you must change your choice")
            print()
    '''                                              
    def pickup(self, labyrinth):
        """for pickup item in labyrinth"""
        cellContent = labyrinth.cellContent(self.position)
        if cellContent == setup.ON_ITEM :
            labyrinth.replaceCell(self.position[0], self.position[1], setup.MAC_GYVER)
            self.pickupItem += 1
            labyrinth.print()
        else :
            print("Nothing to pickup here !!!!!")
    '''       
    

