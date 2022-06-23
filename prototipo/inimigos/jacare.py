from inimigos.inimigo import Inimigo

altura_jacare = 70
largura_jacare = 40
coordenadax_jacare = 150
coordenaday_jacare = 190
velocidade_jacare = 5
dano = 3
terreno = 'aquatico'

class Jacare(Inimigo):
    def __init__(self):
        super().__init__(altura_jacare, largura_jacare, coordenadax_jacare, coordenaday_jacare, velocidade_jacare, dano, terreno)
