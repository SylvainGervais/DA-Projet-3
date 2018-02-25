import pygame

import random
import labyrinth
import character
import config
import configGui as gui
import main


class Gui :
    def __init__(self, game) :
        self.game = game
        pygame.init()
        self.screen = pygame.display.set_mode((gui.SCREEN_WIDTH, gui.SCREEN_HEIGHT))#, pygame.FULLSCREEN)
        pygame.display.set_caption("Mac Gyver")
        self.img_mcg = pygame.image.load(gui.IMG_MACGYVER).convert_alpha()
        self.img_floor = pygame.image.load(gui.IMG_FLOOR).convert_alpha()
        self.img_wall = pygame.image.load(gui.IMG_WALL).convert_alpha()
        self.img_guardian = pygame.image.load(gui.IMG_MURDOC).convert_alpha()
        self.img_ether = pygame.image.load(gui.IMG_ETHER).convert_alpha()
        self.img_needle = pygame.image.load(gui.IMG_NEEDLE).convert_alpha()
        self.img_tube = pygame.image.load(gui.IMG_TUBE).convert_alpha()

    def print(self) :
        """ print labyrinth in graphic mode """
        labyrinth = self.game.labyrinth.map
        img_items = [self.img_ether, self.img_tube, self.img_needle]
        for i, line in enumerate(labyrinth) :
            for j, cell in enumerate(line) :
                x_blit = gui.LAB_X_ORIGIN + j * gui.SPRITE_WIDTH
                y_blit = gui.LAB_Y_ORIGIN + i * (gui.SPRITE_HEIGHT)
                if cell == config.FREE_SPACE :
                    self.screen.blit(self.img_floor, (x_blit, y_blit))
                elif cell == config.GUARDIAN :
                    self.screen.blit(self.img_floor, (x_blit, y_blit))
                    self.screen.blit(self.img_guardian, (x_blit, y_blit))
                elif cell == config.MAC_GYVER :
                    self.screen.blit(self.img_floor, (x_blit, y_blit))
                    self.screen.blit(self.img_mcg, (x_blit, y_blit))
                elif cell == config.ITEM :
                    self.screen.blit(self.img_floor, (x_blit, y_blit))
                    img = random.choice(img_items)
                    index = img_items.index(img)
                    img_items.pop(index)
                    self.screen.blit(img, (x_blit, y_blit)) 
                else :
                    self.screen.blit(self.img_wall, (x_blit, y_blit))

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

    def run(self):
        continuer = True
        while continuer:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        continuer = False
                    elif event.key == pygame.K_UP:
                        self.move(config.MOVE_FRONT)
                    elif event.key == pygame.K_DOWN:
                        self.move(config.MOVE_BACK)
                    elif event.key == pygame.K_LEFT:
                        self.move(config.MOVE_LEFT)
                    elif event.key == pygame.K_RIGHT:
                        self.move(config.MOVE_RIGHT)
                elif event.type == pygame.QUIT:
                    continuer = False
            pygame.display.flip()
    pygame.quit()


