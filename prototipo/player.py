from personagem import Personagem

class Player(Personagem):
    def __init__(self, altura, largura, vida, coordenadax, coordenaday, velocidade, COR):
        super().__init__(altura, largura, coordenadax, coordenaday, COR)
        self.__vida = vida
        self.__velocidade = velocidade

    @property
    def vida(self):
        return self.__vida
    
    @property
    def velocidade(self):
        return self.__velocidade
    
    def carry(self, v):
        if self.__velocidade > 1:
            if v:
                self.__velocidade -= v
                return True
            else:
                self.__velocidade -= 1
        else:
            return False

    def aumenta_velocidade(self, v):
        if v:
            self.__velocidade += v
        else:
            self.__velocidade += 1
