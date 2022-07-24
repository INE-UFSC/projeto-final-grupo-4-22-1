import pygame
from sapo import Sapo
from TelaJogo import TelaJogo
from pygame.locals import *
from inimigos.cobra import Cobra
from inimigos.jacare import Jacare
from mapa import Mapa
from ImageLibrary import ImageLibrary

class Movimentacao:
    def __init__(self, tela, jogador, mapa):
        self.__tela = tela
        self.__jogador = jogador
        self.__mapa = mapa

    def mover_personagens(self):
        self.mover_jogador()
        self.mover_inimigos()

    def mover_inimigos(self):
        for inimigo in self.__mapa.lista_inimigos:
            inimigo.movimentar(self.__jogador.rect.x,self.__jogador.rect.y)

    def mover_jogador(self):
        for event in self.__tela.ler():
            if event.type == pygame.QUIT:
                self.__tela.fechar()
            if event.type == pygame.KEYDOWN:
                if event.key == K_LEFT:
                    self.__jogador.mover_esquerda()
                    self.__jogador.direcao_horizontal = -1
                elif event.key == K_RIGHT:
                    self.__jogador.mover_direita()
                    self.__jogador.direcao_horizontal = 1
                else:
                    self.__jogador.direcao_horizontal = 0
                if event.key == K_UP:
                    self.__jogador.mover_cima()
                    self.__jogador.direcao_vertical = 1
                elif event.key == K_DOWN:
                    self.__jogador.direcao_vertical = -1
                    self.__jogador.mover_baixo()
                else:
                    self.__jogador.direcao_vertical = 0

        if pygame.key.get_pressed()[K_LEFT]:
            self.__jogador.mover_esquerda()
            self.__jogador.direcao_horizontal = -1
        elif pygame.key.get_pressed()[K_RIGHT]:
            self.__jogador.mover_direita()
            self.__jogador.direcao_horizontal = 1
        else:
            self.__jogador.direcao_horizontal = 0
        if pygame.key.get_pressed()[K_UP]:
            self.__jogador.mover_cima()
            self.__jogador.direcao_vertical = 1
        elif pygame.key.get_pressed()[K_DOWN]:
            self.__jogador.mover_baixo()
            self.__jogador.direcao_vertical = -1
        else:
            self.__jogador.direcao_vertical = 0
