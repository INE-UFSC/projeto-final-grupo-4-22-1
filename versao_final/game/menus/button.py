import pygame

class Button:

    def __init__(self, x, y, w, h):
        self.__font = pygame.font.Font(None,35)
        self.__color = (255,255,255)
        self.__color_light = (255,255,255)
        self.__rect = pygame.Rect(x ,y ,w ,h)
        self.__text = self.__font.render('quit' , True , self.__color)

    @property
    def font(self):
        return self.__font
    
    @property
    def rect(self):
        return self.__rect
    
    @property
    def color(self):
        return self.__color
    
    @property
    def color_light(self):
        return self.__color_light
    
    @property
    def text(self):
        return self.__text

    
    
            
    
      
        