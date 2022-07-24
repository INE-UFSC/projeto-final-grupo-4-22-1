

class Pontuacao():
    def __init__(self, tempo, nivel):
        self.__flores_entregues = []
        self.__tempo = tempo
        self.__nivel = nivel

    @property
    def flores_entregues(self):
        return self.__flores_entregues
    
    @property
    def tempo(self):
        return self.__tempo

    @property
    def nivel(self):
        return self.__nivel
    