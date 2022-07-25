from game.character.Character import Character

class Player(Character):
    def __init__(self, altura, largura, vida, coordenadax, coordenaday, velocidade, COR):
        super().__init__(altura, largura, coordenadax, coordenaday, COR)
        self.__vida = vida
        self.__velocidade_inicial = velocidade
        self.__velocidade = velocidade
        self.__flores = []
        self.__envenenado = False

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
    
    @property
    def flores(self):
        return self.__flores

    @flores.setter
    def flores(self, flor):
        self.__flores.append(flor)

    def debuff(self):
        self.__velocidade = self.__velocidade*(-1)
    
    def alterar_velocidade(self, fator_alteracao):
        self.__velocidade = self.__velocidade*fator_alteracao

    def mover_cima(self):
        self.set_direction_y(1)
        self.rect.y += (-self.velocidade)

    def mover_baixo(self):
        self.set_direction_y(-1)
        self.rect.y += (self.velocidade)

    def mover_esquerda(self):
        self.set_direction_x(-1)
        self.rect.x += (-self.velocidade)

    def mover_direita(self):
        self.set_direction_x(1)
        self.rect.x += (self.velocidade)

    def stopped(self):
        self.set_direction_x(0)
        self.set_direction_y(0)

    @velocidade.setter
    def velocidade(self, velocidade):
        self.__velocidade = velocidade

    @property
    def velocidade_inicial(self):
        return self.__velocidade_inicial
