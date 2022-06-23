from itens.efeitobonus import EfeitoBonus



class Maca(EfeitoBonus):
    def __init__(self, nome, largura, altura, coordenadax, coordenaday, bonus):
        super().__init__(nome, largura, altura, coordenadax, coordenaday, bonus)
