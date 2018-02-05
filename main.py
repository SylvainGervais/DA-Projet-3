import labyrinth
import character
import setup


class Main:
    def __init__(self):
         pass

    def run(self):
        pass
    


if __name__ == '__main__':
    print("enter a map file (ex : my_map.json) :")
    mapFile = "map.json" 
        
    #create labyrinth 
    myLabyrinth = labyrinth.Labyrinth(mapFile)

    #place items in map
    myLabyrinth.placeItem(setup.NB_ITEM)
    
    #create Mac Gyver character
    mcG = character.Character(myLabyrinth)

    #get guardian position
    guardianPosition = myLabyrinth.getPositions(setup.GUARDIAN)[0]
    
    #print labyrinth in terminal
    myLabyrinth.print()

    #print rules
    print('You are Mac Gyver "McG". You have to move in labyrinth, pickup all items "<->" and rejoin guardian "!G!"')
    print()

    #print commands
    setup.printCommands()

    while (mcG.position != guardianPosition or mcG.pickupItem != setup.NB_ITEM) :
        print('What do you want ? move, pickup or quit game ?????')
        print('Hit', setup.PRINT, 'for print commands')
        command = input()

        if command == setup.QUIT :
            print("Loooooser !!!!!!!!!")
            exit()

        elif command == setup.PRINT :
            setup.printCommands()

        elif command == setup.PICKUP :
            mcG.pickup(myLabyrinth)

        elif command in (setup.MOVE_FRONT, setup.MOVE_BACK, setup.MOVE_LEFT, setup.MOVE_RIGHT) :
            mcG.move(myLabyrinth, command)

        else :
            print("I don't understand your choice !!!! try again ....")
            setup.printCommands()           
    print('==================================================================================================================')
    print()
    print('               You can exit the labyrinth, you win the game !!!!')
    print()
    print('==================================================================================================================')



