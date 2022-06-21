from TelaJogo import TelaJogo
import pygame
from pygame.locals import *
from sapo import Sapo
from inimigos.cobra import Cobra
from inimigos.jacare import Jacare

class GameController:
    def __init__(self):
        self.__tela = TelaJogo(self)
        self.__clock = pygame.time.Clock()

    def iniciar(self):
        jogador = Sapo()
        cobra = Cobra()
        jacare = Jacare()
        self.__tela.iniciar()
        rodando = True
        while rodando:
            self.__clock.tick(40)
            self.__tela.colorir()
            self.__tela.desenhar(jogador, cobra, jacare)
            for event in self.__tela.ler():
                if event.type == pygame.QUIT:
                    self.__tela.fechar()
                if event.type == pygame.KEYDOWN:
                    if event.key == K_LEFT and 0 <= jogador.coordenadax:
                        jogador.moverx(-jogador.velocidade)
                    if event.key == K_RIGHT and self.__tela.largura - jogador.largura >= jogador.coordenadax:
                        jogador.moverx(jogador.velocidade)
                    if event.key == K_UP and 0 <= jogador.coordenaday:
                        jogador.movery(-jogador.velocidade)
                    if event.key == K_DOWN and self.__tela.altura - jogador.altura >= jogador.coordenaday:
                        jogador.movery(jogador.velocidade)
            if pygame.key.get_pressed()[K_LEFT] and 0 <= jogador.coordenadax:
                jogador.moverx(-jogador.velocidade)
            if pygame.key.get_pressed()[K_RIGHT] and self.__tela.largura - jogador.largura >= jogador.coordenadax:
                jogador.moverx(jogador.velocidade)
            if pygame.key.get_pressed()[K_UP] and 0 <= jogador.coordenaday:
                jogador.movery(-jogador.velocidade)
            if pygame.key.get_pressed()[K_DOWN] and self.__tela.altura - jogador.altura >= jogador.coordenaday:
                jogador.movery(jogador.velocidade)
            self.__tela.update()
