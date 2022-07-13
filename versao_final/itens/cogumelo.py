from itens.efeitoonus import EfeitoOnus
import random

# coordenadas aleatórias do espinho
coordenadax_cogumelo = random.randint(0, 1000)
coordenaday_cogumelo = random.randint(0, 700)

cinza = (124, 134, 153)


class Cogumelo(EfeitoOnus):
    def __init__(self,coordenadax,coordenaday):
        super().__init__("cogumelo", 15, 10,
                         coordenadax,coordenaday, None, cinza)
