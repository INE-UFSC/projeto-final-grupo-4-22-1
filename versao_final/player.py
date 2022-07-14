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
        if self.__velocidade - v > 1:
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
    
    def debuff(self):
        self.__velocidade = self.__velocidade*(-1)
    
    def alterar_velocidade(self, fator_alteracao):
        self.__velocidade = self.__velocidade*fator_alteracao
    


    def mover_cima(self):
        self.rect.y += (-self.velocidade)

    def mover_baixo(self):
        self.rect.y += (self.velocidade)

    def mover_esquerda(self):
        self.rect.x += (-self.velocidade)

    def mover_direita(self):
        self.rect.x += (self.velocidade)
