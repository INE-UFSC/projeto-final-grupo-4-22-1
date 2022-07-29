from game.character.player.Player import Player

class CollisionConsequences:
    def __init__(self, player):
        #player = player
        teste = 0

    def player_e_inimigo(self, player):
        return "Perdeu!"

    def player_e_parceiro(self, player):
        for flor in player.flores_coletadas:
            if player.flores_coletadas[flor] == True:
                player.aumenta_velocidade(flor.peso)
        player.soltar_flores()

    def player_e_item(self, player, item):
        item.aplicar_efeito(player)

    def player_e_flor(self, player, flor):
        player.flores_coletadas[flor] = player.carry(flor.peso)

    def player_e_water(self, player):
        player.velocidade = player.velocidade_na_agua

    def player_e_ground(self, player):
        player.velocidade = player.velocidade_normal

    def player_e_barreira_x(self, player, tile):
        if player.envenenado == False:
            if player.direction_x == -1:
                player.rect.x = tile.right

            elif player.direction_x == 1:
                player.rect.x = tile.left - player.rect.w
        else:
            if player.direction_x == 1:
                player.rect.x = tile.right

            elif player.direction_x == -1:
                player.rect.x = tile.left - player.rect.w

    def player_e_barreira_y(self, player, tile):
        if player.envenenado == False:
            if player.direction_y == 1:
                player.rect.y = tile.bottom

            elif player.direction_y == -1:
                player.rect.bottom = tile.top
        else:
            if player.direction_y == -1:
                player.rect.y = tile.bottom

            elif player.direction_y == 1:
                player.rect.bottom = tile.top

    def enemy_x(self, enemy, tile):
        if enemy.direction_x == -1:
            enemy.rect.x = tile.right
            enemy.set_counter(4)

        elif enemy.direction_x == 1:
            enemy.rect.x = tile.left - enemy.rect.w
            enemy.set_counter(2)

    def enemy_y(self, enemy, tile):
        if enemy.direction_y == 1:
            enemy.rect.y = tile.bottom
            enemy.set_counter(3)

        elif enemy.direction_y == -1:
            enemy.rect.bottom = tile.top
            enemy.set_counter(1)
