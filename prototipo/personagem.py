
class Personagem:
    def __init__(self, altura, largura, coordenadax, coordenaday, velocidade):
        self.__altura = altura
        self.__largura = largura
        self.__coordenadax = coordenadax
        self.__coordenaday = coordenaday
        self.__velocidade = velocidade

    @property
    def altura(self):
        return self.__altura
    
    @property
    def largura(self):
        return self.__largura

    @property
    def coordenadax(self):
        return self.__coordenadax

    @property
    def coordenaday(self):
        return self.__coordenaday

    @property
    def velocidade(self):
        return self.__velocidade

    def moverx(self, velocidade):
        self.__coordenadax += velocidade

    def movery(self, velocidade):
        self.__coordenaday += velocidade
