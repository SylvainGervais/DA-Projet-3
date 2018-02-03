import labyrinth
import character
import setup


class Main:
    def __init__():
        pass

    def run():
        pass
    


if __name__ == '__main__':
    
    print("enter a map file (ex : my_map.json) :")
    mapFile = input()
    
    labyrinth = labyrinth.Labyrinth(mapFile)
    
    #place items in map
    labyrinth.placeItem(3)

    #print labyrinth in terminal
    labyrinth.print()

    mcG = character.Character(labyrinth)
    print("Position de Mac Gyver : ", mcG.position)
    print("Sac à dos : ", mcG.pickupItem, "/", setup.BAG_CAPACITY)




