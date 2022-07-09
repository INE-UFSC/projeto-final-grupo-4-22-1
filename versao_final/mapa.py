import pygame

from itens.girassol import Girassol
from itens.jasmin import Jasmin
from itens.maca import Maca
from itens.espinho import Espinho
from itens.cogumelo import Cogumelo

from terreno.aquatico import Aquatico
from ra import Ra

from inimigos.cobra import Cobra
from inimigos.jacare import Jacare

from coordenada import Coordenada

class Mapa:
    def __init__(self):
        self.__lista_parceiro = pygame.sprite.Group()
        self.__lista_cobras = pygame.sprite.Group()
        self.__lista_jacares = pygame.sprite.Group()
        self.__lista_flores = pygame.sprite.Group()
        self.__lista_consumiveis = pygame.sprite.Group()
        self.__lista_cogumelos = pygame.sprite.Group()
        self.__lista_terreno_aquatico = pygame.sprite.Group()
        self.__all_sprites = pygame.sprite.Group()
        self.__c1 = Coordenada(0,0,0)

    def spawn_flores(self, quantidade):
        for i in range (quantidade):
            self.__c1.coordenadas()
            girassol = Girassol(self.__c1.coordenadax,self.__c1.coordenaday)
            self.__c1.coordenadas()
            jasmin = Jasmin(self.__c1.coordenadax,self.__c1.coordenaday)
            self.__lista_flores.add(girassol, jasmin)
            self.__all_sprites.add(girassol, jasmin)

    def spawn_cobras(self):
        cobra = Cobra(50,30,100,100,2,2,'terrestre')
        self.__lista_cobras.add(cobra)


    def spawn_jacares(self):
        jacare = Jacare(70,40,500,60,10,3,'aquatico')
        self.__lista_jacares.add(jacare)

    def spawn_consumiveis(self):
        for i in range (2):
            self.__c1.coordenadas()
            maca = Maca(self.__c1.coordenadax,self.__c1.coordenaday)
            self.__c1.coordenadas()
            espinho = Espinho(self.__c1.coordenadax,self.__c1.coordenaday)
            self.__c1.coordenadas()
            cogumelo = Cogumelo(self.__c1.coordenadax,self.__c1.coordenaday)

            self.__lista_consumiveis.add(maca, espinho)
            self.__lista_cogumelos.add(cogumelo)
            self.__all_sprites.add(maca, espinho,cogumelo)

    def spawn_ra(self):
        ra = Ra()
        self.__lista_parceiro.add(ra)
        self.__all_sprites.add(ra)

    def spawn_terrenos(self):
        aquatico = Aquatico()
        self.__lista_terreno_aquatico.add(aquatico)
        self.__all_sprites.add(aquatico)
    
    def spawn_all(self):
        self.spawn_terrenos()
        self.spawn_ra()
        self.spawn_consumiveis()
        self.spawn_jacares()
        self.spawn_cobras()
        self.spawn_flores(5)
        return self.__all_sprites

    def reset(self):
        self.__lista_parceiro = pygame.sprite.Group()
        self.__lista_cobras = pygame.sprite.Group()
        self.__lista_jacares = pygame.sprite.Group()
        self.__lista_flores = pygame.sprite.Group()
        self.__lista_consumiveis = pygame.sprite.Group()
        self.__lista_cogumelos = pygame.sprite.Group()
        self.__lista_terreno_aquatico = pygame.sprite.Group()
        self.__all_sprites = pygame.sprite.Group()

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
    def lista_consumiveis(self):
        return self.__lista_consumiveis

    @property
    def lista_cogumelos(self):
        return self.__lista_cogumelos

    @property
    def lista_terreno_aquatico(self):
        return self.__lista_terreno_aquatico

    @property
    def all_sprites(self):
        return self.__all_sprites