from itens.efeitoonus import EfeitoOnus
import random

# coordenadas aleatórias do espinho
coordenadax_espinho = random.randint(0, 1000)
coordenaday_espinho = random.randint(0, 700)
marrom = (75, 54, 33)

class Espinho(EfeitoOnus):
    def __init__(self,coordenadax,coordenaday):
        super().__init__("espinho", 15, 10, coordenadax, coordenaday, -5, marrom)
