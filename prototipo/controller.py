from TelaJogo import TelaJogo
import pygame
from pygame.locals import *

from terreno.aquatico import Aquatico
from sapo import Sapo

from inimigos.cobra import Cobra
from inimigos.jacare import Jacare

from itens.girassol import Girassol


# TODO: precisamos verificar se essa combinação de coordenadas que criamos p/ cada item já está sendo usada, pq se já estiver teremos que criar novas coordenadas até todas serem diferentes (isso é no arquivos do item, só deixei  comentário aqui, pq sempre usamos esse arquivo)


class GameController:
    def __init__(self):
        self.__tela = TelaJogo(self)
        self.__clock = pygame.time.Clock()
        self.__lista_cobras = pygame.sprite.Group()
        self.__lista_jacares = pygame.sprite.Group()
        self.__lista_players = pygame.sprite.Group()
        self.__all_sprites = pygame.sprite.Group()
        self.__lista_girassois = pygame.sprite.Group()

    def iniciar(self):
        jogador = Sapo()
        cobra = Cobra()
        jacare = Jacare()
        girassol = Girassol()
        
        self.__lista_players.add(jogador)
        self.__lista_cobras.add(cobra)
        self.__lista_jacares.add(jacare)
        self.__lista_girassois.add(girassol)
        
        self.__all_sprites.add(jogador)
        self.__all_sprites.add(cobra)
        self.__all_sprites.add(jacare)
        self.__all_sprites.add(girassol)
        
        self.__tela.iniciar()
        rodando = True
        
        while rodando:  
            self.__clock.tick(40)
            self.__tela.colorir()
            self.__tela.desenhar(self.__all_sprites)
            self.colisoes(jogador)
            for event in self.__tela.ler():
                if event.type == pygame.QUIT:
                    self.__tela.fechar()
                if event.type == pygame.KEYDOWN:
                    if event.key == K_LEFT and 0 <= jogador.rect.y:
                        jogador.rect.x += (-jogador.velocidade)
                    if event.key == K_RIGHT and self.__tela.largura - jogador.largura >= jogador.rect.x:
                        jogador.rect.x += (jogador.velocidade)
                    if event.key == K_UP and 0 <= jogador.coordenaday:
                        jogador.rect.y += (-jogador.velocidade)
                    if event.key == K_DOWN and self.__tela.altura - jogador.altura >= jogador.rect.y:
                        jogador.rect.y += (jogador.velocidade)
            if pygame.key.get_pressed()[K_LEFT] and 0 <= jogador.rect.x:
                jogador.rect.x += (-jogador.velocidade)
            if pygame.key.get_pressed()[K_RIGHT] and self.__tela.largura - jogador.largura >= jogador.rect.x:
                jogador.rect.x += (jogador.velocidade)
            if pygame.key.get_pressed()[K_UP] and 0 <= jogador.rect.y:
                jogador.rect.y += (-jogador.velocidade)
            if pygame.key.get_pressed()[K_DOWN] and self.__tela.altura - jogador.altura >= jogador.rect.y:
                jogador.rect.y += (jogador.velocidade)
            self.__tela.update()

    def colisoes(self, jogador):
        colisoes_cobras = pygame.sprite.spritecollide(jogador, self.__lista_cobras, True)
        colisoes_jacare = pygame.sprite.spritecollide(jogador, self.__lista_jacares, True)
        jogador.flores = pygame.sprite.spritecollide(jogador, self.__lista_girassois, True)
        #colisoes_flores = pygame.sprite.spritecollide(jogador, self.__lista_girassois, True)
