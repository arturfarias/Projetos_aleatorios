from pygame.sprite import Sprite
from images.images import player
from pygame import transform

class Character(Sprite):
    def __init__(self):
        super().__init__()

        self.image = transform.scale(player, (128,128))
        self.rect = self.image.get_rect()

    def update(self):
        pass