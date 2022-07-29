import pygame

from game.character.enemies.jacare import Jacare
from game.character.enemies.cobra import Cobra

from game.collisions.CollisionConsequences import CollisionConsequences

class Collisions():
    def __init__(self, mapa, jogador):
        self.__mapa = mapa
        self.__jogador = jogador
        self.__consequences = CollisionConsequences(self)

    def checar_colisoes_com_jogador(self, tiles):
        self.__colisoes_flores = pygame.sprite.spritecollide(self.__jogador, self.__mapa.lista_flores, True)
        self.__colisoes_parceiro = pygame.sprite.spritecollide(self.__jogador, self.__mapa.lista_parceiro, False)
        self.__colisoes_itens = pygame.sprite.spritecollide(self.__jogador, self.__mapa.lista_itens, True)
        self.__colisoes_inimigos = pygame.sprite.spritecollide(self.__jogador, self.__mapa.enimies, False)

        if self.__colisoes_inimigos:
            return self.__consequences.jogador_e_inimigo(self.__jogador)

        elif self.__colisoes_flores:
            flor = self.__colisoes_flores[0]
            self.__consequences.jogador_e_flor(self.__jogador, flor)

        elif self.__colisoes_itens:
            item = self.__colisoes_itens[0]
            self.__consequences.jogador_e_item(self.__jogador, item)

        elif self.__colisoes_parceiro:
            self.__consequences.jogador_e_parceiro(self.__jogador)

        #código feio pra caralho? sim
        jogador_tiles = self.colisao_tiles(self.__jogador, tiles)
        for hit in jogador_tiles:
            if hit[1] == "void":
                self.__consequences.jogador_e_barreira_x(self.__jogador, hit[0])
                self.__consequences.jogador_e_barreira_y(self.__jogador, hit[0])
            elif hit[1] == "water":
                self.__consequences.jogador_e_water(self.__jogador)
            elif hit[1] == "ground":
                self.__consequences.jogador_e_ground(self.__jogador)

    def colisao_itens(self, item, tiles):
        item_tiles = self.colisao_tiles(item, tiles)
        for hit in item_tiles:
            if hit[1] != "ground":
                return False
        return True

    def colisao_tiles(self, personagem, tiles):
        hits = []
        for tile in tiles:
            if personagem.rect.colliderect(tile[0]):
                hits.append(tile)
        return hits

    def colisao_com_inimigos(self):
        inimigos = self.__mapa.enimies
        tile = self.__mapa.tile_rects
        
        for inimigo in inimigos:
            colisao_inimigo = self.colisao_tiles(inimigo, tile)

            for colisao in colisao_inimigo:
                if colisao[1] == "ground" and isinstance(inimigo, Jacare):
                    self.__consequences.enemy_x(inimigo, colisao[0])

                elif colisao[1] == "void" and isinstance(inimigo, Jacare):
                    if colisao[0].right == 0:
                        self.__consequences.enemy_x(inimigo, colisao[0])
                    else:
                        self.__consequences.enemy_y(inimigo, colisao[0])
                    
                elif colisao[1] == "void" and isinstance(inimigo, Cobra):
                    if colisao[0].right == 0:
                        self.__consequences.enemy_x(inimigo, colisao[0])
                    else:
                        self.__consequences.enemy_y(inimigo, colisao[0])

                elif colisao[1] == "water" and isinstance(inimigo, Cobra):
                    self.__consequences.enemy_x(inimigo, colisao[0])


    def reset(self):
        self.__colisoes_parceiro = None
        self.__colisoes_flores = None
        self.__colisoes_itens = None
