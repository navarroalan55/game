# The main file for the game
import pygame
from menu import Menu
from pygame.locals import *

pygame.init()

# Things that will be need to run

class Main:
    def __init__(self):
        self.window = pygame.display.set_mode((500,400))
        self.title = pygame.display.set_caption('Run!')
        self.Main()

    def Main(self):
        running = True

        while running == True:
            Menu() # Class from menu.py

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

Main()
