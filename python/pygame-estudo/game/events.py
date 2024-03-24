import pygame
import sys
from pygame.locals import QUIT, KEYDOWN

class Events:
    _instance = None
    
    def __init__(self):
        pass

    def __new__(events):
        if events._instance is None:
            events._instance = super().__new__(events)
        return events._instance

    def run(self): # executa os eventos globais
            self.events = pygame.event.get() # Atualiza eventos e salva no atributo, um por vez
            self.quit()

    def quit(self):
        for event in self.events: # Passa por todos os eventos 
            if event.type == QUIT: # Verdadeiro se foi o evento de fechar o jogo
                pygame.quit() # Finaliza o jogo
                sys.exit() # Finaliza o programa python
    
    def key_pressed(self, key_code):
        key = pygame.key.get_pressed() # pega as teclas precionadas.
        return key[key_code] # Retorna se a tecla pressionada e a mesma em key_code
    
    def key_down(self, key_code): # Método para saber se a tecla foi apertada
        for event in self.events: # Passa por todos os eventos 
            if (event.type == KEYDOWN): # Olha se uma tecla qualquer foi apertada 
                return event.key == key_code  # retorna se a tecla foi a passada ao método
