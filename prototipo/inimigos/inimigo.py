from personagem import Personagem

class Inimigo(Personagem):
    def __init__(self, altura, largura, coordenadax, coordenaday, velocidade, dano, terreno, COR):
        super().__init__(altura, largura, coordenadax, coordenaday, velocidade, COR)
        self.__dano = dano
        self.__terreno = terreno

    @property
    def dano(self):
        return self.__dano
    
    @property
    def terreno(self):
        return self.__terreno
