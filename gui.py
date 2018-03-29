import pygame as pg

import random
import labyrinth
import character
import config
import configGui as gui
import main


class Gui:
    def __init__(self, game):
        """initialize graphical mode"""
        # store console game in gui attributes 
        self.game = game

        # place items pictures
        self.position_items()
        
        #pygame
        pg.init()
        self.screen = pg.display.set_mode(
            (gui.SCREEN_WIDTH, gui.SCREEN_HEIGHT)
        )
        pg.display.set_caption("Mac Gyver")

        #load pictures
        self.img_mcg = pg.image.load(gui.IMG_MACGYVER).convert_alpha()
        self.img_floor = pg.image.load(gui.IMG_FLOOR).convert_alpha()
        self.img_wall = pg.image.load(gui.IMG_WALL).convert_alpha()
        self.img_guardian = pg.image.load(
            gui.IMG_MURDOC).convert_alpha()
        self.img_ether = pg.image.load(gui.IMG_ETHER).convert_alpha()
        self.img_needle = pg.image.load(gui.IMG_NEEDLE).convert_alpha()
        self.img_tube = pg.image.load(gui.IMG_TUBE).convert_alpha()
        self.img_bag_not_full = pg.image.load(
            gui.IMG_BAG_NOT_FULL).convert_alpha()
        self.img_bag_full = pg.image.load(
            gui.IMG_BAG_FULL).convert_alpha()
        self.img_win = pg.image.load(gui.IMG_WIN).convert_alpha()
        self.img_loose = pg.image.load(gui.IMG_LOOSE).convert_alpha()
        self.picked_up_item()
        
        # fonts
        default_font = pg.font.get_default_font()
        font = pg.font.SysFont(default_font, 80)


    def position_items(self):
        """position specific items ether, needle and tube in labyrinth"""
        item_cells = self.game.labyrinth.item_cells[:]
        self.ether_position = random.choice(item_cells)
        item_cells.pop(item_cells.index(self.ether_position))
        self.needle_position = random.choice(item_cells)
        item_cells.pop(item_cells.index(self.needle_position))
        self.tube_position = random.choice(item_cells)

    def print(self):
        """ print labyrinth and item bag in graphic mode """
        labyrinth = self.game.labyrinth.map

        #print labyrinth n graphical mode
        for i, line in enumerate(labyrinth):
            for j, cell in enumerate(line):
                x_blit = gui.LAB_X_ORIGIN + j * gui.SPRITE_WIDTH
                y_blit = gui.LAB_Y_ORIGIN + i * (gui.SPRITE_HEIGHT)
                if cell in (config.FREE_SPACE, config.ITEM):
                    self.screen.blit(self.img_floor, (x_blit, y_blit))
                elif cell == config.GUARDIAN:
                    self.screen.blit(self.img_floor, (x_blit, y_blit))
                    self.screen.blit(self.img_guardian, (x_blit, y_blit))
                elif cell == config.MAC_GYVER:
                    self.screen.blit(self.img_floor, (x_blit, y_blit))
                    self.screen.blit(self.img_mcg, (x_blit, y_blit))
                else:
                    self.screen.blit(self.img_wall, (x_blit, y_blit))
                if [i, j] == self.ether_position:
                    self.screen.blit(self.img_ether, (x_blit, y_blit))
                elif [i, j] == self.needle_position:
                    self.screen.blit(self.img_needle, (x_blit, y_blit))
                elif [i, j] == self.tube_position:
                    self.screen.blit(self.img_tube, (x_blit, y_blit))

    def move(self, direction):
        """move mac gyver in labyrinth in graphic mode"""
        start_position, dest_position = self.game.character.move(direction)

        # move function in labyrinth class return start and destination position
        # the list is [line, column] like [y, x] coordinates
        start_y, start_x = start_position or [None, None]
        dest_y, dest_x = dest_position or [None, None]

        #if move authorized, start position is not None
        if start_position:
            x_blit_origin = gui.LAB_X_ORIGIN + start_x * gui.SPRITE_WIDTH
            y_blit_origin = gui.LAB_Y_ORIGIN + start_y * gui.SPRITE_HEIGHT
            x_blit_destination = gui.LAB_X_ORIGIN + dest_x * gui.SPRITE_WIDTH
            y_blit_destination = gui.LAB_Y_ORIGIN + dest_y * gui.SPRITE_HEIGHT
            self.screen.blit(self.img_floor, (x_blit_origin, y_blit_origin))
            self.screen.blit(
                self.img_mcg, (x_blit_destination, y_blit_destination))

    def picked_up_item(self):
        """if MAC GYVER is on item cell, item is picked up in bag"""
        nb_item_in_bag = self.game.character.picked_up_item

        # initialize items box
        labyrinth_height = len(self.game.labyrinth.map) * gui.SPRITE_HEIGHT
        x_blit_bag = gui.LAB_X_ORIGIN
        y_blit_bag = gui.LAB_Y_ORIGIN + labyrinth_height + gui.SPRITE_HEIGHT

        #calculate position to print items in box when picked up
        x_blit_item = x_blit_bag + gui.SPRITE_WIDTH + (
            nb_item_in_bag * gui.SPRITE_WIDTH)
        y_blit_item = y_blit_bag

        self.screen.blit(self.img_bag_not_full, (x_blit_bag, y_blit_bag))

        # when items are picked up, picture is moved in items box
        # the indicator change when bag is full
        bag_is_full = nb_item_in_bag == config.NB_ITEM
        mcg_position = self.game.character.position
        list_items_positions = self.game.labyrinth.item_cells
        if mcg_position in list_items_positions:
            if mcg_position == self.ether_position:
                self.screen.blit(self.img_ether, (x_blit_item, y_blit_item))
            elif mcg_position == self.needle_position:
                self.screen.blit(self.img_needle, (x_blit_item, y_blit_item))
            elif mcg_position == self.tube_position:
                self.screen.blit(self.img_tube, (x_blit_item, y_blit_item))
            list_items_positions.pop(list_items_positions.index(mcg_position))
        if bag_is_full:
            self.screen.blit(self.img_bag_full, (x_blit_bag, y_blit_bag))

    def run(self):
        """game loop in graphic mode"""
        playing = True
        moving = True
        guardian_position = self.game.labyrinth.get_positions(
            config.GUARDIAN)[0]
        while playing:
            while moving:
                for event in pg.event.get():
                    if event.type == pg.KEYDOWN:
                        if event.key == pg.K_ESCAPE:
                            moving = False
                            playing = False
                        elif event.key == pg.K_UP:
                            self.move(config.MOVE_FRONT)
                        elif event.key == pg.K_DOWN:
                            self.move(config.MOVE_BACK)
                        elif event.key == pg.K_LEFT:
                            self.move(config.MOVE_LEFT)
                        elif event.key == pg.K_RIGHT:
                            self.move(config.MOVE_RIGHT)
                        self.picked_up_item()
                        if self.game.character.position == guardian_position:
                            moving = False
                    elif event.type == pg.QUIT:
                        moving = False
                        playing = False
                    pg.display.flip()
            if self.game.character.picked_up_item == config.NB_ITEM:
                self.screen.blit(self.img_win, (0, 0))
                game_over_text = font.render(
                    "YOU WIN !!!", True, (255, 255, 255))
            else:
                self.screen.blit(self.img_loose, (0, 0))
                game_over_text = font.render(
                    "YOU LOOSE !!!", True, (255, 255, 255))
            self.screen.blit(game_over_text, (500, 640))
            pg.display.flip()

            # screen autoclose when game is over
            pg.time.delay(3000)
            playing = False
        pg.quit()
