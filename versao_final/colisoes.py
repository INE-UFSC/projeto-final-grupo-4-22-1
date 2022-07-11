import pygame
from mapa import Mapa
from sapo import Sapo
from itens.girassol import Girassol
from itens.jasmin import Jasmin
from itens.maca import Maca
from itens.espinho import Espinho
from itens.cogumelo import Cogumelo

class Colisoes():
    def __init__(self, mapa):
        self.__mapa = mapa
        self.__colisoes_parceiro = None
        self.__colisoes_cobra = None
        self.__colisoes_jacare = None
        self.__colisoes_flores = None
        self.__colisoes_macas = None
        self.__colisoes_espinhos = None
        self.__colisoes_cogumelos = None
        self.__colisoes_terreno_aquatico = None

    def checar_colisoes_com_jogador(self, jogador):
        self.__colisoes_cobra = pygame.sprite.spritecollide(jogador, self.__mapa.lista_cobras, False)
        self.__colisoes_jacare = pygame.sprite.spritecollide(jogador, self.__mapa.lista_jacares, False)
        self.__colisoes_flores = pygame.sprite.spritecollide(jogador, self.__mapa.lista_flores, True)
        self.__colisoes_terreno_aquatico = pygame.sprite.spritecollide(jogador, self.__mapa.lista_terreno_aquatico, False)
        self.__colisoes_parceiro = pygame.sprite.spritecollide(jogador, self.__mapa.lista_parceiro, False)
        self.__colisoes_macas = pygame.sprite.spritecollide(jogador, self.__mapa.lista_macas, True)
        self.__colisoes_cogumelos = pygame.sprite.spritecollide(jogador,self.__mapa.lista_cogumelos,True)
        self.__colisoes_espinhos = pygame.sprite.spritecollide(jogador,self.__mapa.lista_espinhos,True)

        if self.__colisoes_cobra:
            return "Perdeu!"

        elif self.__colisoes_jacare:
            return("Perdeu!")

        if self.__colisoes_flores:
            flor = self.__colisoes_flores[0]
            jogador.flores_coletadas[flor] = jogador.carry(flor.peso)

        elif self.__colisoes_macas:
            if jogador.velocidade<0:
                jogador.debuff()
            jogador.aumenta_velocidade(3)

        elif self.__colisoes_cogumelos:
            jogador.debuff()
        elif self.__colisoes_espinhos:
            jogador.aumenta_velocidade(-3)

        elif self.__colisoes_parceiro:
            for flor in jogador.flores_coletadas:
                if jogador.flores_coletadas[flor] == True:
                    jogador.aumenta_velocidade(flor.peso)
            jogador.soltar_flores()

    def reset(self):
        self.__colisoes_parceiro = None
        self.__colisoes_cobra = None
        self.__colisoes_jacare = None
        self.__colisoes_flores = None
        self.__colisoes_macas = None
        self.__colisoes_cogumelos = None
        self.__colisoes_espinhos = None
        self.__colisoes_terreno_aquatico = None
