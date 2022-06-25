from inimigos.inimigo import Inimigo
from TelaJogo import TelaJogo
import pygame

VERMELHO = 	(139, 0, 0)                      

class Cobra(Inimigo):
    def __init__(self,altura_cobra:int, largura_cobra:int, coordenadax:int, coordenaday_cobra:int, velocidade_cobra:int, dano:int, terreno:str):
        super().__init__(altura_cobra, largura_cobra, coordenadax, coordenaday_cobra, velocidade_cobra, dano, terreno, VERMELHO)
        self.__counter = 0
        #teste 
        self.__width = 1200
        self.__height = 600
        self.display = pygame.display.set_mode((self.__width, self.__height))
        
    
    @property
    def counter(self):
        return self.__counter
    
    @counter.setter
    def counter(self, counter):
        self.__counter = counter

#falta extensão para o eixo Y
#pensando em passar função para controller discutir com o grupo
#rotação de imagem quando implementar eixo Y    
    def movimento(self):
        distance = 50

        if self.counter >= 0 and self.counter <= distance:
               self.rect.x += self.velocidade
        elif self.counter >= distance and self.counter <= distance*2:
            self.rect.x -= self.velocidade
        else:
            self.counter = 0
            
        self.counter += 1
        self.atualiza()
        print(self.rect.x)
    
    def atualiza(self):
        self.tamanho_ponto("prototipo\Imagens\cobra_teste.png",self.altura,self.largura, self.rect.x,self.coordenaday)
    
    def tamanho_ponto(self, imagem,altura,largura, x, y):
        imagem = pygame.image.load(imagem)
        imagem = pygame.transform.scale(imagem,(altura,largura))
        self.display.blit(imagem, (x, y))