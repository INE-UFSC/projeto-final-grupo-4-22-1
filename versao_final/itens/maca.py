from itens.efeitosnojogador import EfeitosNoJogador
import time

vermelho = (255, 0, 0)
efeito = 2


class Maca(EfeitosNoJogador):
    def __init__(self,coordenadax,coordenaday):
        super().__init__("maca", 15, 10, coordenadax,coordenaday, vermelho, efeito)
        self.__efeito = efeito
    
    def aplicar_efeito(self, jogador):
        jogador.alterar_velocidade(self.__efeito)
