import labyrinth
import setup

class Character:
    def __init__(self, labyrinth):
        self.position = labyrinth.getPositions(setup.MAC_GYVER)
        self.pickupItem = 0

    def move(self):
        """for move a character in the labyrinth, it can move front, back, left, right"""
        direction = input()
        destination = self.position  #initialyse destination for not modify self.position if move is prohibited
        if direction == MOVE_FRONT:
            for i, j in destination:
                i-=1
        if direction == MOVE_BACK:
            for i, j in destination:
                i+=1
        if direction == MOVE_LEFT:
            for i, j in destination:
                j-=1
        if direction == MOVE_RIGHT:
            for i, j in destination:
                j+=1

          
        #si la destination est espace libre ou objet:
            #mettre l'avatar du personnage sur la cellule destination
            #effacer l'avatar sur la position d'origine
        #sinon:
            #message ("You want move ", direction," but this is prohibited")

    def pickup(self):
        """for pickup item in labyrinth"""
        pass


