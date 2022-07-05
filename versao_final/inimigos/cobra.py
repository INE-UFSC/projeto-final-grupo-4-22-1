from inimigos.inimigo import Inimigo

VERMELHO = 	(139, 0, 0)                      

class Cobra(Inimigo):
    def __init__(self,altura_cobra:int, largura_cobra:int, coordenadax:int, coordenaday_cobra:int, velocidade_cobra:int, dano:int, terreno:str):
        super().__init__(altura_cobra, largura_cobra, coordenadax, coordenaday_cobra, velocidade_cobra, dano, terreno, VERMELHO)
        
    
    

#falta extensão para o eixo Y
#pensando em passar função para controller discutir com o grupo
#rotação de imagem quando implementar eixo Y    
