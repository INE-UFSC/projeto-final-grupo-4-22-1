from personagem import Personagem

class Player(Personagem):
    def __init__(self, altura, largura, vida, coordenadax, coordenaday, velocidade):
        super().__init__(altura, largura, coordenadax, coordenaday, velocidade)
        self.__vida = vida

    @property
    def vida(self):
        return self.__vida
