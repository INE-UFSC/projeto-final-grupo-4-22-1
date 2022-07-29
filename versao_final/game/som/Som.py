from pygame import mixer
import os

class Som():
    def __init__(self):
        self.__SomFundo = os.path.join("game\som\musica\musica_fundo.mp3")
        self.__SomInicial = os.path.join("game\som\musica\musica_inicial.mp3")
        self.__SomPerdeu = os.path.join("game\som\musica\musica_final.mp3")
        self.__Somsunflower = os.path.join("game\som\musica\sunflower.mp3")
    
    def iniciar(self,musica):
        mixer.init()
        if(musica==0):
            mixer.music.load(self.__SomFundo)
        elif(musica==1):
            mixer.music.load(self.__SomInicial)
        elif(musica==2):
            mixer.music.load(self.__SomPerdeu)
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




    
    
    