import pygame , sys ,math
from random import*
from pygame.locals import *
import pyganim

class Game():
    def __init__(self):
        self.size = 800,600
        self.width = 800
        self.height = 600        
        self.screen = pygame.display.set_mode(self.size)
        self.clock = pygame.time.Clock()
        
class Personagem(Game):
    def __init__(self):
        self.keys = [False, False, False, False]
        self.playerpos=[120,420]
        self.shurikens=[]
        self.speed = 4 
        self.vida_azukay = 3
        self.player_imagem = pygame.image.load("Sprites/azukay_front/frente.png")
        self.player_descendo = pygame.image.load("Sprites/azukay_front/frente.png")
        self.player_esquerda = pygame.image.load("Sprites/azukay_left/esquerda1.png")
        self.player_direita = pygame.image.load("Sprites/azukay_right/direita1.png")
        self.player_subindo = pygame.image.load("Sprites/azukay_back/costas_andando.png")
        self.shuriken = pygame.image.load("Sprites/shuriken/shuriken.png")
        
        self.cima = pyganim.PygAnimation([("Sprites/azukay_back/costas_andando.png",0.1),
                                     ("Sprites/azukay_back/costas_andando1.png",0.1),
                                     ("Sprites/azukay_back/costas_andando2.png",0.1)])
        
        self.baixo = pyganim.PygAnimation([("Sprites/azukay_front/frente.png",0.1),
                                      ("Sprites/azukay_front/frente_andando1.png",0.1),
                                      ("Sprites/azukay_front/frente_andando2.png",0.1)])
        
        self.esquerda = pyganim.PygAnimation([("Sprites/azukay_left/esquerda1.png",0.1),
                                         ("Sprites/azukay_left/esquerda2.png",0.1),
                                         ("Sprites/azukay_left/esquerda3.png",0.1)])
        
        self.direita = pyganim.PygAnimation([("Sprites/azukay_right/direita1.png",0.1),
                                        ("Sprites/azukay_right/direita2.png",0.1),
                                        ("Sprites/azukay_right/direita3.png",0.1)])        
        
    def movimentarPlayer(self):                
        for event in pygame.event.get():                
            if event.type == QUIT:
                sys.exit()
                
            if event.type == pygame.KEYDOWN:
                
                '''
                # mudar para colocar opcao no meio da fase
                if event.key== K_ESCAPE:
                    Menu().run_menu(Game().screen)'''
                
                if event.key== K_w:
                    if self.keys[1] == False and self.keys[2] == False and self.keys[3] == False: 
                        self.keys[0]=True
                        self.cima.play()
                
                elif event.key==K_a:
                    if self.keys[0] == False and self.keys[2] == False and self.keys[3] == False:
                        self.keys[1]=True
                        self.esquerda.play()
                
                elif event.key==K_s:
                    if self.keys[0] == False and self.keys[1] == False and self.keys[3] == False: 
                        self.keys[2]=True
                        self.baixo.play()
                
                elif event.key==K_d:
                    if self.keys[0] == False and self.keys[1] == False and self.keys[2] == False:
                        self.keys[3]=True
                        self.direita.play()
            if event.type == pygame.KEYUP:
                
                if event.key ==  K_w:
                    self.keys[0]=False
                    self.cima.stop()
                    self.player_imagem = self.player_subindo
                
                elif event.key==K_a:
                    self.esquerda.stop()
                    self.keys[1]=False
                    self.player_imagem = self.player_esquerda
                
                elif event.key==K_s:
                    self.baixo.stop()
                    self.keys[2]=False
                    self.player_imagem = self.player_descendo
                
                elif event.key==K_d:
                    self.direita.stop()
                    self.keys[3]=False
                    self.player_imagem = self.player_direita
                            
            if (self.keys[0] == True) and (self.playerpos[1] > 120):
                self.playerpos[1] -= self.speed
            elif (self.keys[2] == True) and (self.playerpos[1] < (Game().height - 47)):
                self.playerpos[1] += self.speed
            if (self.keys[1] == True) and (self.playerpos[0] > 30):
                self.playerpos[0] -= self.speed
            elif (self.keys[3] == True) and (self.playerpos[0] < (Game().width - 35)):
                self.playerpos[0] += self.speed
        Personagem().printaPersonagem()

    def atirar(self):
        
        playerrot = pygame.transform.rotate(self.player_imagem, 0)
        playerpos1 = (self.playerpos[0]-playerrot.get_rect().width/2, self.playerpos[1]-playerrot.get_rect().height/2)
        for event in pygame.event.get(): 
            if event.type == pygame.KEYDOWN:
                if event.key in (K_UP,K_DOWN,K_LEFT,K_RIGHT):
                
                    if event.key == K_UP:
                        position= [self.playerpos[0],self.playerpos[1]-50]
                    
                    elif event.key == K_DOWN:
                        position= [self.playerpos[0],self.playerpos[1]+50]
                    
                    elif event.key == K_LEFT:
                        position= [self.playerpos[0]-50,self.playerpos[1]]
                    
                    elif event.key == K_RIGHT:
                        position= [self.playerpos[0]+50,self.playerpos[1]]
                                                
                    self.shurikens.append([math.atan2(position[1]-(playerpos1[1]+50),position[0]-(playerpos1[0]+50)),playerpos1[0]+32,playerpos1[1]+32])  
        Personagem().printaShuriken()                          
                
    def printaPersonagem(self):        
        
        if self.keys[0] == False and self.keys[1] == False and self.keys[2] == False and self.keys[3] == False:
            Game().screen.blit(self.player_imagem,(self.playerpos[0]-50,self.playerpos[1]-50))
            
        self.baixo.blit(Game().screen, (self.playerpos[0]-50, self.playerpos[1]-50))
        self.cima.blit(Game().screen, (self.playerpos[0]-50, self.playerpos[1]-50))
        self.esquerda.blit(Game().screen, (self.playerpos[0]-50, self.playerpos[1]-50))
        self.direita.blit(Game().screen, (self.playerpos[0]-50, self.playerpos[1]-50))
        Personagem().atirar()
        
    def printaShuriken(self):
            for bullet in self.shurikens:
                index = 0
                velx = math.cos(bullet[0]) * 10
                vely = math.sin(bullet[0]) * 10
                bullet[1] += velx
                bullet[2] += vely
                if bullet[1] < -64 or bullet[1] > 800 or bullet[2] < -64 or bullet[2] > 600:
                    self.shurikens.pop(index)
                index += 1
                
            for projectile in self.shurikens:
                shuriken1 = pygame.transform.rotate(self.shuriken, 360 - projectile[0] * 57.29)
                Game().screen.blit(shuriken1, (projectile[1], projectile[2]))


class sprite():
    def __init__(self):
        self.sprite = '' 
        
class Fase(Personagem):
    def __init__(self):        
        self.chao = pygame.image.load("Sprites/bg/chao.png")        
                
    def jogar(self):
        pygame.init()
        pygame.display.set_caption('##############  AZUKAY ############### ')
                
        while True:
            Game().screen.blit(self.chao,(0,0)
            x = Personagem()
            x.movimentarPlayer()            
Fase().jogar()
            