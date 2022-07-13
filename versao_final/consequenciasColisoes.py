from player import Player

class ConsequenciasColisoes:
    def __init__(self, jogador):
        self.__jogador = jogador

    def jogador_e_inimigo(self):
        return "Perdeu!"

    def jogador_e_parceiro(self):
        for flor in self.__jogador.flores_coletadas:
            if self.__jogador.flores_coletadas[flor] == True:
                self.__jogador.aumenta_velocidade(flor.peso)
        self.__jogador.soltar_flores()

    def jogador_e_espinho(self):
        self.__jogador.aumenta_velocidade(-3)

    def jogador_e_cogumelo(self):
        self.__jogador.debuff()

    def jogador_e_maca(self):
        if self.__jogador.velocidade < 0:
            self.__jogador.debuff()
        self.__jogador.aumenta_velocidade(3)

    def jogador_e_flor(self, flor):
        self.__jogador.flores_coletadas[flor] = self.__jogador.carry(flor.peso)
