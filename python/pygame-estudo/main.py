from game.events import Events
from pygame import init
from pygame import display
from pygame.time import Clock
from game.game import Game

class Main:
    def __init__(self):
        init() # Inicializa o pygame
        self.screen = display.set_mode((800,600)) # Define a tela e o tamanho que ele deve ter
        display.set_caption("Shooter") # Define o texto que fica na tela
        self.game = Game(self.screen) # Cria uma instância da classe Game e passa a tela como argumento
        self.events = Events() # Cria uma instância da classe de eventos
        self.fps = Clock() # Cria uma antincia de relógio do pygame

    def run(self):
        while(True): # Cria o loop infinito a qual o jogo roda
            self.events.quit() # Chama o método de evento que gerencia o fechamento do jogo
            self.game.run() # Executa o conteúdo da classe Game

            display.flip() # Usado para atualizar a tela a todo frame
            self.fps.tick(60) # Limita a quantidade de frames para 60

if (__name__ == "__main__"):
    main = Main()
    main.run() # Executa todo o código 