from itens.coletaveis import Coletaveis
import random

#FIXME: pq nome para o item??
nome = "girassol"

largura_girassol = 20
altura_girassol = 15

# coordenadas aleatórias do girassol
'''coordenadax_girassol = random.randint(0, 1000)
coordenaday_girassol = random.randint(0, 700)'''

peso_girassol = 3
amarelo = (255, 255, 0)


class Girassol(Coletaveis):
    def __init__(self,coordenadax,coordenaday):
        super().__init__(nome, largura_girassol, altura_girassol,
                         coordenadax,coordenaday, peso_girassol, amarelo)
