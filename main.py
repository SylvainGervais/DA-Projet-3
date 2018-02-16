#! /usr/bin/env python3
# coding: utf-8


import labyrinth
import character
import config


class Game:
    def __init__(self):
        print("enter a map file (ex : my_map.json) :")
        mapFile = "map.json" 
            
        #create labyrinth 
        self.labyrinth = labyrinth.Labyrinth(mapFile)

        #place items in map
        self.labyrinth.placeItem(config.NB_ITEM)
        
        #create Mac Gyver character
        self.character = character.Character(self.labyrinth)

        #print labyrinth in terminal
        self.labyrinth.print()

        #print rules
        print('You are Mac Gyver "McG". You have to move in labyrinth, pickup all items "<->" and rejoin guardian "!G!"')
        print()

        #print commands
        config.printCommands()


    def run(self):
        
        #get guardian position
        guardianPosition = self.labyrinth.getPositions(config.GUARDIAN)[0]

        while (self.character.position != guardianPosition) :
            print('What do you want ? move or quit game ?????')
            print('Hit', config.PRINT, 'for print commands')
            command = input()

            if command == config.QUIT :
                print("Loooooser !!!!!!!!!")
                exit()

            elif command == config.PRINT :
                config.printCommands()

           
            elif command in (config.MOVE_FRONT, config.MOVE_BACK, config.MOVE_LEFT, config.MOVE_RIGHT) :
                if(self.character.move(command)): #if move is OK
                    self.labyrinth.print()
                    print("Picked up items ", self.character.pickedUpItem,"/", config.NB_ITEM)
                    print()

                else:
                    print()
                    print("You can't go here ! Choose another direction !!!")
                    print("==================================================================================")
                    print()

            else :
                print("I don't understand your choice !!!! try again ....")
                config.printCommands()

        if self.character.pickedUpItem == config.NB_ITEM :
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
    play = Game()
    play.run()

    
