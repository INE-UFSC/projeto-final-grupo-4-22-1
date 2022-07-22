from cmath import rect
from inimigos.inimigo import Inimigo
from ImageLibrary import ImageLibrary
VERDE_ESCURO = (0, 100, 0)

class Jacare(Inimigo):
    def __init__(self,altura_jacare:int, largura_jacare:int, coordenadax_jacare:int, coordenaday_jacare:int, velocidade_jacare:int, dano:int, terreno:str):
        super().__init__(altura_jacare, largura_jacare, coordenadax_jacare, coordenaday_jacare, velocidade_jacare, dano, terreno, VERDE_ESCURO)
        self.__imagens = ImageLibrary()
        self.__imagens = [self.__imagens.jacare_direita,self.__imagens.jacare_baixo,self.__imagens.jacare_esquerda,self.__imagens.jacare_cima]
    
    
    def movimentar(self,SapoPosicaox,SapoPosicaoy):
        movimento_jacare = self.movimento(15,4,5,600,500,500,0,80,SapoPosicaox,SapoPosicaoy)
        self.atualiza(movimento_jacare,self.__imagens[0],self.__imagens[1],self.__imagens[2],self.__imagens[3])
    
    