from cmath import rect

from game.character.enemies.Enemy import Enemy
from game.imageLibrary.ImageLibrary import ImageLibrary


class Jacare(Enemy):
    def __init__(self, altura_jacare:int, largura_jacare:int, coordenadax_jacare:int, coordenaday_jacare:int, velocidade_jacare:int, dano:int, terreno:str):
        super().__init__(altura_jacare, largura_jacare, coordenadax_jacare, coordenaday_jacare, 2, dano, terreno)
        self.__imagens = ImageLibrary()
        self.__imagens = [self.__imagens.jacare_direita,self.__imagens.jacare_baixo,self.__imagens.jacare_esquerda,self.__imagens.jacare_cima]
    
    
    def movimentar(self, player_position):
        movimento_jacare = self.movimento(player_position)
        self.atualiza(movimento_jacare,self.__imagens[0],self.__imagens[1],self.__imagens[2],self.__imagens[3])
    
    
