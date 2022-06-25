from inimigos.inimigo import Inimigo
from TelaJogo import TelaJogo
import pygame

VERMELHO = 	(139, 0, 0)                      

class Cobra(Inimigo):
    def __init__(self,altura_cobra:int, largura_cobra:int, coordenadax:int, coordenaday_cobra:int, velocidade_cobra:int, dano:int, terreno:str):
        super().__init__(altura_cobra, largura_cobra, coordenadax, coordenaday_cobra, velocidade_cobra, dano, terreno, VERMELHO)
        self.__counter = 0
        self.__tela = TelaJogo(self)
    
    @property
    def counter(self):
        return self.__counter
    
    @counter.setter
    def counter(self, counter):
        self.__counter = counter

    def movimento(self):
        distance = 400

        if self.counter >= 0 and self.counter <= distance:
               self.coordenadax += self.velocidade
        elif self.counter >= distance and self.counter <= distance*2:
            self.coordenadax -= self.velocidade
        else:
            self.counter = 0
            
        self.counter += 1
        print(self.coordenadax)