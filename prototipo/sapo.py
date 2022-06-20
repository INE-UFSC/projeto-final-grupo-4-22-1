from player import Player

altura_do_sapo = 30
largura_do_sapo = 30
vidas_do_sapo = 3
coordenadax_sapo = 30
coordenaday_sapo = 30
velocidade_do_sapo = 12

class Sapo(Player):
    def __init__(self):
        super().__init__(altura_do_sapo, largura_do_sapo, vidas_do_sapo, coordenadax_sapo, coordenaday_sapo, velocidade_do_sapo)
