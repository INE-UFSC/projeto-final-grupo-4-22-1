from inimigos.inimigo import Inimigo
import pygame

altura_cobra = 50
largura_cobra = 30
coordenadax_cobra = 200
coordenaday_cobra = 200
velocidade_cobra = 5
dano = 2
terreno = 'terrestre'
VERMELHO = 	(139, 0, 0)
caminho = [[240, 150],[240, 450],[360, 450],[360, 150]]
                      

class Cobra(Inimigo):
    def __init__(self):
        super().__init__(altura_cobra, largura_cobra, coordenadax_cobra, coordenaday_cobra, velocidade_cobra, dano, terreno, VERMELHO)
        self.__caminho = caminho

    #def mudaCoord(self,nCaminho):

    def calculaDistancia(self, coordenax, coordenay):
        return ((self.coordenadax - coordenax)**2 + (self.coordenaday - coordenay)**2)**0.5
    
    """@staticmethod
    def versorEntreCoordenadas(coordX0, coordY0,coordX1, coordY1):
        x = coordX1 - coordX0
        y = coordY1 - coordY0
        modulo = (x**2 + y**2)**0.5
        if modulo == 0:
            return (0,0)
        else:
            return (x/modulo, y/modulo)"""