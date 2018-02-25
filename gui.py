import pygame

import labyrinth
import character
import config
import configGui as gui
import main


class Gui :
    def __init__(self, character) :
        self.character = character
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
        labyrinth = self.character.labyrinth.map
        for i, line in enumerate(labyrinth) :
            for j, cell in enumerate(line) :
                x_blit = gui.LAB_X_ORIGIN + j * gui.SPRITE_WIDTH
                y_blit = gui.LAB_Y_ORIGIN + i * (gui.SPRITE_HEIGHT)
                if cell == config.FREE_SPACE :
                    self.screen.blit(self.img_floor, (x_blit, y_blit))
                elif cell == config.WALL :
                    self.screen.blit(self.img_wall, (x_blit, y_blit))
                elif cell == config.GUARDIAN :
                    self.screen.blit(self.img_floor, (x_blit, y_blit))
                    self.screen.blit(self.img_guardian, (x_blit, y_blit))
                elif cell == config.MAC_GYVER :
                    self.screen.blit(self.img_floor, (x_blit, y_blit))
                    self.screen.blit(self.img_mcg, (x_blit, y_blit))
        pygame.display.flip()

    def run(self):
        continuer = True
        
        while continuer:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    continuer = False 
            pygame.display.flip()

    pygame.quit()


lab = labyrinth.Labyrinth("map.json")
mcG = character.Character(lab)
guiPlay = Gui(mcG)
guiPlay.print()
guiPlay.run()
