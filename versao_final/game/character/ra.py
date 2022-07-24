from game.character.Character import Character

ROXO = (72, 61, 139)

class Ra(Character):
    def __init__(self, altura_ra:int, largura_ra:int, coordenadax_ra:int, coordenaday_ra:int):
        super().__init__(altura_ra, largura_ra, coordenadax_ra, coordenaday_ra, ROXO)
