import pygame, csv

from game.maps.terreno.Water import Water
from game.maps.terreno.Ground import Ground

from game.character.ra import Ra

from game.character.enemies.cobra import Cobra
from game.character.enemies.jacare import Jacare

from game.items.Apple import Apple
from game.items.Thorm import Thorm
from game.items.Mushroom import Mushroom

from game.items.collectibles.sunflower import Sunflower
from game.items.collectibles.jasminen import Jasminen

from game.items.coordinates.coordenada import Coordenada
from game.GameScreen import GameScreen

from game.maps.MapsLibrary import MapsLibrary


class Mapa:
    def __init__(self):
        self.__lista_parceiro = pygame.sprite.Group()
        self.__lista_cobras = pygame.sprite.Group()
        self.__lista_jacares = pygame.sprite.Group()
        self.__enemies = pygame.sprite.Group()
        self.__lista_flores = pygame.sprite.Group()
        self.__lista_apples = pygame.sprite.Group()
        self.__lista_mushrooms = pygame.sprite.Group()
        self.__lista_thorms = pygame.sprite.Group()
        self.__lista_terreno_water = pygame.sprite.Group()
        self.__all_sprites = pygame.sprite.Group()
        self.__lista_itens = pygame.sprite.Group()
        
        self.__water = Water()
        self.__ground = Ground()

        self.__c1 = Coordenada(0,0)
        self.__screen = GameScreen(self)
        self.__maps = MapsLibrary()
        
    def load_map(self):
        map_list = []
        self.__tile_rects = []
        
        with open(self.__maps.medium, 'r') as file_obj:
            reader_obj = csv.reader(file_obj)
            for row in reader_obj:
                map_list.append(list(row))

        height, width = len(map_list), len(map_list[0])

        self.__original_map = {'ground': [], 'water': [], 'void': []}
        for y, line in enumerate(map_list):
            if line != '':
                for x, tile_name in enumerate(line):
                    self.__original_map[tile_name].append((x*100-100,y*100-100))
                    self.__tile_rects.append((pygame.Rect(x*100-100,y*100-100, 100, 100), tile_name))

    def spawn_flores(self, quantidade):
        for i in range (quantidade):
            self.__c1.coordenadas('coletavel')
            sunflower = Sunflower(self.__c1.coordenadax,self.__c1.coordenaday)
            self.__c1.coordenadas('coletavel')
            jasminen = Jasminen(self.__c1.coordenadax,self.__c1.coordenaday)
            self.__lista_flores.add(sunflower, jasminen)
            self.__all_sprites.add(sunflower, jasminen)

    def spawn_cobras(self):
        cobra = Cobra(50,30,100,100,2,2,'ground')
        self.__lista_cobras.add(cobra)
        self.__enemies.add(cobra)

    def spawn_jacares(self):
        jacare = Jacare(70,40,500,60,10,3,'water')
        self.__lista_jacares.add(jacare)
        self.__enemies.add(jacare)

    def spawn_consumiveis(self, quant_apple, quant_thorm, quant_mushroom):
        for i in range (quant_apple):
            self.__c1.coordenadas('consumivel')
            apple = Apple(self.__c1.coordenadax,self.__c1.coordenaday)
            self.__lista_apples.add(apple)
        for i in range (quant_thorm):
            self.__c1.coordenadas('consumivel')
            thorm = Thorm(self.__c1.coordenadax,self.__c1.coordenaday)
            self.__lista_thorms.add(thorm)
        for i in range (quant_mushroom):
            self.__c1.coordenadas('consumivel')
            mushroom = Mushroom(self.__c1.coordenadax,self.__c1.coordenaday)
            self.__lista_mushrooms.add(mushroom)

        self.__all_sprites.add(apple, thorm,mushroom)
        self.__lista_itens.add(apple, thorm, mushroom)

    def spawn_ra(self):
        ra = Ra(30, 30, 15, 585)
        self.__lista_parceiro.add(ra)
        self.__all_sprites.add(ra)

    def spawn_all(self, quant_apple, quant_thorm, quant_mushroom, quant_flores):
        self.spawn_ra()
        self.spawn_consumiveis(quant_apple, quant_thorm, quant_mushroom)
        self.spawn_jacares()
        self.spawn_cobras()
        self.spawn_flores(quant_flores)

    def reset(self):
        self.__lista_parceiro = pygame.sprite.Group()
        self.__lista_cobras = pygame.sprite.Group()
        self.__lista_jacares = pygame.sprite.Group()
        self.__lista_flores = pygame.sprite.Group()
        self.__lista_apples = pygame.sprite.Group()
        self.__lista_mushrooms = pygame.sprite.Group()
        self.__lista_thorms = pygame.sprite.Group()
        self.__lista_terreno_water = pygame.sprite.Group()
        self.__all_sprites = pygame.sprite.Group()
        self.__enemies = pygame.sprite.Group()
        self.__c1 = Coordenada(0,0)
        self.__lista_itens = pygame.sprite.Group()

    @property
    def lista_itens(self):
        return self.__lista_itens

    @property
    def enimies(self):
        return self.__enemies

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
    def lista_apples(self):
        return self.__lista_apples

    @property
    def lista_thorms(self):
        return self.__lista_thorms

    @property
    def lista_mushrooms(self):
        return self.__lista_mushrooms

    @property
    def lista_terreno_water(self):
        return self.__lista_terreno_water

    @property
    def all_sprites(self):
        return self.__all_sprites

    @property
    def original_map(self):
        return self.__original_map

    @property
    def water_sprite(self):
        return self.__water.sprite

    @property
    def ground_sprite(self):
        return self.__ground.sprite

    @property
    def tile_rects(self):
        return self.__tile_rects
