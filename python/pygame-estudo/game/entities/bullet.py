from pygame.sprite import Sprite
from images.images  import bullet

class Bullet(Sprite):
    def __init__(self):
        super().__init__()
        self.image = bullet
        self.rect = self.image.get_rect()

    def update(self):
        pass
