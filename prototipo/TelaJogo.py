import pygame, random

largura = 700
altura = 420
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERDE = (0, 255, 0)

class TelaJogo:
    def __init__(self, controller):
        self.__controlador = controller
        self.__largura = largura
        self.__altura = altura
        self.__tela = pygame.display.set_mode((self.__largura, self.__altura))
        pygame.display.set_caption("GRUPO 4")

    @property
    def largura(self):
        return self.__largura

    @property
    def altura(self):
        return self.__altura

    def iniciar(self):
        pygame.init()

    def colorir(self):
        self.__tela.fill(VERDE)

    def desenhar(self, jogador):
        pygame.draw.rect(self.__tela, BRANCO, pygame.Rect(jogador.coordenadax, jogador.coordenaday, jogador.altura, jogador.largura))

    def ler(self):
        return pygame.event.get()

    def update(self):
        pygame.display.update()

    def fechar(self):
        pygame.quit()
        exit()
