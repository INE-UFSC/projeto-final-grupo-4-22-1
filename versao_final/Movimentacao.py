import pygame
from sapo import Sapo
from TelaJogo import TelaJogo
from pygame.locals import *
from inimigos.cobra import Cobra
from inimigos.jacare import Jacare
from mapa import Mapa

class Movimentacao:
    def __init__(self, tela, jogador, mapa):
        self.__tela = tela
        self.__jogador = jogador
        self.__mapa = mapa

    def mover_personagens(self):
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

        for cobra in self.__mapa.lista_cobras:
            distancia_cobra = cobra.distancia_ponto(self.__jogador.rect.x,self.__jogador.rect.y,cobra.rect.x,cobra.rect.y)
            cobra.movimento(50,2,3,300,550,100,20,250,"Imagens/cobra_direita.png","Imagens/cobra_baixo.png","Imagens/cobra_esquerda.png","Imagens/cobra_cima.png",distancia_cobra,self.__jogador.rect.x,self.__jogador.rect.y)

        for jacare in self.__mapa.lista_jacares:
            distancia_jacare = jacare.distancia_ponto(self.__jogador.rect.x,self.__jogador.rect.y,jacare.rect.x,jacare.rect.y)
            jacare.movimento(15,4,5,600,500,500,0,80,"Imagens/jacare_direita.png","Imagens/jacare_baixo.png","Imagens/jacare_esquerda.png","Imagens/jacare_cima.png",distancia_jacare,self.__jogador.rect.x,self.__jogador.rect.y)
