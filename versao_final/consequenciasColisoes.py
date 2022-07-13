from player import Player

class ConsequenciasColisoes:
    def __init__(self):
        pass

    def jogador_e_inimigo(self):
        return "Perdeu!"

    def jogador_e_parceiro(self, jogador):
        for flor in jogador.flores_coletadas:
            if jogador.flores_coletadas[flor] == True:
                jogador.aumenta_velocidade(flor.peso)
        jogador.soltar_flores()

    def jogador_e_espinho(self, jogador):
        jogador.aumenta_velocidade(-3)

    def jogador_e_cogumelo(self, jogador):
        jogador.debuff()

    def jogador_e_maca(self, jogador):
        if jogador.velocidade < 0:
            jogador.debuff()
        jogador.aumenta_velocidade(3)

    def jogador_e_flor(self, jogador, flor):
        jogador.flores_coletadas[flor] = jogador.carry(flor.peso)
