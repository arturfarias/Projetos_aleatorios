from pygame.sprite import Sprite
from images.images import enemy
from pygame import transform
import random

class Enemy(Sprite): # Herda de Sprite para usar recursos de colisão 
    def __init__(self): 
        super().__init__() # Obrigatório para inicializar o construtor da classe pai
        self.image = transform.scale(enemy, (128,128)) # Ajusta o tamanho da imagem
        self.rect = self.image.get_rect(center=(900,random.randrange(40,550))) # Posiciona e cria a colisão
        self.speed = random.randrange(-10,-3) # Define a velocidade aleatoriamente

    def update(self): # Atualiza o objeto a cada loop
        self.rect = self.rect.move(self.speed,0) # Movimenta a sprite na tela

        if (self.rect.x < -100): # Destrói o objeto quando chegar na posição indicada
            self.kill()