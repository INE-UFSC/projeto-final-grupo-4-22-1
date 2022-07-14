from itens.efeitosnojogador import EfeitosNoJogador
import time

cinza = (124, 134, 153)
efeito = -1


class Cogumelo(EfeitosNoJogador):
    def __init__(self,coordenadax,coordenaday):
        super().__init__("cogumelo", 15, 10,coordenadax,coordenaday, cinza, efeito)
        self.__efeito = efeito
    
    def aplicar_efeito(self, jogador):
        jogador.alterar_velocidade(self.__efeito)
