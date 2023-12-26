from pygame.sprite import Sprite
from images.images import enemy
from pygame import transform

class Enemy(Sprite):
    def __init__(self):
        super().__init__()
        self.image = transform.scale(enemy, (128,128))
        self.rect = self.image.get_rect(center=(800,400))

    def update(self):
        self.rect = self.rect.move(-1,0)