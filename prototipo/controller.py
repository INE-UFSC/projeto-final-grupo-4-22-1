from TelaJogo import TelaJogo
import pygame
from pygame.locals import *

from terreno.aquatico import Aquatico
from sapo import Sapo

from inimigos.cobra import Cobra
from inimigos.jacare import Jacare

from itens.girassol import Girassol
from itens.jasmin import Jasmin


# TODO: precisamos verificar se essa combinação de coordenadas que criamos p/ cada item já está sendo usada, pq se já estiver teremos que criar novas coordenadas até todas serem diferentes (isso é no arquivos do item, só deixei  comentário aqui, pq sempre usamos esse arquivo)


class GameController:
    def __init__(self):
        self.__tela = TelaJogo(self)
        self.__clock = pygame.time.Clock()
        
        self.__lista_players = pygame.sprite.Group()
        self.__jogador = None

        self.__lista_cobras = pygame.sprite.Group()
        self.__colisoes_cobra = None

        self.__lista_jacares = pygame.sprite.Group()
        self.__colisoes_jacare = None

        self.__lista_flores = pygame.sprite.Group()
        self.__colisoes_flores = None

        self.__lista_terreno_aquatico = pygame.sprite.Group()
        
        self.__all_sprites = pygame.sprite.Group()
        
    def iniciar(self):
        self.__jogador = Sapo()
        cobra = Cobra()
        jacare = Jacare()
        
        girassol = Girassol()
        jasmin = Jasmin()
        
        aquatico = Aquatico()
        
        self.__lista_terreno_aquatico.add(aquatico)
        self.__lista_players.add(self.__jogador)
        self.__lista_cobras.add(cobra)
        self.__lista_jacares.add(jacare)
        self.__lista_flores.add(girassol, jasmin)
        
        self.__all_sprites.add(aquatico)
        self.__all_sprites.add(self.__jogador)
        self.__all_sprites.add(cobra)
        self.__all_sprites.add(girassol, jasmin)
        self.__all_sprites.add(jacare)
        
        self.__tela.iniciar()
        rodando = True
        
        while rodando:  
            self.__clock.tick(40)
            self.__tela.colorir()
            self.__tela.desenhar(self.__all_sprites)
            
            self.colisoes()
            
            if self.__colisoes_cobra:
                print("Perdeu! A cobra te pegou!")
                break
            elif self.__colisoes_jacare:
                print("Perdeu! O jacaré te pegou!")
                break
            elif self.__colisoes_flores:
                peso = self.__colisoes_flores[0].peso
                self.__jogador.carry(peso)

            for event in self.__tela.ler():
                if event.type == pygame.QUIT:
                    self.__tela.fechar()
                if event.type == pygame.KEYDOWN:
                    if event.key == K_LEFT and 0 <= self.__jogador.rect.y:
                        self.__jogador.rect.x += (-self.__jogador.velocidade)
                    if event.key == K_RIGHT and self.__tela.largura - self.__jogador.largura >= self.__jogador.rect.x:
                        self.__jogador.rect.x += (self.__jogador.velocidade)
                    if event.key == K_UP and 0 <= self.__jogador.coordenaday:
                        self.__jogador.rect.y += (-self.__jogador.velocidade)
                    if event.key == K_DOWN and self.__tela.altura - self.__jogador.altura >= self.__jogador.rect.y:
                        self.__jogador.rect.y += (self.__jogador.velocidade)

            if pygame.key.get_pressed()[K_LEFT] and 0 <= self.__jogador.rect.x:
                self.__jogador.rect.x += (-self.__jogador.velocidade)
            if pygame.key.get_pressed()[K_RIGHT] and self.__tela.largura - self.__jogador.largura >= self.__jogador.rect.x:
                self.__jogador.rect.x += (self.__jogador.velocidade)
            if pygame.key.get_pressed()[K_UP] and 0 <= self.__jogador.rect.y:
                self.__jogador.rect.y += (-self.__jogador.velocidade)
            if pygame.key.get_pressed()[K_DOWN] and self.__tela.altura - self.__jogador.altura >= self.__jogador.rect.y:
                self.__jogador.rect.y += (self.__jogador.velocidade)

            self.__tela.update()

    def colisoes(self):
        self.__colisoes_cobra = pygame.sprite.spritecollide(self.__jogador, self.__lista_cobras, False)
        self.__colisoes_jacare = pygame.sprite.spritecollide(self.__jogador, self.__lista_jacares, False)
        #jogador.flores = pygame.sprite.spritecollide(self.__jogador, self.__lista_girassois, True)
        self.__colisoes_flores = pygame.sprite.spritecollide(self.__jogador, self.__lista_flores, True)
        colisoes_terreno_aquatico = pygame.sprite.spritecollide(self.__jogador, self.__lista_terreno_aquatico, False)
