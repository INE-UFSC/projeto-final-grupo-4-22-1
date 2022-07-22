import os


class ImageLibrary():
    def __init__(self):
        self.__inicial = os.path.join("Menus_botoes/1.png")
        self.__perdeu = os.path.join("Menus_botoes/perdeu.png")
        self.__cobra_direita = os.path.join("Imagens/cobra_direita.png")
        self.__cobra_baixo = os.path.join("Imagens/cobra_baixo.png")
        self.__cobra_esquerda = os.path.join("Imagens/cobra_esquerda.png")
        self.__cobra_cima = os.path.join("Imagens/cobra_cima.png")
        self.__jacare_direita = os.path.join("Imagens/jacare_direita.png")
        self.__jacare_baixo = os.path.join("Imagens/jacare_baixo.png")
        self.__jacare_esquerda = os.path.join("Imagens/jacare_esquerda.png")
        self.__jacare_cima = os.path.join("Imagens/jacare_cima.png")
        self.__water = os.path.join("Imagens/water.png")
        self.__ground = os.path.join("Imagens/ground.png")
        self.__maca = os.path.join("Imagens/maca.png")
        self.__cogumelo = os.path.join("Imagens/cogumelo.png")
        self.__girassol = os.path.join("Imagens/girassol.png")
        self.__jasmin = os.path.join("Imagens/jasmin.png")
        self.__espinho = os.path.join("Imagens/espinho.png")
    
    @property 
    def inicial(self):
        return self.__inicial
    
    @property 
    def perdeu(self):
        return self.__perdeu

    @property 
    def cobra_direita(self):
        return self.__cobra_direita
    
    @property 
    def cobra_baixo(self):
        return self.__cobra_baixo
    
    @property 
    def cobra_esquerda(self):
        return self.__cobra_esquerda
    
    @property 
    def cobra_cima(self):
        return self.__cobra_cima
    
    @property 
    def jacare_direita(self):
        return self.__jacare_direita
    
    @property 
    def jacare_baixo(self):
        return self.__jacare_baixo
    
    @property 
    def jacare_esquerda(self):
        return self.__jacare_esquerda
    
    @property 
    def jacare_cima(self):
        return self.__jacare_cima

    @property 
    def water(self):
        return self.__water
    
    @property 
    def ground(self):
        return self.__ground

    @property
    def maca(self):
        return self.__maca
    @property
    def cogumelo(self):
        return self.__cogumelo
    @property
    def girassol(self):
        return self.__girassol
    @property
    def jasmin(self):
        return self.__jasmin
    @property
    def espinho(self):
        return self.__espinho