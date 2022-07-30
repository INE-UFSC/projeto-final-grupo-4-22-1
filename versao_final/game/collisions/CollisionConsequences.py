from game.character.player.Player import Player

class CollisionConsequences:
    def __init__(self, player):
        self.__player = player

    def player_e_inimigo(self):
        return "Perdeu!"

    def player_e_parceiro(self):
        for flor in self.__player.flores_coletadas:
            if self.__player.flores_coletadas[flor] == True:
                self.__player.aumenta_velocidade(flor.peso)
        self.__player.soltar_flores()

    def player_e_item(self, item):
        item.aplicar_efeito(self.__player)

    def player_e_flor(self, flor):
        self.__player.flores_coletadas[flor] = self.__player.carry(flor.peso)

    def player_e_water(self):
        self.__player.velocidade = self.__player.velocidade_na_agua

    def player_e_ground(self):
        self.__player.velocidade = self.__player.velocidade_normal

    def player_e_barreira_x(self, tile):
        if self.__player.envenenado == False:
            if self.__player.direction_x == -1:
                self.__player.rect.x = tile.right

            elif self.__player.direction_x == 1:
                self.__player.rect.x = tile.left - self.__player.rect.w
        else:
            if self.__player.direction_x == 1:
                self.__player.rect.x = tile.right

            elif self.__player.direction_x == -1:
                self.__player.rect.x = tile.left - self.__player.rect.w

    def player_e_barreira_y(self, tile):
        if self.__player.envenenado == False:
            if self.__player.direction_y == 1:
                self.__player.rect.y = tile.bottom

            elif self.__player.direction_y == -1:
                self.__player.rect.bottom = tile.top
        else:
            if self.__player.direction_y == -1:
                self.__player.rect.y = tile.bottom

            elif self.__player.direction_y == 1:
                self.__player.rect.bottom = tile.top

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
