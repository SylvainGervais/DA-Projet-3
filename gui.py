import pygame

import random
import labyrinth
import character
import config
import configGui as gui
import main


class Gui:
    def __init__(self, game):
        self.game = game
        self.position_items()
        pygame.init()
        self.screen = pygame.display.set_mode((gui.SCREEN_WIDTH, gui.SCREEN_HEIGHT))
        pygame.display.set_caption("Mac Gyver")
        self.img_mcg = pygame.image.load(gui.IMG_MACGYVER).convert_alpha()
        self.img_floor = pygame.image.load(gui.IMG_FLOOR).convert_alpha()
        self.img_wall = pygame.image.load(gui.IMG_WALL).convert_alpha()
        self.img_guardian = pygame.image.load(gui.IMG_MURDOC).convert_alpha()
        self.img_ether = pygame.image.load(gui.IMG_ETHER).convert_alpha()
        self.img_needle = pygame.image.load(gui.IMG_NEEDLE).convert_alpha()
        self.img_tube = pygame.image.load(gui.IMG_TUBE).convert_alpha()
        self.img_bag_not_full = pygame.image.load(gui.IMG_BAG_NOT_FULL).convert_alpha()
        self.img_bag_full = pygame.image.load(gui.IMG_BAG_FULL).convert_alpha()
        self.img_win= pygame.image.load(gui.IMG_WIN).convert_alpha()
        self.img_loose = pygame.image.load(gui.IMG_LOOSE).convert_alpha()
        self.picked_up_item()

    def position_items(self):
        """position specific items ether, needle and tube on items positions in labyrinth"""
        item_cells = self.game.labyrinth.item_cells[:]
        self.ether_position = random.choice(item_cells)
        item_cells.pop(item_cells.index(self.ether_position))
        self.needle_position = random.choice(item_cells)
        item_cells.pop(item_cells.index(self.needle_position))
        self.tube_position = random.choice(item_cells)

    def print(self):
        """ print labyrinth and item bag in graphic mode """
        labyrinth = self.game.labyrinth.map
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
        move_positions = self.game.character.move(direction)
        if move_positions:
            x_blit_origin = gui.LAB_X_ORIGIN + move_positions[0][1] * gui.SPRITE_WIDTH
            y_blit_origin = gui.LAB_Y_ORIGIN + move_positions[0][0] * gui.SPRITE_HEIGHT
            x_blit_destination = gui.LAB_X_ORIGIN + move_positions[1][1] * gui.SPRITE_WIDTH
            y_blit_destination = gui.LAB_Y_ORIGIN + move_positions[1][0] * gui.SPRITE_HEIGHT
            self.screen.blit(self.img_floor, (x_blit_origin, y_blit_origin))
            self.screen.blit(self.img_mcg, (x_blit_destination, y_blit_destination))
    
    def picked_up_item(self):
        """if MAC GYVER is on item cell, item is picked up in bag"""
        labyrinth_height = len(self.game.labyrinth.map) * gui.SPRITE_HEIGHT
        x_blit_bag = gui.LAB_X_ORIGIN
        y_blit_bag = gui.LAB_Y_ORIGIN + labyrinth_height + gui.SPRITE_HEIGHT
        x_blit_item = x_blit_bag + gui.SPRITE_WIDTH + self.game.character.picked_up_item * gui.SPRITE_WIDTH
        y_blit_item = y_blit_bag
        self.screen.blit(self.img_bag_not_full, (x_blit_bag, y_blit_bag))
        bag_is_full = self.game.character.picked_up_item == config.NB_ITEM
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
        playing = True
        moving = True
        guardian_position = self.game.labyrinth.get_positions(config.GUARDIAN)[0]
        default_font = pygame.font.get_default_font()
        font = pygame.font.SysFont(default_font, 80)
        while playing:
            while moving: 
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            playing = False
                        elif event.key == pygame.K_UP:
                            self.move(config.MOVE_FRONT)
                        elif event.key == pygame.K_DOWN:
                            self.move(config.MOVE_BACK)
                        elif event.key == pygame.K_LEFT:
                            self.move(config.MOVE_LEFT)
                        elif event.key == pygame.K_RIGHT:
                            self.move(config.MOVE_RIGHT)
                        self.picked_up_item()
                        if self.game.character.position == guardian_position:
                            moving = False
                    elif event.type == pygame.QUIT:
                        playing = False
                    pygame.display.flip()
            if self.game.character.picked_up_item == config.NB_ITEM:
                self.screen.blit(self.img_win, (0, 0))
                game_over_text = font.render("YOU WIN !!!", True, (255, 255, 255))
            else:
                self.screen.blit(self.img_loose, (0, 0))
                game_over_text = font.render("YOU LOOSE !!!", True, (255, 255, 255))
            self.screen.blit(game_over_text, (500, 640))
            pygame.display.flip()
            pygame.time.delay(5000)
            playing = False
        pygame.quit()

