from pygame.sprite import Sprite
from images.images  import bullet

class Bullet(Sprite): # Herda de Sprite para usar recursos de colisão 
    def __init__(self):
        super().__init__() # Obrigatório para inicializar o construtor da classe pai
        self.image = bullet # Cria um atributo com a imagem carregada
        self.rect = self.image.get_rect() # Posiciona e cria a colisão

    def update(self): # Atualiza o objeto a cada loop
        pass
