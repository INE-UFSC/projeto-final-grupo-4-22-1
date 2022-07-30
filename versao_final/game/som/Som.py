from pygame import mixer
import pygame
import os

class Som():
    def __init__(self):
        self.__SomFundo = os.path.join("game/som/musica/musica_fundo.mp3")
        self.__SomInicial = os.path.join("game/som/musica/musica_inicial.wav")
        self.__SomPerdeu = os.path.join("game/som/musica/musica_final_perdeu.ogg")
        self.__SomGanhou = os.path.join("game/som/musica/musica_final_ganhou.mp3")

    def iniciar(self,musica):
        mixer.init()
        pygame.mixer.music.set_volume(0.05)
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
        mixer.music.unpause()
    
    def pause(self):
        mixer.music.pause()
    
    def elemento(self):
        mixer.init()
        mixer.music.load(self.__Somsunflower)
        mixer.music.play(1)
    """caso vcs queiram testar o código de música basta colocar 
    pip install pygame==1.9.6
    no cmd e reiniciar a maquina
    ai basta descomentar o código do controller e testar"""




    
    
    