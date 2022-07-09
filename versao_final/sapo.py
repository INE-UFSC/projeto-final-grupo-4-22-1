from player import Player
import pygame

PRETO = (0,0,0)

class Sapo(Player):
    def __init__(self, altura_do_sapo:int, largura_do_sapo:int, vidas_do_sapo:int, coordenadax_sapo:int, coordenaday_sapo:int, velocidade_do_sapo:int):
        super().__init__(altura_do_sapo, largura_do_sapo, vidas_do_sapo, coordenadax_sapo, coordenaday_sapo, velocidade_do_sapo, PRETO)
        self.__flores_coletadas = {}

    def soltar_flores(self):
        self.__flores_coletadas = {}

    @property
    def flores_coletadas(self):
        return self.__flores_coletadas

    @flores_coletadas.setter
    def flores_coletadas(self, flores_coletadas):
        self.__flores_coletadas = flores_coletadas
