from cmath import rect
from inimigos.inimigo import Inimigo
import pygame
import random

VERDE_ESCURO = (0, 100, 0)

class Jacare(Inimigo):
    def __init__(self,altura_jacare:int, largura_jacare:int, coordenadax_jacare:int, coordenaday_jacare:int, velocidade_jacare:int, dano:int, terreno:str):
        super().__init__(altura_jacare, largura_jacare, coordenadax_jacare, coordenaday_jacare, velocidade_jacare, dano, terreno, VERDE_ESCURO)
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
   
    def movimento(self, distancia:int):
        imagem = 0
        if self.counter >= 0 and self.counter <= distancia and self.rect.x <= 600:
               self.rect.x += self.velocidade
        elif self.counter >= distancia and self.counter <= distancia*4 and self.rect.y <= 500:
            self.rect.y += self.velocidade
            imagem = 1
        elif self.counter >= distancia*4 and self.counter <= distancia*5 and self.rect.x >= 500:
            self.rect.x -= self.velocidade
            imagem = 2   
        elif self.counter >= distancia*5 and self.counter <= distancia*8 and self.rect.y>=0:
            self.rect.y -= self.velocidade
            imagem = 3
        else:
            self.counter = random.randint(0,80)
            
        self.counter += 1
        self.atualiza(imagem)
    
    def atualiza(self,imagem):
        if(imagem == 0):
            self.tamanho_ponto("Imagens/jacare_direita.png",self.altura,self.largura, self.rect.x,self.rect.y)
        elif(imagem == 1):
            self.tamanho_ponto("Imagens/jacare_baixo.png",self.altura,self.largura, self.rect.x,self.rect.y)
        elif(imagem == 2):
            self.tamanho_ponto("Imagens/jacare_esquerda.png",self.altura,self.largura, self.rect.x,self.rect.y)
        elif(imagem == 3):
            self.tamanho_ponto("Imagens/jacare_cima.png",self.altura,self.largura, self.rect.x,self.rect.y)
    
    def tamanho_ponto(self, imagem,altura,largura, x, y):
        imagem = pygame.image.load(imagem)
        imagem = pygame.transform.scale(imagem,(altura,largura))
        self.display.blit(imagem, (x, y))
