import pygame, random, time

from pygame.locals import *
from operator import index

from game.GameScreen import GameScreen
from game.Clock import Clock

from game.ranking.Ranking import Ranking

from game.collisions.Collisions import Collisions

from game.maps.terreno.Water import Water

from game.character.ra import Ra
from game.character.player.sapo import Sapo
from game.character.enemies.cobra import Cobra
from game.character.enemies.jacare import Jacare

from game.items.collectibles.sunflower import Sunflower
from game.items.collectibles.jasminen import Jasminen

from game.items.Apple import Apple
from game.items.Thorn import Thorn
from game.items.Mushroom import Mushroom

from game.maps.mapa import Mapa
from game.menus.input_box import InputBox
from game.Movimentacao import Movimentacao

from game.construtorDeFases import ConstrutorDeFases

from game.som.Som import Som


class GameController:
    def __init__(self):
        self.__ranking = Ranking()
        self.__mapa = Mapa()
        self.__screen = GameScreen(self)
        self.__construtor = ConstrutorDeFases(self.__mapa)
        self.__clock = pygame.time.Clock()
        self.__jogador = None
        self.__relogio = Clock()
        self.__teste = False
        self.__som = Som()

    def start(self):
        self.__screen.start()
        self.__usuario = ''
        input_box = InputBox(430,300,140,32)
        menu = True
        #self.__som.iniciar(1)
        while menu:
            self.__screen.menu(input_box)
            for event in self.__screen.ler():
                if event.type == pygame.QUIT:
                    self.__screen.fechar()
                if event.type == pygame.KEYDOWN:
                    if event.key == K_RETURN:
                        self.__usuario = input_box.texto
                        pygame.time.set_timer(pygame.USEREVENT,310)
                        return self.iniciar()
                    if event.key == K_BACKSPACE:
                        self.tela_ranking()
                input_box.handle_event(event)
            self.__screen.update()
            self.__clock.tick(30)

    def iniciar(self):
        fase_atual = 1
        self.__screen.start()
        rodando = True
        #self.__som.iniciar(0)
        game = True
        vitoria = False
        while game:
            self.__relogio.iniciar_clock()
            self.__jogador = Sapo(30, 30, 3, 300, 300, 7)
            if self.__construtor.gerar_fase(fase_atual) == "Finished!":
                vitoria = True
                break
            sprites = self.__mapa.all_sprites
            sprites.add(self.__jogador)
            movimentacao = Movimentacao(self.__screen, self.__jogador, self.__mapa)
            collisions = Collisions(self.__mapa, self.__jogador)
            while rodando:
                for event in self.__screen.ler():
                    if event.type == pygame.QUIT:
                        self.__screen.fechar()
                    elif event.type == pygame.USEREVENT:
                        self.__teste = self.__relogio.verifica_clock()
                if self.__teste == True:
                    break
                self.__clock.tick(40)
                self.__screen.draw_map(self.__mapa.dict_sprites_mapa, self.__mapa.original_map)
                self.__screen.desenhar(sprites)
                self.__screen.imagem_relogio(self.__relogio.timer_text,1050,20)
                if self.__mapa.checar_flores() == "Acabou!" and self.__jogador.flores_coletadas == {}:
                    break
                if collisions.checar_colisoes_com_jogador(self.__mapa.tile_rects) == 'Perdeu!':
                    game = False
                    break
                collisions.colisao_com_inimigos()
                movimentacao.mover_personagens()
                print(self.__jogador.velocidade)
                self.__screen.update()
            if game == False:
                break
            self.__mapa.reset()
            fase_atual += 1
        self.game_over()

    def game_over(self):
        self.__ranking.atualiza_ranking(self.__usuario, self.__relogio.timer_sec)
        game_over = True
        #self.__som.iniciar(2)
        while game_over:
            self.__clock.tick(40)
            self.__screen.update()
            self.__screen.game_over()
            for event in self.__screen.ler():
                if event.type == pygame.QUIT:
                    self.__screen.fechar()
                if event.type == pygame.KEYDOWN:
                    if event.key == K_RETURN:
                        return self.restart()
                    elif event.key == K_BACKSPACE:
                        self.tela_ranking()

    def tela_ranking(self):
        while True:
            for event in self.__screen.ler():
                if event.type == pygame.QUIT:
                    self.__screen.fechar()
                if event.type == pygame.KEYDOWN:
                    if event.key == K_BACKSPACE:
                        return
                    if event.key == K_r:
                        self.__ranking.reset_ranking()
            self.__screen.tela_ranking(self.__ranking.ranking)
            self.__screen.update()

    def restart(self):
        self.__mapa.reset()
        self.start()
