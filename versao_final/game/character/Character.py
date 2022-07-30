import pygame

class Character(pygame.sprite.Sprite):
    def __init__(self, altura, largura, coordenadax, coordenaday):
        pygame.sprite.Sprite.__init__(self)
        self.__altura = altura
        self.__largura = largura
        self.__coordenadax = coordenadax
        self.__coordenaday = coordenaday
        self.image = pygame.Surface([altura, largura])
        self.rect = self.image.get_rect()
        self.rect.center = [coordenadax, coordenaday]

        # coordenadas x: 1-direita, 0-parado, -1-esquerda e y: 1-cima, 0-parado, -1-baixo
        self.__direction = pygame.math.Vector2(0, 0)

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
    def direction(self):
        return self.__direction

    @property
    def direction_x(self):
        return self.__direction.x

    @property
    def direction_y(self):
        return self.__direction.y

    def set_direction_x(self, direction):
        self.__direction.x = direction

    def set_direction_y(self, direction):
        self.__direction.y = direction
