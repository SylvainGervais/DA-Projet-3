#! /usr/bin/env python3
# coding: utf-8

import argparse

import labyrinth
import character
import config
import gui


class Game:

    def __init__(self):
        """labyrinth initialisation with items on random positions"""
        print("enter a map file (ex : my_map.json) :")
        mapFile = input() 

        # create labyrinth
        self.labyrinth = labyrinth.Labyrinth(mapFile)

        # place items in map
        self.labyrinth.item_cells = self.labyrinth.place_item(config.NB_ITEM)

        # create Mac Gyver character
        self.character = character.Character(self.labyrinth)

    def run(self, args):
        """loop game while mac gyver and guardian positions are different"""
        if args.graphic_mode:
            gui_play = gui.Gui(play)
            gui_play.print()
            gui_play.run()
        else:
            # print labyrinth in terminal
            self.labyrinth.print()

            # print rules
            print('You are Mac Gyver "McG". You have to move in labyrinth,' 
                  'pickup all items "<->" and rejoin guardian "!G!"')
            print()
            # print commands
            config.print_commands()

            # get guardian position
            guardian_position = self.labyrinth.get_positions(
                config.GUARDIAN)[0]

            # main loop / while mac gyver and guardian position are different
            # call for move
            while (self.character.position != guardian_position):
                print('What do you want ? move or quit game ?????')
                print('Hit', config.PRINT, 'for print commands')
                command = input()
                if command == config.QUIT:
                    print("Loooooser !!!!!!!!!")
                    exit()
                elif command == config.PRINT:
                    config.print_commands()
                elif command in (config.MOVE_FRONT, config.MOVE_BACK,
                                 config.MOVE_LEFT, config.MOVE_RIGHT):

                    # if move is authorized, print labyrinth else print message
                    if(self.character.move(command))!= [None, None]:
                        self.labyrinth.print()
                        print("Picked up items ",
                              self.character.picked_up_item, "/",
                              config.NB_ITEM)
                        print()
                    else:
                        print()
                        print('______________________________________________'
                              '_____________________________________________')
                        print()

                        print("You can't go here !"
                              "Choose another direction !!!")
                        print('______________________________________________'
                              '_____________________________________________')
                        print()
                else:
                    print("I don't understand your choice !!!! try again ....")
                    config.print_commands()
            if self.character.picked_up_item == config.NB_ITEM:
                print('______________________________________________________'
                      '___________________________________________________')
                print()
                print('The guardian is sleeping,'
                      'you can exit the labyrinth -------> you win !!!!')
                print()
                print('______________________________________________________'
                      '_____________________________________________________')
            else:
                print('______________________________________________________'
                      '______________________________________________________')
                print()
                print("The guardian stop you, "
                      "he's too strong for you ----> You looooose !!!")
                print()
                print('______________________________________________________'
                      '______________________________________________________')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-g", "--graphic_mode",
                        help="for playing in graphic mode",
                        action="store_true")
    args = parser.parse_args()
    play = Game()
    play.run(args)
