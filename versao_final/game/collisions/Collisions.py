import pygame

from game.character.enemies.jacare import Jacare
from game.character.enemies.cobra import Cobra

from game.collisions.CollisionConsequences import CollisionConsequences

class Collisions():
    def __init__(self, mapa, jogador):
        self.__mapa = mapa
        self.__jogador = jogador
        self.__consequences = CollisionConsequences(self.__jogador)

    def checar_colisoes_com_jogador(self, tiles):
        self.__colisoes_flores = pygame.sprite.spritecollide(self.__jogador, self.__mapa.lista_flores, True)
        self.__colisoes_parceiro = pygame.sprite.spritecollide(self.__jogador, self.__mapa.lista_parceiro, False)
        self.__colisoes_itens = pygame.sprite.spritecollide(self.__jogador, self.__mapa.lista_itens, True)
        self.__colisoes_inimigos = pygame.sprite.spritecollide(self.__jogador, self.__mapa.lista_inimigos, False)

        if self.__colisoes_inimigos:
            return self.__consequences.jogador_e_inimigo()

        elif self.__colisoes_flores:
            flor = self.__colisoes_flores[0]
            self.__consequences.jogador_e_flor(flor)

        elif self.__colisoes_itens:
            item = self.__colisoes_itens[0]
            self.__consequences.jogador_e_item(item)

        elif self.__colisoes_parceiro:
            self.__consequences.jogador_e_parceiro()

        #código feio pra caralho? sim
        jogador_tiles = self.colisao_tiles(self.__jogador, tiles)
        for hit in jogador_tiles:
            if hit[1] == "void":
                self.__consequences.jogador_e_barreira_x(hit[0])
                self.__consequences.jogador_e_barreira_y(hit[0])
            elif hit[1] == "water":
                self.__consequences.jogador_e_water()

    def colisao_tiles(self, personagem, tiles):
        hits = []
        for tile in tiles:
            if personagem.rect.colliderect(tile[0]):
                hits.append(tile)
        return hits

    def colisao_com_inimigos(self, inimigos, tiles):
        for inimigo in inimigos:
            colisao_inimigo = self.colisao_tiles(inimigo, tiles)

            for colisao in colisao_inimigo:
                if colisao[1] == "ground" and isinstance(inimigo, Jacare):
                    if colisao[0].x + 100 > inimigo.rect.x:
                        inimigo.rect.x = colisao[0].right

                    elif colisao[0].x < inimigo.rect.x:
                        inimigo.rect.x = colisao[0].left

                elif colisao[1] == "void" and isinstance(inimigo, Jacare):
                    if colisao[0].y + 100 > inimigo.rect.y:
                        inimigo.rect.y = colisao[0].bottom
                    elif colisao[0].y < inimigo.rect.y:
                        inimigo.rect.y = colisao[0].top

                if colisao[1] == "water" and isinstance(inimigo, Cobra):
                    if colisao[0].x + 100 > inimigo.rect.x:
                        inimigo.rect.x = colisao[0].right

                    elif colisao[0].x < inimigo.rect.x:
                        inimigo.rect.x = colisao[0].left

                elif colisao[1] == "void" and isinstance(inimigo, Cobra):
                    if colisao[0].y + 100 > inimigo.rect.y:
                        inimigo.rect.y = colisao[0].bottom
                    elif colisao[0].y < inimigo.rect.y:
                        inimigo.rect.y = colisao[0].top

    def reset(self):
        self.__colisoes_parceiro = None
        self.__colisoes_flores = None
        self.__colisoes_itens = None
