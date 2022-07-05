from cmath import rect
from inimigos.inimigo import Inimigo
VERDE_ESCURO = (0, 100, 0)

class Jacare(Inimigo):
    def __init__(self,altura_jacare:int, largura_jacare:int, coordenadax_jacare:int, coordenaday_jacare:int, velocidade_jacare:int, dano:int, terreno:str):
        super().__init__(altura_jacare, largura_jacare, coordenadax_jacare, coordenaday_jacare, velocidade_jacare, dano, terreno, VERDE_ESCURO)
        
   
   