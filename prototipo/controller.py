from TelaJogo import TelaJogo
import pygame
from pygame.locals import *
from sapo import Sapo
from inimigos.cobra import Cobra
from inimigos.jacare import Jacare
from itens.girassol import Girassol

class GameController:
    def __init__(self):
        self.__tela = TelaJogo(self)
        self.__clock = pygame.time.Clock()
        self.__lista_cobras = pygame.sprite.Group()
        self.__lista_jacares = pygame.sprite.Group()
        self.__lista_players = pygame.sprite.Group()
        self.__all_sprites = pygame.sprite.Group()

    def iniciar(self):
        jogador = Sapo()
        cobra = Cobra()
        jacare = Jacare()
        girassol = Girassol()
        self.__lista_players.add(jogador)
        self.__lista_cobras.add(cobra)
        self.__lista_jacares.add(jacare)
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