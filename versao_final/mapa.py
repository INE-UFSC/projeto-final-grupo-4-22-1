import pygame
import csv

from itens.girassol import Girassol
from itens.jasmin import Jasmin
from itens.maca import Maca
from itens.espinho import Espinho
from itens.cogumelo import Cogumelo

from terreno.aquatico import Aquatico
from terreno.terrestre import Terrestre

from ra import Ra

from inimigos.cobra import Cobra
from inimigos.jacare import Jacare

from coordenadas.coordenada import Coordenada
from TelaJogo import TelaJogo

class Mapa:
    def __init__(self):
        self.__lista_parceiro = pygame.sprite.Group()
        self.__lista_cobras = pygame.sprite.Group()
        self.__lista_jacares = pygame.sprite.Group()
        self.__lista_inimigos = pygame.sprite.Group()
        self.__lista_flores = pygame.sprite.Group()
        self.__lista_macas = pygame.sprite.Group()
        self.__lista_cogumelos = pygame.sprite.Group()
        self.__lista_espinhos = pygame.sprite.Group()
        self.__lista_terreno_aquatico = pygame.sprite.Group()
        self.__all_sprites = pygame.sprite.Group()
        self.__lista_itens = pygame.sprite.Group()
        
        self.__aquatico = Aquatico()
        self.__terrestre = Terrestre()

        self.__c1 = Coordenada(0,0)
        self.__tela = TelaJogo(self)
        
    def load_map(self):
        map_list = []
        self.__tile_rects = []
        
        with open('mapa.csv', 'r') as file_obj:
            reader_obj = csv.reader(file_obj)
            for row in reader_obj:
                map_list.append(list(row))
        print(map_list)

        height, width = len(map_list), len(map_list[0])

        self.__original_map = {'terra': [], 'agua': [], 'void': []}
        for y, line in enumerate(map_list):
            if line != '':
                for x, tile_name in enumerate(line):
                    self.__original_map[tile_name].append((x*100-100,y*100-100))
                    if tile_name == 'agua':
                        self.__tile_rects.append((pygame.Rect(x*100-100,y*100-100, 100, 100), 'agua'))
                    elif tile_name == 'void':
                        self.__tile_rects.append((pygame.Rect(x*100-100, y*100-100, 100, 100), 'void'))

    def spawn_flores(self, quantidade):
        for i in range (quantidade):
            self.__c1.coordenadas('coletavel')
            girassol = Girassol(self.__c1.coordenadax,self.__c1.coordenaday)
            self.__c1.coordenadas('coletavel')
            jasmin = Jasmin(self.__c1.coordenadax,self.__c1.coordenaday)
            self.__lista_flores.add(girassol, jasmin)
            self.__all_sprites.add(girassol, jasmin)

    def spawn_cobras(self):
        cobra = Cobra(50,30,100,100,2,2,'terrestre')
        self.__lista_cobras.add(cobra)
        self.__lista_inimigos.add(cobra)

    def spawn_jacares(self):
        jacare = Jacare(70,40,500,60,10,3,'aquatico')
        self.__lista_jacares.add(jacare)
        self.__lista_inimigos.add(jacare)

    def spawn_consumiveis(self, quant_maca, quant_espinho, quant_cogumelo):
        for i in range (quant_maca):
            self.__c1.coordenadas('consumivel')
            maca = Maca(self.__c1.coordenadax,self.__c1.coordenaday)
            self.__lista_macas.add(maca)
        for i in range (quant_espinho):
            self.__c1.coordenadas('consumivel')
            espinho = Espinho(self.__c1.coordenadax,self.__c1.coordenaday)
            self.__lista_espinhos.add(espinho)
        for i in range (quant_cogumelo):
            self.__c1.coordenadas('consumivel')
            cogumelo = Cogumelo(self.__c1.coordenadax,self.__c1.coordenaday)
            self.__lista_cogumelos.add(cogumelo)

        self.__all_sprites.add(maca, espinho,cogumelo)
        self.__lista_itens.add(maca, espinho, cogumelo)

    def spawn_ra(self):
        ra = Ra(30, 30, 15, 585)
        self.__lista_parceiro.add(ra)
        self.__all_sprites.add(ra)

    def spawn_all(self, quant_maca, quant_espinho, quant_cogumelo, quant_flores):
        self.spawn_ra()
        self.spawn_consumiveis(quant_maca, quant_espinho, quant_cogumelo)
        self.spawn_jacares()
        self.spawn_cobras()
        self.spawn_flores(quant_flores)

    def reset(self):
        self.__lista_parceiro = pygame.sprite.Group()
        self.__lista_cobras = pygame.sprite.Group()
        self.__lista_jacares = pygame.sprite.Group()
        self.__lista_flores = pygame.sprite.Group()
        self.__lista_macas = pygame.sprite.Group()
        self.__lista_cogumelos = pygame.sprite.Group()
        self.__lista_espinhos = pygame.sprite.Group()
        self.__lista_terreno_aquatico = pygame.sprite.Group()
        self.__all_sprites = pygame.sprite.Group()
        self.__lista_inimigos = pygame.sprite.Group()
        self.__c1 = Coordenada(0,0)
        self.__lista_itens = pygame.sprite.Group()

    @property
    def lista_itens(self):
        return self.__lista_itens

    @property
    def lista_cobras(self):
        return self.__lista_cobras

    @property
    def lista_jacares(self):
        return self.__lista_jacares

    @property
    def lista_parceiro(self):
        return self.__lista_parceiro

    @property
    def lista_flores(self):
        return self.__lista_flores

    @property
    def lista_macas(self):
        return self.__lista_macas

    @property
    def lista_espinhos(self):
        return self.__lista_espinhos

    @property
    def lista_cogumelos(self):
        return self.__lista_cogumelos

    @property
    def lista_terreno_aquatico(self):
        return self.__lista_terreno_aquatico

    @property
    def all_sprites(self):
        return self.__all_sprites

    @property
    def lista_inimigos(self):
        return self.__lista_inimigos

    @property
    def original_map(self):
        return self.__original_map

    @property
    def aquatico_sprite(self):
        return self.__aquatico.sprite

    @property
    def terrestre_sprite(self):
        return self.__terrestre.sprite

    @property
    def tile_rects(self):
        return self.__tile_rects
