from itens.efeitobonus import EfeitoBonus
import random

#coordenadax_maca = 15
#coordenaday_maca = 50
vermelho = (255, 0, 0)


class Maca(EfeitoBonus):
    def __init__(self,coordenadax,coordenaday):
        super().__init__("maca", 15, 10,
                         coordenadax,coordenaday, 5, vermelho)
