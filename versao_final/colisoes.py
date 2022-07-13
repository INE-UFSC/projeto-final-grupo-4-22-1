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
    def __init__(self, mapa):
        self.__mapa = mapa
        self.__consequencias = ConsequenciasColisoes()
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
            return self.__consequencias.jogador_e_inimigo()

        elif self.__colisoes_jacare:
            return self.__consequencias.jogador_e_inimigo()

        if self.__colisoes_flores:
            flor = self.__colisoes_flores[0]
            self.__consequencias.jogador_e_flor(jogador, flor)

        elif self.__colisoes_macas:
            self.__consequencias.jogador_e_maca(jogador)

        elif self.__colisoes_cogumelos:
            self.__consequencias.jogador_e_cogumelo(jogador)

        elif self.__colisoes_espinhos:
            self.__consequencias.jogador_e_espinho(jogador)

        elif self.__colisoes_parceiro:
            self.__consequencias.jogador_e_parceiro(jogador)

    def reset(self):
        self.__colisoes_parceiro = None
        self.__colisoes_cobra = None
        self.__colisoes_jacare = None
        self.__colisoes_flores = None
        self.__colisoes_macas = None
        self.__colisoes_cogumelos = None
        self.__colisoes_espinhos = None
        self.__colisoes_terreno_aquatico = None
