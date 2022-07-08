from itens.coletaveis import Coletaveis
import random

#FIXME: pq nome para o item??
nome = "jasmin"

largura_jasmin = 15
altura_jasmin = 10

# coordenadas aleatórias do girassol
'''coordenadax_jasmin = random.randint(0, 1000) #TODO: restringir p/ terreno terrestre
coordenaday_jasmin = random.randint(0, 700) #TODO: restringir p/ terreno terrestre'''

peso_jasmin = 1
rosa = (255, 0, 132)


class Jasmin(Coletaveis):
    def __init__(self,coordenadax,coordenaday):
        super().__init__(nome, largura_jasmin, altura_jasmin,
                         coordenadax, coordenaday, peso_jasmin, rosa)
