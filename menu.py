# Menu for game
import pygame

pygame.font.init()
# define constants
myfont = pygame.font.SysFont("monospace", 30)

class Menu():
    def __init__(self):
        window = pygame.display.set_mode((500,400))
        self.main_menu(window)

    def main_menu(self, window):
        window.fill((0,0,0))
        label = myfont.render("RUN!", 1, (255,255,0))
        window.blit(label, (100,100))
        pygame.display.flip()
        # make buttons
