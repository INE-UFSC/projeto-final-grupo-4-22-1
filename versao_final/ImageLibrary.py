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
        self.__apple = os.path.join("Imagens/apple.png")
        self.__mushroom = os.path.join("Imagens/mushroom.png")
        self.__sunflower = os.path.join("Imagens/sunflower.png")
        self.__jasminen = os.path.join("Imagens/jasminen.png")
        self.__thorm = os.path.join("Imagens/thorm.png")
    
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
    def apple(self):
        return self.__apple
    @property
    def mushroom(self):
        return self.__mushroom
    @property
    def sunflower(self):
        return self.__sunflower
    @property
    def jasminen(self):
        return self.__jasminen
    @property
    def thorm(self):
        return self.__thorm