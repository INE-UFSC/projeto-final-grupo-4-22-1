from inimigos.inimigo import Inimigo
from bibliotecaImagens import BibliotecaImagens

VERMELHO = 	(139, 0, 0)                      

class Cobra(Inimigo):
    def __init__(self,altura_cobra:int, largura_cobra:int, coordenadax:int, coordenaday_cobra:int, velocidade_cobra:int, dano:int, terreno:str):
        super().__init__(altura_cobra, largura_cobra, coordenadax, coordenaday_cobra, velocidade_cobra, dano, terreno, VERMELHO)
        self.__imagens = BibliotecaImagens()
        self.__imagens = [self.__imagens.cobra_direita,self.__imagens.cobra_baixo,self.__imagens.cobra_esquerda,self.__imagens.cobra_cima]
        
    def movimento_cobra(self):
        movimento_cobra = self.movimento(50,2,3,300,550,100,20,250,self.__imagens[0],self.__imagens[1],self.__imagens[2],self.__imagens[3])
        return movimento_cobra
        
    
    


