#! /usr/bin/env python3
# coding: utf-8


import labyrinth
import character
import config


class Main:
    def __init__(self):
         pass

    def run(self):
        pass

def main() :
    print("enter a map file (ex : my_map.json) :")
    mapFile = "map.json" 
        
    #create labyrinth 
    myLabyrinth = labyrinth.Labyrinth(mapFile)

    #place items in map
    myLabyrinth.placeItem(config.NB_ITEM)
    
    #create Mac Gyver character
    mcG = character.Character(myLabyrinth)

    #get guardian position
    guardianPosition = myLabyrinth.getPositions(config.GUARDIAN)[0]
    
    #print labyrinth in terminal
    myLabyrinth.print()

    #print rules
    print('You are Mac Gyver "McG". You have to move in labyrinth, pickup all items "<->" and rejoin guardian "!G!"')
    print()

    #print commands
    config.printCommands()

    while (mcG.position != guardianPosition) :
        print('What do you want ? move or quit game ?????')
        print('Hit', config.PRINT, 'for print commands')
        command = input()

        if command == config.QUIT :
            print("Loooooser !!!!!!!!!")
            exit()

        elif command == config.PRINT :
            config.printCommands()

       
        elif command in (config.MOVE_FRONT, config.MOVE_BACK, config.MOVE_LEFT, config.MOVE_RIGHT) :
            mcG.move(command)
            myLabyrinth.print()

        else :
            print("I don't understand your choice !!!! try again ....")
            config.printCommands()

    if mcG.pickedUpItem == config.NB_ITEM :
        print('==================================================================================================================')
        print()
        print('               The guardian is sleeping, you can exit the labyrinth ------->  you win !!!!')
        print()
        print('==================================================================================================================')
    else :
        print('==================================================================================================================')
        print()
        print("               The guardian stop you, he's too strong for you ----> You looooose !!!")
        print()
        print('==================================================================================================================')


if __name__ == '__main__':
    main()


