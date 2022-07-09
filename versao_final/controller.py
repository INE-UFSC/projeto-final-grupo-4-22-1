from operator import index
from TelaJogo import TelaJogo
from ranking import Ranking
from rankingDAO import RankingDAO
import pygame
from pygame.locals import *
from inimigos import Inimigo
from colisoes import Colisoes
from bibliotecaImagens import BibliotecaImagens

from terreno.aquatico import Aquatico
from sapo import Sapo
from ra import Ra

from inimigos.cobra import Cobra
from inimigos.jacare import Jacare
import random

from itens.girassol import Girassol
from itens.jasmin import Jasmin
from itens.maca import Maca
from itens.espinho import Espinho
from itens.cogumelo import Cogumelo

from coordenada import Coordenada
from mapa import Mapa
from input_box import InputBox
#c_flor = Coordenada(0,0,0)
#c_item = Coordenada(0,0,0)
c1 = Coordenada(0,0,0)


# TODO: precisamos verificar se essa combinação de coordenadas que criamos p/ cada item já está sendo usada, pq se já estiver teremos que criar novas coordenadas até todas serem diferentes (isso é no arquivos do item, só deixei  comentário aqui, pq sempre usamos esse arquivo)


class GameController:
    def __init__(self):
        self.__rankingDAO = RankingDAO()
        self.__ranking = Ranking(self.__rankingDAO)
        self.__mapa = Mapa()
        self.__colisoes = Colisoes(self.__mapa)
        self.__tela = TelaJogo(self)
        self.__clock = pygame.time.Clock()
        self.__jogador = None
        self.__imagens = BibliotecaImagens()

    def iniciar_menu(self):
        self.__tela.iniciar()
        self.__tela.menu()
        self.__usuario = ''
        input_box = InputBox(430,300,140,32)
        menu = True
        while menu:
            self.__tela.update()
            for event in self.__tela.ler():
                if event.type == pygame.QUIT:
                    self.__tela.fechar()
                if event.type == pygame.KEYDOWN:
                    if event.key == K_SPACE:
                        self.__usuario = input_box.texto
                        return self.iniciar()
                input_box.handle_event(event)
            self.__tela.menu()
            self.__tela.desenhar_input_box(input_box)
            pygame.display.flip()
            self.__clock.tick(30)

    def iniciar(self):
        self.__jogador = Sapo()
        self.__tela.iniciar()
        rodando = True
        sprites = self.__mapa.spawn_all()
        sprites.add(self.__jogador)
        
        while rodando:  
            self.__clock.tick(40)
            self.__tela.colorir()
            self.__tela.desenhar(sprites)

            if self.__colisoes.checar_colisoes_com_jogador(self.__jogador) == 'Perdeu!':
                break
            
            for cobra in self.__mapa.lista_cobras:
                distancia_cobra = cobra.distancia_ponto(self.__jogador.rect.x,self.__jogador.rect.y,cobra.rect.x,cobra.rect.y)
                cobra.movimento(50,2,3,300,550,100,20,250,self.__imagens.cobra_direita,self.__imagens.cobra_baixo,self.__imagens.cobra_esquerda,self.__imagens.cobra_cima,distancia_cobra,self.__jogador.rect.x,self.__jogador.rect.y)

            for jacare in self.__mapa.lista_jacares:
                distancia_jacare = jacare.distancia_ponto(self.__jogador.rect.x,self.__jogador.rect.y,jacare.rect.x,jacare.rect.y)
                jacare.movimento(15,4,5,600,500,500,0,80,self.__imagens.jacare_direita,self.__imagens.jacare_baixo,self.__imagens.jacare_esquerda,self.__imagens.jacare_cima,distancia_jacare,self.__jogador.rect.x,self.__jogador.rect.y)

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

            self.__tela.update()
        self.game_over()

    def game_over(self):
        self.__ranking.atualiza_ranking(self.__usuario, 502)
        self.__tela.game_over()
        game_over = True
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
        self.__colisoes.reset()
        self.__jogador = None
        self.iniciar()
