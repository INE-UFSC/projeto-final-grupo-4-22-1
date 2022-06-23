from itens.efeitoonus import EfeitoOnus

nome = "espinho"
largura_espinho = 15
altura_espinho = 10
coordenadax_espinho = 15
coordenaday_espinho = 50
onus = 5
cinza = (124,134,153)

class Espinho(EfeitoOnus):
    def __init__(self, nome, largura_espinho, altura_espinho, coordenadax_espinho, coordenaday_espinho, cinza):
        super().__init__(nome, largura_espinho, altura_espinho, coordenadax_espinho, coordenaday_espinho, cinza)
