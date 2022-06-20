from inimigo import Inimigo

altura_cobra = 50
largura_cobra = 30
coordenadax_cobra = 80
coordenaday_cobra = 80
velocidade_cobra = 5
dano = 2
terreno = 'terrestre'

class Cobra(Inimigo):
    def __init__(self):
        super().__init__(altura_cobra, largura_cobra, coordenadax_cobra, coordenaday_cobra, velocidade_cobra, dano, terreno)
