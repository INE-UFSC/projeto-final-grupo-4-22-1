from operator import index
from TelaJogo import TelaJogo
from ranking import Ranking
import pygame
from pygame.locals import *
from inimigos import Inimigo
from colisoes import Colisoes

from terreno.water import Water
from sapo import Sapo
from ra import Ra

from inimigos.cobra import Cobra
from inimigos.jacare import Jacare
import random

from itens.sunflower import Sunflower
from itens.jasminen import Jasminen
from itens.apple import Apple
from itens.thorm import Thorm
from itens.mushroom import Mushroom

from coordenadas.coordenada import Coordenada
from mapa import Mapa
from input_box import InputBox
from Movimentacao import Movimentacao
#c_flor = Coordenada(0,0,0)
#c_item = Coordenada(0,0,0)

import time
from clock import Clock
from construtorDeFases import ConstrutorDeFases

from Som import Som


# TODO: precisamos verificar se essa combinação de coordenadas que criamos p/ cada item já está sendo usada, pq se já estiver teremos que criar novas coordenadas até todas serem diferentes (isso é no arquivos do item, só deixei  comentário aqui, pq sempre usamos esse arquivo)


class GameController:
    def __init__(self):
        self.__ranking = Ranking()
        self.__mapa = Mapa()
        self.__tela = TelaJogo(self)
        self.__construtor = ConstrutorDeFases(self.__mapa)
        self.__clock = pygame.time.Clock()
        self.__jogador = None
        self.__relogio = Clock()
        self.__teste = False
        self.__som = Som()

    def iniciar_menu(self):
        self.__tela.iniciar()
        self.__usuario = ''
        input_box = InputBox(430,300,140,32)
        menu = True
        #self.__som.iniciar(1)
        while menu:
            self.__tela.menu(input_box)
            for event in self.__tela.ler():
                if event.type == pygame.QUIT:
                    self.__tela.fechar()
                if event.type == pygame.KEYDOWN:
                    if event.key == K_SPACE:
                        self.__usuario = input_box.texto
                        pygame.time.set_timer(pygame.USEREVENT,310)
                        return self.iniciar()
                input_box.handle_event(event)
            self.__tela.update()
            self.__clock.tick(30)

    def iniciar(self):
        self.__jogador = Sapo(30, 30, 3, 300, 300, 7)
        colisoes = Colisoes(self.__mapa, self.__jogador)
        self.__tela.iniciar()
        movimentacao = Movimentacao(self.__tela, self.__jogador, self.__mapa)
        rodando = True
        self.__relogio.iniciar_clock()
        self.__construtor.gerar_fase(2)
        sprites = self.__mapa.all_sprites
        sprites.add(self.__jogador)
        #self.__som.iniciar(0)
        while rodando:
            for event in self.__tela.ler():
                if event.type == pygame.QUIT:
                    self.__tela.fechar()
                elif event.type == pygame.USEREVENT:
                    self.__teste = self.__relogio.verifica_clock()
            if self.__teste == True:
                break
            self.__clock.tick(40)
            self.__tela.draw_map(self.__mapa.water_sprite, self.__mapa.original_map['water'])
            self.__tela.draw_map(self.__mapa.ground_sprite, self.__mapa.original_map['ground'])
            self.__tela.desenhar(sprites)
            self.__tela.imagem_relogio(self.__relogio.timer_text,1050,20)
            if colisoes.checar_colisoes_com_jogador(self.__mapa.tile_rects) == 'Perdeu!':
                break
            movimentacao.mover_personagens()
            self.__tela.update()
        self.game_over()

    def game_over(self):
        self.__ranking.atualiza_ranking(self.__usuario, self.__relogio.timer_sec)
        self.__tela.game_over()
        game_over = True
        #self.__som.iniciar(2)
        while game_over:
            self.__clock.tick(40)
            self.__tela.update()
            for event in self.__tela.ler():
                if event.type == pygame.QUIT:
                    self.__tela.fechar()
                if event.type == pygame.KEYDOWN:
                    if event.key == K_SPACE:
                        return self.restart()

    def restart(self):
        self.__mapa.reset()
        self.iniciar()