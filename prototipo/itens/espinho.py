from itens.efeitoonus import EfeitoOnus
import random

#FIXME: pq nome para o item??
nome = "espinho"
largura_espinho = 15
altura_espinho = 10

# coordenadas aleatórias do espinho
coordenadax_espinho = random.randint(0, 1000)
coordenaday_espinho = random.randint(0, 700)
onus = 5
cinza = (124, 134, 153)

class Espinho(EfeitoOnus):
    def __init__(self, nome, largura_espinho, altura_espinho, coordenadax_espinho, coordenaday_espinho, cinza):
        super().__init__(nome, largura_espinho, altura_espinho, coordenadax_espinho, coordenaday_espinho, cinza)
