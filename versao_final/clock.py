from TelaJogo import TelaJogo
import pygame
import time
class Clock():
    def __init__(self):
        self.__timer_font = None
        self.__timer_sec = None
        self.__timer_text = None
        self.__tela = TelaJogo(self)
    
    @property
    def timer_font(self):
        return self.__timer_font
    
    @property
    def timer_sec(self):
        return self.__timer_sec
    
    @property
    def timer_text(self):
        return self.__timer_text
    
    def iniciar_clock(self):
        self.__timer_font = pygame.font.SysFont("fontname", 48)
        self.__timer_sec = 120
        self.__timer_text = self.__timer_font.render(
            "02:00", True, ((255, 255, 255)))
        
    def verifica_clock(self):
        if self.__timer_sec > 0:
            self.__timer_sec -= 1
            self.__timer_text = self.__timer_font.render(time.strftime('%M:%S',time.gmtime(self.__timer_sec)),True,((255,255,255)))
        else:
            tempo = True
            return tempo
            



            