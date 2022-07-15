import pygame

from bibliotecaImagens import BibliotecaImagens

class Terrestre(pygame.sprite.Sprite):
    def __init__(self):#, altura, largura, coordenadax, coordenaday, AZUL):
        self.__altura = 100
        self.__largura = 100
        #self.__coordenadax = coordenadax
        #self.__coordenaday = coordenaday
        #self.__cor = AZUL

        self.__vitorias_regias = []
        pygame.sprite.Sprite.__init__(self)
        #self.image = pygame.Surface([largura, altura])
        #self.image.fill(self.__cor)
        #self.rect = self.image.get_rect()
        #self.rect.center = [self.__coordenadax, self.__coordenaday]
        
        self.__imagens = BibliotecaImagens()
        self.__sprite = self.__imagens.terra

    @property
    def altura(self):
        return self.__altura
    
    @property
    def largura(self):
        return self.__largura

    '''@property
    def coordenadax(self):
        return self.__coordenadax

    @property
    def coordenaday(self):
        return self.__coordenaday'''

    @property
    def sprite(self):
        return self.__sprite
