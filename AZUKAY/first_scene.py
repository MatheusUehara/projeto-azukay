import pygame , sys ,math
from random import*
from pygame.locals import *
import pyganim

class Game():
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.size = self.width, self.height = 800 , 600
        self.bg_color = 255, 246, 213
        self.screen = pygame.display.set_mode(self.size)
        self.clock = pygame.time.Clock()
        pygame.display.set_caption('##############  AZUKAY ############### ')
    
    def run(self):
        FPS = 60
        fpsClock = pygame.time.Clock()
        width, height = 800, 600
        self.keys = [False, False, False, False]
        playerpos=[120,420]
        self.shurikens=[]
        self.speed = 3
        player_imagem = pygame.image.load("Sprites/azukay_front/frente.png")
        player_descendo = pygame.image.load("Sprites/azukay_front/frente.png")
        player_esquerda = pygame.image.load("Sprites/azukay_left/esquerda0.png")
        player_direita = pygame.image.load("Sprites/azukay_right/direita0.png")
        player_subindo = pygame.image.load("Sprites/azukay_back/costas_andando.png")
        chao = pygame.image.load("fases/fase1/fundo.png")
        status = pygame.image.load("fases/fase1/rock_statusbar.png")
        shuriken = pygame.image.load("Sprites/shuriken/shuriken.png")
        

        cima = pyganim.PygAnimation([("Sprites/azukay_back/costas_andando.png",0.1),
                                     ("Sprites/azukay_back/costas_andando1.png",0.1),
                                     ("Sprites/azukay_back/costas_andando2.png",0.1)])
        
        baixo = pyganim.PygAnimation([("Sprites/azukay_front/frente.png",0.1),
                                      ("Sprites/azukay_front/frente_andando1.png",0.1),
                                      ("Sprites/azukay_front/frente_andando2.png",0.1)])
        
        esquerda = pyganim.PygAnimation([("Sprites/azukay_left/esquerda1.png",0.1),
                                         ("Sprites/azukay_left/esquerda2.png",0.1),
                                         ("Sprites/azukay_left/esquerda3.png",0.1)])
        
        direita = pyganim.PygAnimation([("Sprites/azukay_right/direita1.png",0.1),
                                        ("Sprites/azukay_right/direita2.png",0.1),
                                        ("Sprites/azukay_right/direita3.png",0.1)])
        

        while True:

            self.screen.fill(0) 

            self.screen.blit(chao,(0,0))
            self.screen.blit(status,(0,0))

            # 6.1 - posicao do player usada pro tiro
            playerrot = pygame.transform.rotate(player_imagem, 0)
            playerpos1 = (playerpos[0]-playerrot.get_rect().width/2, playerpos[1]-playerrot.get_rect().height/2)
            
            # no caso de todas as chves falsas blitar a ultima imagem valida
            if self.keys[0] == False and self.keys[1] == False and self.keys[2] == False and self.keys[3] == False:
                self.screen.blit(player_imagem,(playerpos[0]-50,playerpos[1]-50))
            
            baixo.blit(self.screen, (playerpos[0]-50, playerpos[1]-50))
            cima.blit(self.screen, (playerpos[0]-50, playerpos[1]-50))
            esquerda.blit(self.screen, (playerpos[0]-50, playerpos[1]-50))
            direita.blit(self.screen, (playerpos[0]-50, playerpos[1]-50))

            self.printaShuriken(shuriken)


            pygame.display.flip()

    
            # 8 -Eventos de Movimentacao e tiro 
            for event in pygame.event.get():
                
                if event.type == QUIT:
                    sys.exit()
                    
                if event.type == pygame.KEYDOWN:
                    
                    if event.key== K_ESCAPE:
                        Game().menu()
                    
                    if event.key== K_w:
                        if self.keys[2]==False: 
                            self.keys[0]=True
                            player_imagem = player_subindo
                        if self.keys[1] == False and self.keys[2] == False and self.keys[3] == False: 
                            cima.play()
                    
                    elif event.key==K_a:
                        if self.keys[3]==False: 
                            self.keys[1]=True
                            player_imagem = player_esquerda
                        if self.keys[0] == False and self.keys[2] == False and self.keys[3] == False:
                            esquerda.play()
                    
                    elif event.key==K_s:
                        if self.keys[0]==False: 
                            self.keys[2]=True
                            player_imagem = player_descendo
                        if self.keys[0] == False and self.keys[1] == False and self.keys[3] == False: 
                            baixo.play()
                    
                    elif event.key==K_d:
                        if self.keys[1]==False: 
                            self.keys[3]=True
                            player_imagem = player_direita
                        if self.keys[0] == False and self.keys[1] == False and self.keys[2] == False:
                            direita.play()    
                              
                    # Eventos de Tiro                   
                    elif event.key in (K_UP,K_DOWN,K_LEFT,K_RIGHT):
                    
                        if event.key == K_UP:
                            position= [playerpos[0],playerpos[1]-50]
                        
                        elif event.key == K_DOWN:
                            position= [playerpos[0],playerpos[1]+50]
                        
                        elif event.key == K_LEFT:
                            position= [playerpos[0]-50,playerpos[1]]
                        
                        elif event.key == K_RIGHT:
                            position= [playerpos[0]+50,playerpos[1]]
                        
                        self.shurikens.append([math.atan2(position[1]-(playerpos1[1]+50),position[0]-(playerpos1[0]+50)),playerpos1[0]+32,playerpos1[1]+32])                            
                    
                if event.type == pygame.KEYUP:
                    
                    if event.key ==  K_w:
                        self.keys[0]=False
                        cima.stop()
                        player_imagem = player_subindo
                    
                    elif event.key==K_a:
                        esquerda.stop()
                        self.keys[1]=False
                        player_imagem = player_esquerda
                    
                    elif event.key==K_s:
                        baixo.stop()
                        self.keys[2]=False
                        player_imagem = player_descendo
                    
                    elif event.key==K_d:
                        direita.stop()
                        self.keys[3]=False
                        player_imagem = player_direita
            
            self.movimentarPlayer(width, height, playerpos)
            
            pygame.display.update()
            fpsClock.tick(FPS)

    def printaShuriken(self, shuriken):
    # 6.2 - Shurikens
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
            shuriken1 = pygame.transform.rotate(shuriken, 360 - projectile[0] * 57.29)
            self.screen.blit(shuriken1, (projectile[1], projectile[2]))

    def movimentarPlayer(self, width, height, playerpos):
    # 9 - Move player
        if (self.keys[0] == True) and (playerpos[1] > 120):
            
            playerpos[1] -= self.speed
        elif (self.keys[2] == True) and (playerpos[1] < (height - 47)):
            playerpos[1] += self.speed
        if (self.keys[1] == True) and (playerpos[0] > 30):
            playerpos[0] -= self.speed
        elif (self.keys[3] == True) and (playerpos[0] < (width - 35)):
            playerpos[0] += self.speed

Game().run()