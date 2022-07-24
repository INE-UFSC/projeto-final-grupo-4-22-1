class Distancia:
    def __init__(self, coordenada, lista_coordenadas):
        self.__coordenada = coordenada
        self.__lista_coordenadas = lista_coordenadas
    
    def calcula_distancia(self, distancia_max):
        for item in self.__lista_coordenadas:
            distancia = ((item[0] - self.__coordenada[0])**2 + (item[1] - self.__coordenada[1])**2)**.5
            
            if int(distancia) < distancia_max:
                return False

        return True
        
