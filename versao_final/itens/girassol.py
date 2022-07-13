from itens.coletaveis import Coletaveis
import random

amarelo = (255, 255, 0)

class Girassol(Coletaveis):
    def __init__(self,coordenadax,coordenaday):
        super().__init__("girassol", 20, 15,
                         coordenadax,coordenaday, 3, amarelo)
