from images.images import space
from game.entities.character import Character
from game.entities.bullet import Bullet
from game.entities.enemy import Enemy
from pygame.sprite import Group, GroupSingle

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.character = Character()
        self.bullet = Bullet()

        self.BulletGroup = Group()
        self.characterGroup = GroupSingle(self.character)

        self.enemyGroup = Group()
        self.enemyGroup.add(Enemy())

    def run(self):
        self.screen.blit(space,(0,0))
        
        self.characterGroup.draw(self.screen)
        self.characterGroup.update()

        self.enemyGroup.draw(self.screen)
        self.enemyGroup.update()