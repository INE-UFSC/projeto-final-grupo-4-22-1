from player import Player
import pygame

class ConsequenciasColisoes:
    def __init__(self, jogador):
        self.__jogador = jogador

    def jogador_e_inimigo(self):
        return "Perdeu!"

    def jogador_e_parceiro(self):
        for flor in self.__jogador.flores_coletadas:
            if self.__jogador.flores_coletadas[flor] == True:
                self.__jogador.aumenta_velocidade(flor.peso)
        self.__jogador.soltar_flores()

    def jogador_e_item(self, item):
        item.aplicar_efeito(self.__jogador)

    def jogador_e_flor(self, flor):
        self.__jogador.flores_coletadas[flor] = self.__jogador.carry(flor.peso)

    def jogador_e_water(self):
        self.__jogador.velocidade = 3

    def jogador_e_barreira_x(self, tile):
        if self.__jogador.direcao_horizontal == -1:
            self.__jogador.rect.x = tile.right
        elif self.__jogador.direcao_horizontal == 1:
            self.__jogador.rect.x = tile.left - self.__jogador.rect.w

    def jogador_e_barreira_y(self, tile):
        if self.__jogador.direcao_vertical == 1:
            self.__jogador.rect.y = tile.bottom
        elif self.__jogador.direcao_vertical == -1:
            self.__jogador.rect.bottom = tile.top - self.__jogador.rect.h
