import random, math
from abc import ABC
from game.GameScreen import GameScreen
from game.character.Character import Character

class Enemy(Character, ABC):
    def __init__(self, altura, largura, coordenadax, coordenaday, velocidade, dano, terreno):
        super().__init__(altura, largura, coordenadax, coordenaday)
        self.__dano = dano
        self.__terreno = terreno
        self.__velocidade = velocidade
        self.__counter = 0
        self.__screen = GameScreen()

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
    
    def set_counter(self, counter):
        self.__counter = counter
    
    def mover_cima(self):
        self.set_direction_y(1)
        self.rect.y -= self.velocidade

    def mover_baixo(self):
        self.set_direction_y(-1)
        self.rect.y += self.velocidade

    def mover_esquerda(self):
        self.set_direction_x(-1)
        self.rect.x -= self.velocidade

    def mover_direita(self):
        self.set_direction_x(1)
        self.rect.x += self.velocidade
        

    def movimento(self, player_position):
        imagem = 0
        distance_from_player = self.distancia_ponto(player_position, self.rect.x, self.rect.y)

        if distance_from_player <= 200:
            if self.rect.x <= player_position[0]:
                self.mover_direita()
                imagem = 0

            elif self.rect.x > player_position[0]:
                self.mover_esquerda()
                imagem = 2

            if self.rect.y <= player_position[1]:
                self.mover_baixo()
                imagem = 1

            elif self.rect.y >  player_position[1]:
                self.mover_cima()
                imagem = 3
        
        if self.counter == 1:
            imagem = 0
            self.mover_direita()
            
        elif self.counter == 3:
            imagem = 2
            self.mover_esquerda()

        elif self.counter == 4:
            imagem = 1
            self.mover_baixo()

        elif self.counter == 2:
            imagem = 3
            self.mover_cima()

        else:
            self.__counter = random.randint(1, 4)

        #self.counter += 1
        return imagem


    def atualiza(self, imagem, direita, baixo, esquerda, cima):
        if(imagem == 0):
            self.__screen.tamanho_ponto(direita,self.altura,self.largura, self.rect.x,self.rect.y)
        elif(imagem == 1):
            self.__screen.tamanho_ponto(baixo,self.altura,self.largura, self.rect.x,self.rect.y)
        elif(imagem == 2):
            self.__screen.tamanho_ponto(esquerda,self.altura,self.largura, self.rect.x,self.rect.y)
        elif(imagem == 3):
            self.__screen.tamanho_ponto(cima,self.altura,self.largura, self.rect.x,self.rect.y)
    

    def distancia_ponto(self, player_position,inimigox,inimigoy):
        distancia = math.sqrt((inimigox-player_position[0])**2+(inimigoy-player_position[1])**2)
        return distancia
