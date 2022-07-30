from pygame import mixer
import pygame
import os

class Som():
    def __init__(self):
        mixer.init()
        pygame.mixer.music.set_volume(0.05)
        self.__SomFundo = os.path.join("game/som/musica/musica_fundo.mp3")
        self.__SomInicial = os.path.join("game/som/musica/musica_inicial.wav")
        self.__SomPerdeu = os.path.join("game/som/musica/musica_final_perdeu.ogg")
        self.__SomGanhou = os.path.join("game/som/musica/musica_final_ganhou.mp3")

    def iniciar(self,musica):
        if(musica==0):
            mixer.music.load(self.__SomFundo)
        elif(musica==1):
            mixer.music.load(self.__SomInicial)
        elif(musica==2):
            mixer.music.load(self.__SomPerdeu)
        elif(musica==3):
            mixer.music.load(self.__SomGanhou)
        mixer.music.play(-1)

    def unpause(self):
        pygame.mixer.music.set_volume(0.05)

    def pause(self):
        pygame.mixer.music.set_volume(0)
