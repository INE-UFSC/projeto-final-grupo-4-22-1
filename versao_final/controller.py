from operator import index
from TelaJogo import TelaJogo
from ranking import Ranking
from rankingDAO import RankingDAO
import pygame
from pygame.locals import *
from inimigos import Inimigo

from terreno.aquatico import Aquatico
from sapo import Sapo
from ra import Ra

from inimigos.cobra import Cobra
from inimigos.jacare import Jacare
import random

from itens.girassol import Girassol
from itens.jasmin import Jasmin
from itens.maca import Maca
from itens.espinho import Espinho
from itens.cogumelo import Cogumelo

from coordenada import Coordenada
#c_flor = Coordenada(0,0,0)
#c_item = Coordenada(0,0,0)
c1 = Coordenada(0,0,0)


# TODO: precisamos verificar se essa combinação de coordenadas que criamos p/ cada item já está sendo usada, pq se já estiver teremos que criar novas coordenadas até todas serem diferentes (isso é no arquivos do item, só deixei  comentário aqui, pq sempre usamos esse arquivo)


class GameController:
    def __init__(self):
        self.__rankingDAO = RankingDAO()
        self.__ranking = Ranking(self.__rankingDAO)

        self.__tela = TelaJogo(self)
        self.__clock = pygame.time.Clock()
        
        self.__lista_player = pygame.sprite.Group()
        self.__jogador = None

        self.__lista_parceiro = pygame.sprite.Group()
        self.__colisoes_parceiro = None

        self.__lista_cobras = pygame.sprite.Group()
        self.__colisoes_cobra = None

        self.__lista_jacares = pygame.sprite.Group()
        self.__colisoes_jacare = None

        self.__lista_flores = pygame.sprite.Group()
        self.__colisoes_flores = None

        self.__lista_consumiveis = pygame.sprite.Group()
        self.__colisoes_consumiveis = None

        self.__lista_cogumelos = pygame.sprite.Group()
        self.__colisoes_cogumelos = None

        self.__lista_terreno_aquatico = pygame.sprite.Group()
        self.__colisoes_terreno_aquatico = None
        
        self.__all_sprites = pygame.sprite.Group()
        
        #chave é o objeto flor e o valor é bool p/ saber se seu peso foi ou não descontado da velocidade do sapo
        self.__flores_coletadas = {}

    def iniciar_menu(self):
        self.__tela.iniciar()
        self.__tela.menu()
        self.__usuario = ''
        clock = pygame.time.Clock()
        font = pygame.font.Font(None, 32)
        menu = True
        color_inactive = pygame.Color('lightskyblue3')
        color_active = pygame.Color('dodgerblue2')
        color = color_inactive
        active = False
        while menu:
            self.__clock.tick(40)
            self.__tela.update()
            input_box = self.__tela.input_box()
            for event in self.__tela.ler():
                if event.type == pygame.QUIT:
                    self.__tela.fechar()
                if event.type == pygame.KEYDOWN:
                    if event.key == K_SPACE:
                        return self.iniciar()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if input_box.collidepoint(event.pos):
                        active = True
                    else:
                        active = False
                if event.type == pygame.KEYDOWN:
                    if active:
                        if event.key == pygame.K_RETURN:
                            print(self.__usuario)
                        elif event.key == pygame.K_BACKSPACE:
                            self.__usuario = self.__usuario[:-1]
                        else:
                            self.__usuario += event.unicode
            self.__tela.menu()
            txt_surface = font.render(self.__usuario, True, (233,233,233))
            pygame.draw.rect(self.__tela.tela, (0,0,0), input_box, 2)
            self.__tela.tela.blit(txt_surface, (input_box.x+5, input_box.y+5))
            pygame.display.flip()
            clock.tick(30)

    def iniciar(self):
        self.__jogador = Sapo()
        ra = Ra()
        cobra = Cobra(50,30,100,100,2,2,'terrestre')

        jacare = Jacare(70,40,500,60,10,3,'aquatico')
        
        aquatico = Aquatico()

        self.__lista_terreno_aquatico.add(aquatico)
        self.__lista_player.add(self.__jogador)
        self.__lista_parceiro.add(ra)
        self.__lista_cobras.add(cobra)
        self.__lista_jacares.add(jacare)
        
        self.__all_sprites.add(aquatico, self.__jogador, ra)
        
        #FIXME: só para o mvp, dps isso dependerá da fase (que ainda não foi implementada)
        for flor in range(0, 6):
            #print("aaa")
            #print(self.__all_sprites)
            c1.coordenadas()
            girassol = Girassol(c1.coordenadax,c1.coordenaday)
            c1.coordenadas()
            jasmin = Jasmin(c1.coordenadax,c1.coordenaday)
            
            self.__lista_flores.add(girassol, jasmin)
            self.__all_sprites.add(girassol, jasmin)
        
        for cons in range(0,4):
            c1.coordenadas()
            maca = Maca(c1.coordenadax,c1.coordenaday)
            c1.coordenadas()
            espinho = Espinho(c1.coordenadax,c1.coordenaday)
            c1.coordenadas()
            cogumelo = Cogumelo(c1.coordenadax,c1.coordenaday)

            self.__lista_consumiveis.add(maca, espinho)
            self.__lista_cogumelos.add(cogumelo)

            self.__all_sprites.add(maca, espinho,cogumelo)
        
        print(self.__all_sprites)
        self.__tela.iniciar()
        rodando = True
        
        while rodando:  
            self.__clock.tick(40)
            self.__tela.colorir()
            self.__tela.desenhar(self.__all_sprites)
            if self.colisoes() == 'Perdeu!':
                break
<<<<<<< Updated upstream
=======
            cobra.movimento(50,2,3,300,550,100,20,250,"Imagens/cobra_direita.png","Imagens/cobra_baixo.png","Imagens/cobra_esquerda.png","Imagens/cobra_cima.png")
            jacare.movimento(15,4,5,600,500,500,0,80,"Imagens/jacare_direita.png","Imagens/jacare_baixo.png","Imagens/jacare_esquerda.png","Imagens/jacare_cima.png")
>>>>>>> Stashed changes
            
            distancia_cobra = cobra.distancia_ponto(self.__jogador.rect.x,self.__jogador.rect.y,cobra.rect.x,cobra.rect.y)
            distancia_jacare = jacare.distancia_ponto(self.__jogador.rect.x,self.__jogador.rect.y,jacare.rect.x,jacare.rect.y)
            cobra.movimento(50,2,3,300,550,100,20,250,"versao_final/Imagens/cobra_direita.png","versao_final/Imagens/cobra_baixo.png","versao_final/Imagens/cobra_esquerda.png","versao_final/Imagens/cobra_cima.png",distancia_cobra,self.__jogador.rect.x,self.__jogador.rect.y)
            jacare.movimento(15,4,5,600,500,500,0,80,"versao_final/Imagens/jacare_direita.png","versao_final/Imagens/jacare_baixo.png","versao_final/Imagens/jacare_esquerda.png","versao_final/Imagens/jacare_cima.png",distancia_jacare,self.__jogador.rect.x,self.__jogador.rect.y)
            

            for event in self.__tela.ler():
                if event.type == pygame.QUIT:
                    self.__tela.fechar()
                if event.type == pygame.KEYDOWN:
                    if event.key == K_LEFT and 0 <= self.__jogador.rect.x:
                        self.__jogador.mover_esquerda()
                    if event.key == K_RIGHT and self.__tela.largura - self.__jogador.largura >= self.__jogador.rect.x:
                        self.__jogador.mover_direita()
                    if event.key == K_UP and 0 <= self.__jogador.rect.y:
                        self.__jogador.mover_cima()
                    if event.key == K_DOWN and self.__tela.altura - self.__jogador.altura >= self.__jogador.rect.y:
                        self.__jogador.mover_baixo()

            if pygame.key.get_pressed()[K_LEFT] and 0 <= self.__jogador.rect.x:
                self.__jogador.mover_esquerda()
            if pygame.key.get_pressed()[K_RIGHT] and self.__tela.largura - self.__jogador.largura >= self.__jogador.rect.x:
                self.__jogador.mover_direita()
            if pygame.key.get_pressed()[K_UP] and 0 <= self.__jogador.rect.y:
                self.__jogador.mover_cima()
            if pygame.key.get_pressed()[K_DOWN] and self.__tela.altura - self.__jogador.altura >= self.__jogador.rect.y:
                self.__jogador.mover_baixo()

            self.__tela.update()
        self.game_over()

    def game_over(self):
        self.atualiza_ranking(self.__usuario, 200)
        self.__tela.game_over()
        game_over = True
        while game_over:
            self.__clock.tick(40)
            self.__tela.update()
            for event in self.__tela.ler():
                if event.type == pygame.QUIT:
                    self.__tela.fechar()
                if event.type == pygame.KEYDOWN:
                    if event.key == K_SPACE:
                        return self.restart()

    def restart(self):
        self.__lista_player = pygame.sprite.Group()
        self.__jogador = None

        self.__lista_parceiro = pygame.sprite.Group()
        self.__colisoes_parceiro = None

        self.__lista_cobras = pygame.sprite.Group()
        self.__colisoes_cobra = None

        self.__lista_jacares = pygame.sprite.Group()
        self.__colisoes_jacare = None

        self.__lista_flores = pygame.sprite.Group()
        self.__colisoes_flores = None

        self.__lista_consumiveis = pygame.sprite.Group()
        self.__colisoes_consumiveis = None

        self.__lista_cogumelos = pygame.sprite.Group()
        self.__colisoes_cogumelos = None

        self.__lista_terreno_aquatico = pygame.sprite.Group()
        self.__colisoes_terreno_aquatico = None
        
        self.__all_sprites = pygame.sprite.Group()
        
        #chave é o objeto flor e o valor é bool p/ saber se seu peso foi ou não descontado da velocidade do sapo
        self.__flores_coletadas = {}
        self.iniciar()

    def colisoes(self):
        self.__colisoes_cobra = pygame.sprite.spritecollide(self.__jogador, self.__lista_cobras, False)
        self.__colisoes_jacare = pygame.sprite.spritecollide(self.__jogador, self.__lista_jacares, False)
        #jogador.flores = pygame.sprite.spritecollide(self.__jogador, self.__lista_girassois, True)
        self.__colisoes_flores = pygame.sprite.spritecollide(self.__jogador, self.__lista_flores, True)
        self.__colisoes_terreno_aquatico = pygame.sprite.spritecollide(self.__jogador, self.__lista_terreno_aquatico, False)
        self.__colisoes_parceiro = pygame.sprite.spritecollide(self.__jogador, self.__lista_parceiro, False)
        self.__colisoes_consumiveis = pygame.sprite.spritecollide(self.__jogador, self.__lista_consumiveis, True)
        self.__colisoes_cogumelos = pygame.sprite.spritecollide(self.__jogador,self.__lista_cogumelos,True)
        if self.__colisoes_cobra:
            return("Perdeu!")
        elif self.__colisoes_jacare:
            return("Perdeu!")
        elif self.__colisoes_flores:
            flor = self.__colisoes_flores[0]
            self.__flores_coletadas[flor] = self.__jogador.carry(flor.peso)
        elif self.__colisoes_consumiveis:
            if self.__jogador.velocidade<0:
                self.__jogador.debuff()
            self.__jogador.aumenta_velocidade(3)
        elif self.__colisoes_cogumelos:
            self.__jogador.debuff()
        elif self.__colisoes_parceiro:
            remove = []
            for flor in self.__flores_coletadas:
                if self.__flores_coletadas[flor] == True:
                    self.__jogador.aumenta_velocidade(flor.peso)
            self.__flores_coletadas = {}

    def atualiza_ranking(self, usuario, pontuacao):
        self.__ranking.atualiza_ranking(usuario, pontuacao)
        self.__rankingDAO.replace(self.__ranking.ranking())
        print(self.__rankingDAO.get_ranking())