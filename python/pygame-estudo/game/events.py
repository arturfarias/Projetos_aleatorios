import pygame
import sys

class Events:
    def __init__(self):
        pass

    def quit(self):
        for event in pygame.event.get(): # Checa todos os eventos que acontecem
            if event.type == pygame.QUIT: # Verdadeiro se foi o evento de fechar o jogo
                pygame.quit() # Finaliza o jogo
                sys.exit() # Finaliza o programa python