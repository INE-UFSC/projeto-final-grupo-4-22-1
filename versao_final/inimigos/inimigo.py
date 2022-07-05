from personagem import Personagem

class Inimigo(Personagem):
    def __init__(self, altura, largura, coordenadax, coordenaday, velocidade, dano, terreno, COR):
        super().__init__(altura, largura, coordenadax, coordenaday, COR)
        self.__dano = dano
        self.__terreno = terreno
        self.__velocidade = velocidade

    @property
    def dano(self):
        return self.__dano
    
    @property
    def terreno(self):
        return self.__terreno

    @property
    def velocidade(self):
        return self.__velocidade
    
    def carry(self, v):
        if self.__velocidade > 1:
            if v:
                self.__velocidade -= v
            else:
                self.__velocidade -= 1
