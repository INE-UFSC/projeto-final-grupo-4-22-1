import pygame
from pygame.locals import *


class Movimentacao:
    def __init__(self, tela, jogador, mapa):
        self.__tela = tela
        self.__jogador = jogador
        self.__mapa = mapa

    def mover_personagens(self):
        self.mover_jogador()
        self.mover_inimigos()

    def mover_inimigos(self):
        for inimigo in self.__mapa.enimies:
            inimigo.movimentar((self.__jogador.rect.x, self.__jogador.rect.y))

    def mover_jogador(self):
        for event in self.__tela.ler():
            if event.type == pygame.QUIT:
                self.__tela.fechar()

            else:
                self.__jogador.stopped()

        if pygame.key.get_pressed()[K_LEFT]:
            self.__jogador.mover_esquerda()

        elif pygame.key.get_pressed()[K_RIGHT]:
            self.__jogador.mover_direita()

        elif pygame.key.get_pressed()[K_UP]:
            self.__jogador.mover_cima()

        elif pygame.key.get_pressed()[K_DOWN]:
            self.__jogador.mover_baixo()

        else:
            self.__jogador.stopped()
