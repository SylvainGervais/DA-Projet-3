import labyrinth
import config

class Character:
    def __init__(self, labyrinth):
        self.pickedUpItem = 0
        self.labyrinth = labyrinth
        self.position = self.labyrinth.getPositions(config.MAC_GYVER)[0]

                       
    def move(self, direction):
        """for move a character in the labyrinth, it can move front, back, left, right. return list with origin position and destination position if move is done else return none"""
        origin = self.position[:]
        free_cells = self.labyrinth.getPositions(config.FREE_SPACE)
        item_cells = self.labyrinth.getPositions(config.ITEM)
        guardian_cell = self.labyrinth.getPositions(config.GUARDIAN)
        #initialyse destination for not modify self.position if move is prohibited
        destination = self.position[:]
        #destination calculation
        if direction == config.MOVE_FRONT:
            destination[0] -= 1    
        elif direction == config.MOVE_BACK:
            destination[0] += 1
        elif direction == config.MOVE_LEFT:
            destination[1] -= 1
        elif direction == config.MOVE_RIGHT:
            destination[1] += 1
        if destination in free_cells or destination in item_cells or destination in guardian_cell :
            #new character position
            self.position = destination
            #picked up item
            destinationCellContent = self.labyrinth.cellContent(destination)
            if destinationCellContent == config.ITEM :
                self.pickedUpItem += 1
            #modify origin and destination  cell content
            self.labyrinth.replaceCell(origin[0], origin[1], config.FREE_SPACE)
            self.labyrinth.replaceCell(destination[0], destination[1], config.MAC_GYVER)
            return [origin, destination] 

               

