from itens.coletaveis import Coletaveis
#from random import randint

nome = "jasmin"  # pq nome para o item??
largura_jasmin = 15
altura_jasmin = 10
coordenadax_jasmin = 100  # randomizar coordenadas para aparecimento do girassol
coordenaday_jasmin = 50
peso_jasmin = 1


class Girassol(Coletaveis):
    def __init__(self):
        super().__init__(nome, largura_jasmin, altura_jasmin,
                         coordenadax_jasmin, coordenaday_jasmin, peso_jasmin)
