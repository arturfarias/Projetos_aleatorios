from pygame.sprite import Sprite
from images.images import enemy
from pygame import transform
import random

class Enemy(Sprite):
    def __init__(self):
        super().__init__()
        self.image = transform.scale(enemy, (128,128))
        self.rect = self.image.get_rect(center=(900,random.randrange(40,550)))
        self.speed = random.randrange(-10,-3)

    def update(self):
        self.rect = self.rect.move(self.speed,0)

        if (self.rect.x < -100):
            self.kill()