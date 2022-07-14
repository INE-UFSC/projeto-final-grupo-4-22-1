import pygame
from mapa import Mapa
from sapo import Sapo
from itens.girassol import Girassol
from itens.jasmin import Jasmin
from itens.maca import Maca
from itens.espinho import Espinho
from itens.cogumelo import Cogumelo
from consequenciasColisoes import ConsequenciasColisoes

class Colisoes():
    def __init__(self, mapa, jogador):
        self.__mapa = mapa
        self.__jogador = jogador
        self.__consequencias = ConsequenciasColisoes(self.__jogador)
        self.__colisoes_parceiro = None
        self.__colisoes_cobra = None
        self.__colisoes_jacare = None
        self.__colisoes_flores = None
        self.__colisoes_macas = None
        self.__colisoes_espinhos = None
        self.__colisoes_cogumelos = None
        self.__colisoes_terreno_aquatico = None

    def checar_colisoes_com_jogador(self):
        self.__colisoes_cobra = pygame.sprite.spritecollide(self.__jogador, self.__mapa.lista_cobras, False)
        self.__colisoes_jacare = pygame.sprite.spritecollide(self.__jogador, self.__mapa.lista_jacares, False)
        self.__colisoes_flores = pygame.sprite.spritecollide(self.__jogador, self.__mapa.lista_flores, True)
        self.__colisoes_terreno_aquatico = pygame.sprite.spritecollide(self.__jogador, self.__mapa.lista_terreno_aquatico, False)
        self.__colisoes_parceiro = pygame.sprite.spritecollide(self.__jogador, self.__mapa.lista_parceiro, False)
        self.__colisoes_macas = pygame.sprite.spritecollide(self.__jogador, self.__mapa.lista_macas, True)
        self.__colisoes_cogumelos = pygame.sprite.spritecollide(self.__jogador,self.__mapa.lista_cogumelos,True)
        self.__colisoes_espinhos = pygame.sprite.spritecollide(self.__jogador,self.__mapa.lista_espinhos,True)

        if self.__colisoes_cobra:
            return self.__consequencias.jogador_e_inimigo()

        elif self.__colisoes_jacare:
            return self.__consequencias.jogador_e_inimigo()

        if self.__colisoes_flores:
            flor = self.__colisoes_flores[0]
            self.__consequencias.jogador_e_flor(flor)

        elif self.__colisoes_macas:
            m1 = Maca(0,0)
            self.__consequencias.jogador_e_maca(m1)

        elif self.__colisoes_cogumelos:
            c1 = Cogumelo(0,0)
            self.__consequencias.jogador_e_cogumelo(c1)

        elif self.__colisoes_espinhos:
            e1 = Espinho(0,0)
            self.__consequencias.jogador_e_espinho(e1)

        elif self.__colisoes_parceiro:
            self.__consequencias.jogador_e_parceiro()

    def reset(self):
        self.__colisoes_parceiro = None
        self.__colisoes_cobra = None
        self.__colisoes_jacare = None
        self.__colisoes_flores = None
        self.__colisoes_macas = None
        self.__colisoes_cogumelos = None
        self.__colisoes_espinhos = None
        self.__colisoes_terreno_aquatico = None
