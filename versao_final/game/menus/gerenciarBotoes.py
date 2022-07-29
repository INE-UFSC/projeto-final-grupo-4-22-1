import pygame
from game.menus.button import Button
from game.GameScreen import GameScreen
from game.ranking.Ranking import Ranking
from game.menus.input_box import InputBox
from game.som.Som import Som

class GerenciarBotoes():
    def __init__(self):
        self.__tela = GameScreen(self)
        self.__buttonSair = Button(470,250,280,60)
        self.__buttonSom = Button(470,335,280,60)
        self.__buttonRanking = Button(470,425,280,60)
        self.__som = Som()
    
    @property
    def usuario(self):
        return self.__usuario
    
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.__buttonSair.rect.collidepoint(event.pos):
                teste = self.tela_inicial()
                if teste == 0:
                    return 0
                
            if self.__buttonSom.rect.collidepoint(event.pos):
                self.tela_som()
    
            if self.__buttonRanking.rect.collidepoint(event.pos):
                self.tela_ranking()
    
    def tela_inicial(self):
        buttonIniciar = Button(490,350,220,50)
        input_box = InputBox(410,268,370,46)
        self.__usuario = ''
        menu = True
        while menu:
            self.__tela.nome(input_box)
            for event in self.__tela.ler():
                if event.type == pygame.QUIT:
                    self.__tela.fechar()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if buttonIniciar.rect.collidepoint(event.pos):
                        self.__usuario = input_box.texto
                        return 0
                input_box.handle_event(event)
            self.__tela.update()
        pygame.time.Clock().tick(30)
    
    def tela_som(self):
        buttonDesligado = Button(510,375,150,60)
        buttonLigado = Button(510,270,150,60)
        menu = True
        while menu:
            self.__tela.som()
            for event in self.__tela.ler():
                if event.type == pygame.QUIT:
                    self.__tela.fechar()
                if event.type == pygame.KEYDOWN:
                    return 
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if buttonDesligado.rect.collidepoint(event.pos):
                        self.__som.pause()
                    elif buttonLigado.rect.collidepoint(event.pos):
                        self.__som.unpause()
            self.__tela.update()
        pygame.time.Clock().tick(30)
    
    def tela_ranking(self):
        menu = True
        while menu:
            self.__tela.ranking()
            ranking  = Ranking()
            self.__tela.tela_ranking(ranking.ranking)
            for event in self.__tela.ler():
                if event.type == pygame.QUIT:
                    self.__tela.fechar()
                if event.type == pygame.KEYDOWN:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_r:
                            ranking.reset_ranking()
                        else:
                            return 
            self.__tela.update()
        pygame.time.Clock().tick(30)