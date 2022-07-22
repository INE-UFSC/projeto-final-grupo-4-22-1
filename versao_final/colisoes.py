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

    def checar_colisoes_com_jogador(self, tiles):
        self.__colisoes_flores = pygame.sprite.spritecollide(self.__jogador, self.__mapa.lista_flores, True)
        self.__colisoes_parceiro = pygame.sprite.spritecollide(self.__jogador, self.__mapa.lista_parceiro, False)
        self.__colisoes_itens = pygame.sprite.spritecollide(self.__jogador, self.__mapa.lista_itens, True)
        self.__colisoes_inimigos = pygame.sprite.spritecollide(self.__jogador, self.__mapa.lista_inimigos, False)

        if self.__colisoes_inimigos:
            return self.__consequencias.jogador_e_inimigo()

        elif self.__colisoes_flores:
            flor = self.__colisoes_flores[0]
            self.__consequencias.jogador_e_flor(flor)

        elif self.__colisoes_itens:
            item = self.__colisoes_itens[0]
            self.__consequencias.jogador_e_item(item)

        elif self.__colisoes_parceiro:
            self.__consequencias.jogador_e_parceiro()

        #código feio pra caralho? sim
        jogador_tiles = self.colisao_tiles(tiles)
        for hit in jogador_tiles:
            if hit[1] == "void":
                self.__consequencias.jogador_e_barreira(jogador_tiles[0][0])
            elif hit[1] == "water":
                self.__consequencias.jogador_e_water()

    def colisao_tiles(self, tiles):
        hits = []
        for tile in tiles:
            if self.__jogador.rect.colliderect(tile[0]):
                hits.append(tile)
        return hits

    def reset(self):
        self.__colisoes_parceiro = None
        self.__colisoes_flores = None
        self.__colisoes_itens = None
