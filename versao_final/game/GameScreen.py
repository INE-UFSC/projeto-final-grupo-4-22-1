import pygame

from game.menus.input_box import InputBox
from game.imageLibrary.ImageLibrary import ImageLibrary


class GameScreen:
    def __init__(self):
        self.__imagens = ImageLibrary()
        
        self.__largura = 1200
        self.__altura = 600
        self.__tela = pygame.display.set_mode((self.__largura, self.__altura))
        pygame.display.set_caption("GRUPO 4")
        
        self.__menu = pygame.image.load(self.__imagens.inicial).convert()
        self.__game_over = pygame.image.load(self.__imagens.perdeu).convert()
        self.__som = pygame.image.load(self.__imagens.som).convert()
        self.__ranking = pygame.image.load(self.__imagens.ranking).convert()
        self.__nome = pygame.image.load(self.__imagens.nome).convert()
        self.__venceu = pygame.image.load(self.__imagens.venceu).convert()
        self.__telas = {"ranking": self.__ranking, "menu": self.__menu, "game_over": self.__game_over, "som": self.__som, "nome": self.__nome, "venceu": self.__venceu}

        self.tamanho_display = self.__largura, self.__altura
        self.display = pygame.display.set_mode(
            self.tamanho_display, pygame.HWSURFACE)

    def desenhar_input_box(self, box):
        self.__tela.blit(box.txt_surface, (box.rect.x+5, box.rect.y+5))
        pygame.draw.rect(self.__tela, box.cor, box.rect, 2)

    def draw_screen(self, nome):
        self.__tela.blit(self.__telas[nome], (0,0))

    def nome(self,box,):
        self.__tela.blit(self.__nome, (0,0))
        self.desenhar_input_box(box)

    def start(self):
        pygame.init()

    def draw_sprites(self, sprites):
        for sprite in sprites:
            image = sprite.sprite
            image = pygame.transform.scale(image,(sprite.altura,sprite.largura))
            self.__tela.blit(image, (sprite.rect.x, sprite.rect.y))

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

    def tamanho_ponto(self, image,altura,largura, x, y):
        image = pygame.image.load(image)
        image = pygame.transform.scale(image,(altura,largura))
        self.__tela.blit(image, (x, y))
    
    def image_relogio(self,imagem,x,y):
        self.__tela.blit(imagem, (x, y))
    
    def tela_ranking(self, ranking):
        fonte = pygame.font.SysFont("Arial", 25, True, False)
        lugar = 90
        for posicao in ranking:
            texto = fonte.render("%s: %s, com %s pontos" % (posicao, ranking[posicao][0], ranking[posicao][1]), False, (255,255,255))
            lugar += 85
            self.__tela.blit(texto, (450, lugar))

    @property
    def largura(self):
        return self.__largura

    @property
    def altura(self):
        return self.__altura

    @property
    def tela(self):
        return self.__tela
