from itens.efeitosnojogador import EfeitosNoJogador
import time


marrom = (75, 54, 33)
efeito = 0

class Espinho(EfeitosNoJogador):
    def __init__(self,coordenadax,coordenaday):
        super().__init__("espinho", 15, 10, coordenadax, coordenaday, marrom, efeito)
        self.__efeito = efeito

    
    def aplicar_efeito(self, jogador):
        jogador.alterar_velocidade(self.__efeito)
