from game.character.enemies.Enemy import Enemy
from game.imageLibrary.ImageLibrary import ImageLibrary


class Cobra(Enemy):
    def __init__(self,altura_cobra:int, largura_cobra:int, coordenadax:int, coordenaday_cobra:int, velocidade_cobra:int, dano:int, terreno:str):
        super().__init__(altura_cobra, largura_cobra, coordenadax, coordenaday_cobra, velocidade_cobra, dano, terreno)
        self.__imagens = ImageLibrary()
        self.__imagens = [self.__imagens.cobra_direita,self.__imagens.cobra_baixo,self.__imagens.cobra_esquerda,self.__imagens.cobra_cima]
        

    def movimentar(self, player_position):
        movimento_cobra = self.movimento(player_position)
        self.atualiza(movimento_cobra,self.__imagens[0],self.__imagens[1],self.__imagens[2],self.__imagens[3])

    
