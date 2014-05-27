import pygame , sys ,math
from random import*
from pygame.locals import *

class Game():
    def __init__(self):
        pygame.init()
        pygame.mixer.init()

        self.size = self.width, self.height = 800, 600
        self.bg_color = 255, 246, 213
        self.screen = pygame.display.set_mode(self.size)
        self.clock = pygame.time.Clock()
        self.pressed_keys = pygame.key.get_pressed()
        pygame.display.set_caption('##############  AZUKAY ############### ')
    
    def menu(self): 
        p1 = pygame.image.load("1p.png")
        p2 = pygame.image.load("2p.png")
        ex = pygame.image.load("sair.png")

        while 1:
            self.clock.tick(600)

            pos = pygame.mouse.get_pos()

            for event in pygame.event.get():                     # Verifica eventos do teclado, mouse etc 
                if event.type == pygame.QUIT: 
                    sys.exit()
                if event.type==pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if (pos[1] > 300) and (pos[1]< 399) and ((pos[0]>449) and (pos[0]<551)):
                        Game().run()
                    elif (pos[1] >400) and (pos[1]<499) and ((pos[0]>449) and (pos[0]<551)):
                        Game().menu()
                    elif (pos[1] >500) and (pos[1]<600) and ((pos[0]>449) and (pos[0]<551)):
                        sys.exit()
            
            bg = pygame.image.load("azuka.png")
            self.screen.blit(bg,[0,0])

            self.screen.blit(p1,(450,300))
            self.screen.blit(p2,(450,400))
            self.screen.blit(ex,(450,500))

            logo = pygame.image.load("logo.png")
            self.screen.blit(logo,[280,70])
            pygame.display.flip()
    def run(self):
        FPS = 60
        fpsClock = pygame.time.Clock()
        width, height = 800, 600
        self.keys = [False, False, False, False]
        playerpos=[120,420]
        self.churikens=[]
        self.healthvalue=194
        self.speed = 4
        player_imagem = pygame.image.load("frente.png")
        player_descendo = pygame.image.load("frente.png")
        player_esquerda = pygame.image.load("esquerda.png")
        player_direita = pygame.image.load("direita.png")
        player_subindo = pygame.image.load("costas_andando.png")
        churiken = pygame.image.load("churiken.png")
        healthbar = pygame.image.load("healthbar.png")
        healthbar_vidas = pygame.image.load("healthbar_vidas.png")
        chao = pygame.image.load("chao.png")
        health = pygame.image.load("health.png")

        while 1:
            # 5 - clear the screen before drawing it again
            self.screen.fill(0) 

            self.screen.blit(chao,(1,1))

            # 6.1 - Player Position and blit
            playerrot = pygame.transform.rotate(player_imagem, 0)
            playerpos1 = (playerpos[0]-playerrot.get_rect().width/2, playerpos[1]-playerrot.get_rect().height/2)
            self.screen.blit(playerrot, playerpos1) 

            # 6.2 - Draw churikens
            for bullet in self.churikens:
                index=0
                velx=math.cos(bullet[0])*10
                vely=math.sin(bullet[0])*10
                bullet[1]+=velx
                bullet[2]+=vely
                if bullet[1]<-64 or bullet[1]>640 or bullet[2]<-64 or bullet[2]>480:
                    self.churikens.pop(index)
                index+=1
            for projectile in self.churikens:
                churiken1 = pygame.transform.rotate(churiken, 360-projectile[0]*57.29)
                self.screen.blit(churiken1, (projectile[1], projectile[2]))


            # 6.5 - Draw health bar
            self.screen.blit(healthbar, (125,18))    
            for health1 in range(self.healthvalue):
                self.screen.blit(health, (health1+128,21))

            self.screen.blit(healthbar_vidas,(125,18))

            # 7 - update the screen
            pygame.display.flip()

    
            # 8 - loop through the events
            for event in pygame.event.get():            
                if event.type == pygame.KEYDOWN:
                    if event.key== K_ESCAPE:
                        Game().menu()
                    if event.key== K_w:
                        self.keys[0]=True
                        player_imagem = player_subindo
                    elif event.key==K_a:
                        self.keys[1]=True
                        player_imagem = player_esquerda
                    elif event.key==K_s:
                        self.keys[2]=True
                        player_imagem = player_descendo
                    elif event.key==K_d:
                        self.keys[3]=True
                        player_imagem = player_direita
                    elif event.key in (K_UP,K_DOWN,K_LEFT,K_RIGHT):
                        if event.key == K_UP:
                            position= [playerpos[0],playerpos[1]-50]
                        elif event.key == K_DOWN:
                            position= [playerpos[0],playerpos[1]+50]
                        elif event.key == K_LEFT:
                            position= [playerpos[0]-50,playerpos[1]]
                        elif event.key == K_RIGHT:
                            position= [playerpos[0]+50,playerpos[1]]
                        self.churikens.append([math.atan2(position[1]-(playerpos1[1]+50),position[0]-(playerpos1[0]+50)),playerpos1[0]+32,playerpos1[1]+32])

                if event.type == pygame.KEYUP:
                    if event.key ==  K_w:
                        self.keys[0]=False
                        player_imagem = player_subindo
                    elif event.key==K_a:
                        self.keys[1]=False
                        player_imagem = player_esquerda
                    elif event.key==K_s:
                        self.keys[2]=False
                        player_imagem = player_descendo
                    elif event.key==K_d:
                        self.keys[3]=False
                        player_imagem = player_direita
            
            # 9 - Move player
            if (self.keys[0] == True) and (playerpos[1]>120):
                playerpos[1]-= self.speed
            elif (self.keys[2] == True) and (playerpos[1]<(height-47)):
                playerpos[1]+=self.speed
            if (self.keys[1] == True)  and (playerpos[0]> 30):
                playerpos[0]-=self.speed
            elif (self.keys[3] == True) and (playerpos[0]<(width-35)):
                playerpos[0]+=self.speed
            fpsClock.tick(FPS)

Game().menu()