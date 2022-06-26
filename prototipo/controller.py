from operator import index
from TelaJogo import TelaJogo
import pygame
from pygame.locals import *

from terreno.aquatico import Aquatico
from sapo import Sapo
from ra import Ra

from inimigos.cobra import Cobra
from inimigos.jacare import Jacare
import random

from itens.girassol import Girassol
from itens.jasmin import Jasmin


# TODO: precisamos verificar se essa combinação de coordenadas que criamos p/ cada item já está sendo usada, pq se já estiver teremos que criar novas coordenadas até todas serem diferentes (isso é no arquivos do item, só deixei  comentário aqui, pq sempre usamos esse arquivo)


class GameController:
    def __init__(self):
        self.__tela = TelaJogo(self)
        self.__clock = pygame.time.Clock()
        
        self.__lista_player = pygame.sprite.Group()
        self.__jogador = None

        self.__lista_parceiro = pygame.sprite.Group()
        self.__colisoes_parceiro = None

        self.__lista_cobras = pygame.sprite.Group()
        self.__colisoes_cobra = None

        self.__lista_jacares = pygame.sprite.Group()
        self.__colisoes_jacare = None

        self.__lista_flores = pygame.sprite.Group()
        self.__colisoes_flores = None

        self.__lista_terreno_aquatico = pygame.sprite.Group()
        self.__colisoes_terreno_aquatico = None
        
        self.__all_sprites = pygame.sprite.Group()
        
        #chave é o objeto flor e o valor é bool p/ saber se seu peso foi ou não descontado da velocidade do sapo
        self.__flores_coletadas = {}

    def iniciar(self):
        self.__jogador = Sapo()
        ra = Ra()
        cobra = Cobra(50,30,100,100,5,2,'terrestre')

        jacare = Jacare(70,40,500,60,10,3,'aquatico')
        
        aquatico = Aquatico()

        self.__lista_terreno_aquatico.add(aquatico)
        self.__lista_player.add(self.__jogador)
        self.__lista_parceiro.add(ra)
        self.__lista_cobras.add(cobra)
        self.__lista_jacares.add(jacare)
        
        self.__all_sprites.add(aquatico, self.__jogador, ra)
        
        #FIXME: só para o mvp, dps isso dependerá da fase (que ainda não foi implementada)
        for flor in range(0, 10):
            #print("aaa")
            #print(self.__all_sprites)
            girassol = Girassol()
            jasmin = Jasmin()
            
            self.__lista_flores.add(girassol, jasmin)
            self.__all_sprites.add(girassol, jasmin)
        
        print(self.__all_sprites)
        self.__tela.iniciar()
        rodando = True
        
        while rodando:  
            self.__clock.tick(40)
            self.__tela.colorir()
            self.__tela.desenhar(self.__all_sprites)
            self.colisoes()
            cobra.movimento(50)
            jacare.movimento(15)
            
            
            if self.__colisoes_cobra:
                print("Perdeu! A cobra te pegou!")
                break
            elif self.__colisoes_jacare:
                print("Perdeu! O jacaré te pegou!")
                break
            elif self.__colisoes_flores:
                flor = self.__colisoes_flores[0]
                self.__flores_coletadas[flor] = self.__jogador.carry(flor.peso)
            elif self.__colisoes_parceiro:
                remove = []
                for flor in self.__flores_coletadas:
                    if self.__flores_coletadas[flor] == True:
                        self.__jogador.aumenta_velocidade(flor.peso)
                self.__flores_coletadas = {}
            
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
        self.__colisoes_terreno_aquatico = pygame.sprite.spritecollide(self.__jogador, self.__lista_terreno_aquatico, False)
        self.__colisoes_parceiro = pygame.sprite.spritecollide(self.__jogador, self.__lista_parceiro, False)
