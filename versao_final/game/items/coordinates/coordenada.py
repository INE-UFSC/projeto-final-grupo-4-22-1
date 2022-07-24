import random

from game.items.coordinates.distancia import Distancia


class Coordenada():
    def __init__(self, coordenadax, coordenaday):
        self.__coordenadax = coordenadax
        self.__coordenaday = coordenaday
        self.__dict_coordenadas = {'coletavel': [], 'consumivel': []}


    @property
    def coordenadax(self):
        return self.__coordenadax

    @property
    def coordenaday(self):
        return self.__coordenaday

    @property
    def dict_coordenadadas(self):
        return self.__dict_coordenadas

    def coordenadas(self, tipo_item):
        while True:
            self.__coordenadax = random.randint(0, 1000)
            self.__coordenaday = random.randint(0, 700)
            tuplacoordenada = (self.__coordenadax, self.__coordenaday)
            
            if tipo_item == 'consumivel' and tuplacoordenada not in self.__dict_coordenadas['coletavel']:
                distancia = Distancia(tuplacoordenada, self.__dict_coordenadas['consumivel'])
                if distancia.calcula_distancia(200):
                    break

            elif tipo_item == 'coletavel' and tuplacoordenada not in self.__dict_coordenadas['consumivel']:
                distancia = Distancia(tuplacoordenada, self.__dict_coordenadas['coletavel'])
                if distancia.calcula_distancia(100):
                    break

        self.__dict_coordenadas[tipo_item].append(tuplacoordenada)
