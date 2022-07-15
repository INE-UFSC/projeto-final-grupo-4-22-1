import os


class BibliotecaImagens():
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
        self.__agua = os.path.join("Imagens/agua.png")
        self.__terra = os.path.join("Imagens/terra.png")
    
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
    def agua(self):
        return self.__agua
    
    @property 
    def terra(self):
        return self.__terra
