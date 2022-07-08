from itens.efeitobonus import EfeitoBonus
import random

nome = "maca"
largura_maca = 15
altura_maca = 10
#coordenadax_maca = 15
#coordenaday_maca = 50
bonus = 5
vermelho = (255, 0, 0)


class Maca(EfeitoBonus):
    def __init__(self,coordenadax,coordenaday):
        super().__init__(nome, largura_maca, altura_maca,
                         coordenadax,coordenaday, bonus, vermelho)
