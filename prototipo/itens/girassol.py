from itens.coletaveis import Coletaveis
#from random import randint

nome = "girassol"  # pq nome para o item??
largura_girassol = 20
altura_girassol = 15
coordenadax_girassol = 150  # randomizar coordenadas para aparecimento do girassol
coordenaday_girassol = 130
peso_girassol = 3


class Girassol(Coletaveis):
    def __init__(self):
        super().__init__(nome, largura_girassol, altura_girassol,
                         coordenadax_girassol, coordenaday_girassol, peso_girassol)
