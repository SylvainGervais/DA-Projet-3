#! /usr/bin/env python3
# coding: utf-8

import argparse

import labyrinth
import character
import config
import gui


class Game:
    def __init__(self):
        print("enter a map file (ex : my_map.json) :")
        mapFile = "map.json" 
            #create labyrinth 
        self.labyrinth = labyrinth.Labyrinth(mapFile)
            #place items in map
        self.labyrinth.item_cells = self.labyrinth.place_item(config.NB_ITEM)
            #create Mac Gyver character
        self.character = character.Character(self.labyrinth)
            
    def run(self, args):
        if args.graphic_mode:
            gui_play = gui.Gui(play)
            gui_play.print()
            gui_play.run()
        else:
            #print labyrinth in terminal
            self.labyrinth.print()
            #print rules
            print('You are Mac Gyver "McG". You have to move in labyrinth, pickup all items "<->" and rejoin guardian "!G!"')
            print()
            #print commands
            config.print_commands()

            #get guardian position
            guardian_position = self.labyrinth.get_positions(config.GUARDIAN)[0]
            while (self.character.position != guardian_position):
                print('What do you want ? move or quit game ?????')
                print('Hit', config.PRINT, 'for print commands')
                command = input()
                if command == config.QUIT:
                    print("Loooooser !!!!!!!!!")
                    exit()
                elif command == config.PRINT:
                    config.print_commands()
                elif command in (config.MOVE_FRONT, config.MOVE_BACK, config.MOVE_LEFT, config.MOVE_RIGHT):
                    if(self.character.move(command)): #if move is OK
                        self.labyrinth.print()
                        print("Picked up items ", self.character.picked_up_item,"/", config.NB_ITEM)
                        print()
                    else:
                        print()
                        print("You can't go here ! Choose another direction !!!")
                        print("==================================================================================")
                        print()
                else:
                    print("I don't understand your choice !!!! try again ....")
                    config.print_commands()
            if self.character.picked_up_item == config.NB_ITEM:
                print('===============================================================================================================')
                print()
                print('               The guardian is sleeping, you can exit the labyrinth ------->  you win !!!!')
                print()
                print('===============================================================================================================')
            else:
                print('===============================================================================================================')
                print()
                print("               The guardian stop you, he's too strong for you ----> You looooose !!!")
                print()
                print('===============================================================================================================')

    
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-g", "--graphic_mode", help="for playing in graphic mode", action = "store_true")
    args = parser.parse_args()
    play = Game()
    play.run(args)

    
