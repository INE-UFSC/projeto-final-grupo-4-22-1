from itens.efeitoonus import EfeitoOnus
import random

# FIXME: pq nome para o item??
nome = "cogumelo"
largura_cogumelo = 15
altura_cogumelo = 10

# coordenadas aleatórias do espinho
coordenadax_cogumelo = random.randint(0, 1000)
coordenaday_cogumelo = random.randint(0, 700)

# onus= ??? Efeito onus do cogumelo inverte os comandos como ficaria o atrubuto onus(??)


cinza = (124, 134, 153)


class Cogumelo(EfeitoOnus):
    def __init__(self, nome, largura_cogumelo, altura_cogumelo, coordenadax_cogumelo, coordenaday_cogumelo, cinza):
        super().__init__(nome, largura_cogumelo, altura_cogumelo,
                         coordenadax_cogumelo, coordenaday_cogumelo, cinza)
