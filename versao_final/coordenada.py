import random


class Coordenada():
    def __init__(self, coordenadax, coordenaday,raio_distanciamento):
        self.__coordenadax = coordenadax
        self.__coordenaday = coordenaday
        self.__raio_distanciamento = raio_distanciamento
        self.__lista_coordenadas = []
        self.__dict_coordenadas = {}


    @property
    def coordenadax(self):
        return self.__coordenadax

    @property
    def coordenaday(self):
        return self.__coordenaday

    @property
    def lista_coordenadadas(self):
        return self.__lista_coordenadas

    def coordenadas(self):
        while True:
            self.__coordenadax = random.randint(0, 1000)
            self.__coordenaday = random.randint(0, 700)
            tuplacoordenada = (self.__coordenadax, self.__coordenaday)
            v = tuplacoordenada in self.__lista_coordenadas
            if v == False:
                self.__lista_coordenadas.append(tuplacoordenada)
                break


