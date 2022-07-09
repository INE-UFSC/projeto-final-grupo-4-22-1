from operator import index
from TelaJogo import TelaJogo
from ranking import Ranking
from rankingDAO import RankingDAO
import pygame
from pygame.locals import *
from inimigos import Inimigo
from colisoes import Colisoes

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

    def iniciar_menu(self):
        self.__tela.iniciar()
        self.__tela.menu()
        self.__usuario = ''
        clock = pygame.time.Clock()
        font = pygame.font.Font(None, 32)
        menu = True
        color_inactive = pygame.Color('lightskyblue3')
        color_active = pygame.Color('dodgerblue2')
        color = color_inactive
        active = False
        while menu:
            self.__clock.tick(40)
            self.__tela.update()
            input_box = self.__tela.input_box()
            for event in self.__tela.ler():
                if event.type == pygame.QUIT:
                    self.__tela.fechar()
                if event.type == pygame.KEYDOWN:
                    if event.key == K_SPACE:
                        return self.iniciar()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if input_box.collidepoint(event.pos):
                        active = True
                    else:
                        active = False
                if event.type == pygame.KEYDOWN:
                    if active:
                        if event.key == pygame.K_RETURN:
                            print(self.__usuario)
                        elif event.key == pygame.K_BACKSPACE:
                            self.__usuario = self.__usuario[:-1]
                        else:
                            self.__usuario += event.unicode
            self.__tela.menu()
            txt_surface = font.render(self.__usuario, True, (233,233,233))
            pygame.draw.rect(self.__tela.tela, (0,0,0), input_box, 2)
            self.__tela.tela.blit(txt_surface, (input_box.x+5, input_box.y+5))
            pygame.display.flip()
            clock.tick(30)

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
                cobra.movimento(50,2,3,300,550,100,20,250,"Imagens/cobra_direita.png","Imagens/cobra_baixo.png","Imagens/cobra_esquerda.png","Imagens/cobra_cima.png",distancia_cobra,self.__jogador.rect.x,self.__jogador.rect.y)

            for jacare in self.__mapa.lista_jacares:
                distancia_jacare = jacare.distancia_ponto(self.__jogador.rect.x,self.__jogador.rect.y,jacare.rect.x,jacare.rect.y)
                jacare.movimento(15,4,5,600,500,500,0,80,"Imagens/jacare_direita.png","Imagens/jacare_baixo.png","Imagens/jacare_esquerda.png","Imagens/jacare_cima.png",distancia_jacare,self.__jogador.rect.x,self.__jogador.rect.y)

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
        self.__ranking.atualiza_ranking(self.__usuario, 300)
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
