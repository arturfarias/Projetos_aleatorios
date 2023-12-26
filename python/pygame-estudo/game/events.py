import pygame
import sys

class Events:
    def __init__(self):
        pass

    def quit(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()