import pygame
from pygame.locals import *


class Movimentacao:
    def __init__(self, tela, player, mapa):
        self.__tela = tela
        self.__player = player
        self.__mapa = mapa

    def mover_personagens(self):
        self.mover_player()
        self.mover_inimigos()

    def mover_inimigos(self):
        for inimigo in self.__mapa.enemies:
            inimigo.movimentar((self.__player.rect.x, self.__player.rect.y))

    def mover_player(self):
        for event in self.__tela.ler():
            if event.type == pygame.QUIT:
                self.__tela.fechar()

            else:
                self.__player.stopped()

        if pygame.key.get_pressed()[K_LEFT]:
            self.__player.mover_esquerda()

        elif pygame.key.get_pressed()[K_RIGHT]:
            self.__player.mover_direita()

        elif pygame.key.get_pressed()[K_UP]:
            self.__player.mover_cima()

        elif pygame.key.get_pressed()[K_DOWN]:
            self.__player.mover_baixo()

        else:
            self.__player.stopped()
