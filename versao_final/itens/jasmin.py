from itens.coletaveis import Coletaveis
import random

# coordenadas aleatórias do girassol
'''coordenadax_jasmin = random.randint(0, 1000) #TODO: restringir p/ terreno terrestre
coordenaday_jasmin = random.randint(0, 700) #TODO: restringir p/ terreno terrestre'''

rosa = (255, 0, 132)

class Jasmin(Coletaveis):
    def __init__(self,coordenadax,coordenaday):
        super().__init__("jasmin", 15, 10,
                         coordenadax, coordenaday, 1, rosa)
