from game.events import Events
from pygame import init
from pygame import display
from game.game import Game

class Main:
    def __init__(self):
        init()
        self.screen = display.set_mode((800,600))
        display.set_caption("Shooter")
        self.game = Game(self.screen)
        self.events = Events()

    def run(self):
        while(True):
            self.events.quit()
            self.game.run()

            display.flip()

if (__name__ == "__main__"):
    main = Main()
    main.run()