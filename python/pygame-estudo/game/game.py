from images.images import space
from game.entities.character import Character
from game.entities.bullet import Bullet
from game.entities.enemy import Enemy
from pygame.sprite import Group, GroupSingle

class Game:
    def __init__(self, screen):
        self.screen = screen # Cria um atributo com a referência da tela do jogo
        self.character = Character() # Cria uma instância do personagem
        self.bullet = Bullet() # Cria uma instância da bala

        self.BulletGroup = Group() # Cria um grupo para as balas
        self.characterGroup = GroupSingle(self.character) # Cria um grupo para o personagem

        self.enemyGroup = Group() # Cria um grupo para os inimigos
        self.enemyGroup.add(Enemy()) # Adiciona uma instância de inimigo para o grupo
        self.enemyGroup.add(Enemy()) # Adiciona uma instância de inimigo para o grupo

    def run(self):
        self.screen.blit(space,(0,0)) # Coloca a imagem de fundo do jogo na tela 
        
        self.characterGroup.draw(self.screen) # Coloca o personagem na tela
        self.characterGroup.update() # Chama o método de atualizar o personagem

        self.BulletGroup.draw(self.screen) # Coloca as balas na tela
        self.BulletGroup.update() # Chama o método de atualizar as balas

        self.enemyGroup.draw(self.screen) # Coloca os inimigos na tela
        self.enemyGroup.update() # Chama o método de atualizar os inimigos