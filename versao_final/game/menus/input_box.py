import pygame

class InputBox:

    def __init__(self, x, y, w, h, texto = ''):
        self.__fonte = pygame.font.Font(None, 40)
        self.__rect = pygame.Rect(x, y, w, h)
        self.__color = (255,255,255)
        self.__texto = texto
        self.__txt_surface = self.__fonte.render('', True, (0,0,0))
        self.__active = False

    def handle_event(self, event):
        print("Chegou")
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.__rect.collidepoint(event.pos):
                self.__active = not self.__active
            else:
                self.__active = False
        if event.type == pygame.KEYDOWN:
            if self.__active:
                if event.key == pygame.K_RETURN:
                    print(self.__texto)
                    self.__texto = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.__texto = self.__texto[:-1]
                else:
                    self.__texto += event.unicode
                self.__txt_surface = self.__fonte.render(self.__texto, True, (0,0,0))

    @property
    def txt_surface(self):
        return self.__txt_surface

    @property
    def rect(self):
        return self.__rect

    @property
    def cor(self):
        return self.__color

    @property
    def texto(self):
        return self.__texto
