import random, pygame, math

from game.GameScreen import GameScreen
from game.character.Character import Character

class Enemy(Character):
    def __init__(self, altura, largura, coordenadax, coordenaday, velocidade, dano, terreno):
        super().__init__(altura, largura, coordenadax, coordenaday, (0,0,0))
        self.__dano = dano
        self.__terreno = terreno
        self.__velocidade = velocidade
        self.__counter = 0
        self.__screen = GameScreen(self)

    @property
    def dano(self):
        return self.__dano
    
    @property
    def terreno(self):
        return self.__terreno

    @property
    def velocidade(self):
        return self.__velocidade
    
    @property
    def counter(self):
        return self.__counter
    
    @counter.setter
    def counter(self, counter):
        self.__counter = counter


    def movimento(self, distancia,distanciax,distanciay,delimitaxd,delimitayb,delimitaxe,delimitayc,aleatoriedade,SapoPosicaox,SapoPosicaoy):
        imagem = 0
        raio = self.distancia_ponto(SapoPosicaox,SapoPosicaoy,self.rect.x,self.rect.y)
        if(self.rect.x <= delimitaxd and self.rect.y <= delimitayb and self.rect.x >= delimitaxe and self.rect.y >= delimitayc and raio <= 200):
            if self.rect.x <= SapoPosicaox and self.rect.y <= SapoPosicaoy:
                self.rect.x += self.velocidade
                self.rect.y += self.velocidade
                imagem = 1
            elif self.rect.x <= SapoPosicaox and self.rect.y >  SapoPosicaoy:
                self.rect.x += self.velocidade
                self.rect.y -= self.velocidade
            elif self.rect.x > SapoPosicaox and self.rect.y <=  SapoPosicaoy:
                self.rect.x -= self.velocidade
                self.rect.y += self.velocidade
                imagem = 2
            elif self.rect.x > SapoPosicaox and self.rect.y >  SapoPosicaoy:
                self.rect.x -= self.velocidade
                self.rect.y -= self.velocidade
                imagem = 3

        elif self.counter >= 0 and self.counter <= distancia :
            self.rect.x += self.velocidade

        elif self.counter >= distancia and self.counter <= distancia*distanciax :
            self.rect.y += self.velocidade
            imagem = 1

        elif self.counter >= distancia*distanciax and self.counter <= distancia*distanciay :
            self.rect.x -= self.velocidade
            imagem = 2

        elif self.counter >= distancia*distanciay and self.counter <= distancia*distanciax*2 :
            self.rect.y -= self.velocidade
            imagem = 3

        else:
            self.counter = random.randint(0,aleatoriedade)
        self.counter += 1
        return imagem


    def atualiza(self,imagem,direita,baixo,esquerda,cima):
        if(imagem == 0):
            self.__screen.tamanho_ponto(direita,self.altura,self.largura, self.rect.x,self.rect.y)
        elif(imagem == 1):
            self.__screen.tamanho_ponto(baixo,self.altura,self.largura, self.rect.x,self.rect.y)
        elif(imagem == 2):
            self.__screen.tamanho_ponto(esquerda,self.altura,self.largura, self.rect.x,self.rect.y)
        elif(imagem == 3):
            self.__screen.tamanho_ponto(cima,self.altura,self.largura, self.rect.x,self.rect.y)
    

    def distancia_ponto(self,sapox,sapoy,inimigox,inimigoy):
        distancia = math.sqrt((inimigox-sapox)**2+(inimigoy-sapoy)**2)
        return distancia
