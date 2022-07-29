import os


class ImageLibrary():
    def __init__(self):
        self.__inicial = os.path.join("game/imageLibrary/Menus_botoes/inicial.png")
        self.__perdeu = os.path.join("game/imageLibrary/Menus_botoes/perdeu.png")
        self.__ranking = os.path.join("game/imageLibrary/Menus_botoes/ranking.png")
        self.__nome = os.path.join("game/imageLibrary/Menus_botoes/nome.png")
        self.__som = os.path.join("game/imageLibrary/Menus_botoes/som.png")
        self.__cobra_direita = os.path.join("game/imageLibrary/images/cobra_direita.png")
        self.__cobra_baixo = os.path.join("game/imageLibrary/images/cobra_baixo.png")
        self.__cobra_esquerda = os.path.join("game/imageLibrary/images/cobra_esquerda.png")
        self.__cobra_cima = os.path.join("game/imageLibrary/images/cobra_cima.png")
        self.__jacare_direita = os.path.join("game/imageLibrary/images/jacare_direita.png")
        self.__jacare_baixo = os.path.join("game/imageLibrary/images/jacare_baixo.png")
        self.__jacare_esquerda = os.path.join("game/imageLibrary/images/jacare_esquerda.png")
        self.__jacare_cima = os.path.join("game/imageLibrary/images/jacare_cima.png")
        self.__water = os.path.join("game/imageLibrary/images/water.png")
        self.__ground = os.path.join("game/imageLibrary/images/ground.png")
        self.__apple = os.path.join("game/imageLibrary/images/apple.png")
        self.__mushroom = os.path.join("game/imageLibrary/images/mushroom.png")
        self.__sunflower = os.path.join("game/imageLibrary/images/sunflower.png")
        self.__jasminen = os.path.join("game/imageLibrary/images/jasminen.png")
        self.__ra = os.path.join("game/imageLibrary/images/ra.png")
        self.__sapo_esquerda = os.path.join("game/imageLibrary/images/sapo_esquerda.png")

    @property
    def ranking(self):
        return self.__ranking

    @property 
    def inicial(self):
        return self.__inicial
    
    @property
    def som(self):
        return self.__som

    @property 
    def nome(self):
        return self.__nome
    
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
    def ra(self):
        return self.__ra

    @property
    def sapo_esquerda(self):
        return self.__sapo_esquerda
