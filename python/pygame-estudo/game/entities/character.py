from pygame.sprite import Sprite
from images.images import player
from pygame import transform
from game.events import Events
from pygame.locals import K_w, K_s, K_SPACE

class Character(Sprite): # Herda de Sprite para usar recursos de colisão 
    def __init__(self):
        super().__init__() # Obrigatório para inicializar o construtor da classe pai
        self.events = Events()

        self.image = transform.scale(player, (128,128)) # Ajusta o tamanho da imagem
        self.rect = self.image.get_rect(center=(40,300)) # Posiciona e cria a colisão
    
    def moviment(self): # Método do movimento da nave
        if (self.events.key_pressed(K_w) and self.rect.y > 0): # Verdadeiro se pressionado W e posição maior que 0
            self.rect = self.rect.move(0,-10) # Move a nave
        elif (self.events.key_pressed(K_s) and self.rect.y < 480): # Verdadeiro se pressionado S e posição menor que 480
            self.rect = self.rect.move(0,10) # Move a nave

    def shoot(self):
        if(self.events.key_down(K_SPACE)):# Checa se a tecla foi pressionada 
            print("Disparo") # Placeholder de disparo

    def update(self): # Atualiza o objeto a cada loop
        self.moviment()
        self.shoot()