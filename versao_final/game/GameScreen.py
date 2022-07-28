import pygame, random

from game.menus.input_box import InputBox
from game.imageLibrary.ImageLibrary import ImageLibrary

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
# o fundo do terreno ground será verde
VERDE_CLARO = (0, 255, 0)

class GameScreen:
    def __init__(self, controller):
        self.__imagens = ImageLibrary()
        self.__controlador = controller
        
        self.__largura = 1200
        self.__altura = 600
        self.__tela = pygame.display.set_mode((self.__largura, self.__altura))
        pygame.display.set_caption("GRUPO 4")
        self.__ranking = pygame.image.load(self.__imagens.ranking).convert()
        self.__menu = pygame.image.load(self.__imagens.inicial).convert()
        self.__game_over = pygame.image.load(self.__imagens.perdeu).convert()
        self.tamanho_display = self.__largura, self.__altura
        self.display = pygame.display.set_mode(
            self.tamanho_display, pygame.HWSURFACE)

    def desenhar_input_box(self, box):
        self.__tela.blit(box.txt_surface, (box.rect.x+5, box.rect.y+5))
        pygame.draw.rect(self.__tela, box.cor, box.rect, 2)

    def menu(self, box):
        self.__tela.blit(self.__menu, (0,0))
        self.desenhar_input_box(box)

    def game_over(self):
        self.__tela.blit(self.__game_over, (0,0))

    def start(self):
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
    
    def draw_map(self, imagens, lista_coordenadas):
        for imagem in imagens:
            sprite = pygame.image.load(imagens[imagem])
            sprite = pygame.transform.scale(sprite,(100,100))
            for coordenada in lista_coordenadas:
                if coordenada == imagem:
                    for coord in lista_coordenadas[coordenada]:
                        self.__tela.blit(sprite, coord)

    def tamanho_ponto(self, imagem,altura,largura, x, y):
        imagem = pygame.image.load(imagem)
        imagem = pygame.transform.scale(imagem,(altura,largura))
        self.__tela.blit(imagem, (x, y))
    
    def imagem_relogio(self,imagem,x,y):
        self.__tela.blit(imagem, (x, y))

    def tela_ranking(self, ranking):
        self.__tela.blit(self.__ranking, (0,0))
        fonte = pygame.font.SysFont("Times New Roman", 30, True, False)
        lugar = 165
        for posicao in ranking:
            texto = fonte.render("%s: %s, com %s pontos" % (posicao, ranking[posicao][0], ranking[posicao][1]), False, (255,255,255))
            self.__tela.blit(texto, (350, lugar))
            lugar += 95

    @property
    def largura(self):
        return self.__largura

    @property
    def altura(self):
        return self.__altura

    @property
    def tela(self):
        return self.__tela
