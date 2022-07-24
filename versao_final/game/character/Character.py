import pygame


class Character(pygame.sprite.Sprite):
    def __init__(self, altura, largura, coordenadax, coordenaday, COR):
        self.__altura = altura
        self.__largura = largura
        self.__coordenadax = coordenadax
        self.__coordenaday = coordenaday
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([altura, largura])
        self.image.fill(COR)
        self.rect = self.image.get_rect()
        self.rect.center = [coordenadax, coordenaday]
        
        self.__direcao_vertical = 0
        self.__direcao_horizontal = 0
        

    @property
    def altura(self):
        return self.__altura

    @property
    def largura(self):
        return self.__largura

    @property
    def coordenadax(self):
        return self.__coordenadax

    @coordenadax.setter
    def coordenadax(self, coordenadax):
        self.__coordenadax = coordenadax

    @property
    def coordenaday(self):
        return self.__coordenaday

    def moverx(self, velocidade):
        self.__coordenadax += velocidade

    def movery(self, velocidade):
        self.__coordenaday += velocidade

    @property
    def direcao_vertical(self):
        return self.__direcao_vertical

    @property
    def direcao_horizontal(self):
        return self.__direcao_horizontal

    @direcao_vertical.setter
    def direcao_vertical(self, direcao):
        self.__direcao_vertical = direcao

    @direcao_horizontal.setter
    def direcao_horizontal(self, direcao):
        self.__direcao_horizontal = direcao
