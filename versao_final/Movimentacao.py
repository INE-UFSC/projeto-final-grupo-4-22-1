import pygame
from sapo import Sapo
from TelaJogo import TelaJogo
from pygame.locals import *
from inimigos.cobra import Cobra
from inimigos.jacare import Jacare
from mapa import Mapa
from bibliotecaImagens import BibliotecaImagens

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
                if event.key == K_LEFT and 0 <= self.__jogador.rect.x:
                    self.__jogador.mover_esquerda()
                if event.key == K_RIGHT and self.__tela.largura - self.__jogador.largura >= self.__jogador.rect.x:
                    self.__jogador.mover_direita()
                if event.key == K_UP and 0 <= self.__jogador.rect.y:
                    self.__jogador.mover_cima()
                if event.key == K_DOWN and self.__tela.altura - self.__jogador.altura >= self.__jogador.rect.y:
                    self.__jogador.mover_baixo()

        if pygame.key.get_pressed()[K_LEFT] and 0 <= self.__jogador.rect.x:
            self.__jogador.mover_esquerda()
        if pygame.key.get_pressed()[K_RIGHT] and self.__tela.largura - self.__jogador.largura >= self.__jogador.rect.x:
            self.__jogador.mover_direita()
        if pygame.key.get_pressed()[K_UP] and 0 <= self.__jogador.rect.y:
            self.__jogador.mover_cima()
        if pygame.key.get_pressed()[K_DOWN] and self.__tela.altura - self.__jogador.altura >= self.__jogador.rect.y:
            self.__jogador.mover_baixo()
