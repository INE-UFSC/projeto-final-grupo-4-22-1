from inimigos.inimigo import Inimigo
from TelaJogo import TelaJogo
import pygame
import random

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
    def movimento(self, distancia:int):
        imagem = 0
        if self.counter >= 0 and self.counter <= distancia and self.rect.x <= 300:
            self.rect.x += self.velocidade
        elif self.counter >= distancia and self.counter <= distancia*2.5 and self.rect.y <= 550:
            self.rect.y += self.velocidade
            imagem = 1
        elif self.counter >= distancia*2.5 and self.counter <= distancia*3.5 and self.rect.x >= 100:
            self.rect.x -= self.velocidade
            imagem = 2
        elif self.counter >= distancia*3.5 and self.counter <= distancia*5 and self.rect.y >= 20:
            self.rect.y -= self.velocidade
            imagem = 3
        else:
            self.counter = random.randint(0,250)
            
        self.counter += 1
        self.atualiza(imagem)

    def atualiza(self,imagem):
        if(imagem == 0):
            self.tamanho_ponto("prototipo/Imagens/cobra_direita.png",self.altura,self.largura, self.rect.x,self.rect.y)
        elif(imagem == 1):
            self.tamanho_ponto("prototipo/Imagens/cobra_baixo.png",self.altura,self.largura, self.rect.x,self.rect.y)
        elif(imagem == 2):
            self.tamanho_ponto("prototipo/Imagens/cobra_esquerda.png",self.altura,self.largura, self.rect.x,self.rect.y)
        elif(imagem == 3):
            self.tamanho_ponto("prototipo/Imagens/cobra_cima.png",self.altura,self.largura, self.rect.x,self.rect.y)
    
    
    
    def tamanho_ponto(self, imagem,altura,largura, x, y):
        imagem = pygame.image.load(imagem)
        imagem = pygame.transform.scale(imagem,(altura,largura))
        self.display.blit(imagem, (x, y))
