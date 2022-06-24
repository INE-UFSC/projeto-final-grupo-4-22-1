import pygame, random

#site pras cores https://celke.com.br/artigo/tabela-de-cores-html-nome-hexadecimal-rgb
PRETO = (0, 0, 0)
# o jogador será branco
BRANCO = (255, 255, 255)
#o crush do jogador será roxo
ROXO = (72, 61, 139)
#o inimigo 1 (cobra) será vermelho
VERMELHO = 	(139, 0, 0)
#o inimigo 2 (jacaré) será verde escuro
VERDE_ESCURO = (0, 100, 0)
#as flores serão rosas
ROSA = (218, 112, 214)
#o fundo do terreno aquático será azul
AZUL = (0, 191, 255)
# o fundo do terreno terrestre será verde
VERDE_CLARO = (0, 255, 0)

class TelaJogo:
    def __init__(self, controller):
        self.__controlador = controller
        self.__largura = 1200
        self.__altura = 800
        self.__tela = pygame.display.set_mode((self.__largura, self.__altura))
        pygame.display.set_caption("GRUPO 4")

    @property
    def largura(self):
        return self.__largura

    @property
    def altura(self):
        return self.__altura

    @property
    def tela(self):
        return self.__tela

    def iniciar(self):
        pygame.init()

    def colorir(self):
        self.__tela.fill(VERDE_CLARO)

    def desenhar(self, sprites):
        sprites.draw(self.__tela)

    def ler(self):
        return pygame.event.get()

    def update(self):
        pygame.display.update()

    def fechar(self):
        pygame.quit()
        exit()
