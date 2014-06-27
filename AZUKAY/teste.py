import pygame , sys ,math
from pygame.locals import *
import pyganim


pygame.init()


def run():
    size = width,height = 800, 600
    screen=pygame.display.set_mode(size)
    pygame.display.set_caption('##############  AZUKAY ############### ')
    playerpos=[200,200]
    shurikens=[]
    speed = 4

    dir_direita = False
    dir_esquerda = False
    dir_cima = False
    dir_baixo = False   
    
    
    IDLE = pygame.image.load("Sprites/azukay_front/frente.png")
    player_descendo = pygame.image.load("Sprites/azukay_front/frente.png")
    player_esquerda = pygame.image.load("Sprites/azukay_left/esquerda1.png")
    player_direita = pygame.image.load("Sprites/azukay_right/direita1.png")
    player_subindo = pygame.image.load("Sprites/azukay_back/costas_andando.png")
    statusbar = pygame.image.load("Sprites/bg/statusbar.png")
    shuriken = pygame.image.load("Sprites/shuriken/shuriken.png")
    
    grass = pygame.image.load("Sprites/bg/fundo.png")
    
    
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
    
    jav_esquerda = pyganim.PygAnimation([("Sprites/enemy/javali/lado1.png",0.1),
                                 ("Sprites/enemy/javali/lado2.png",0.1)])
    
    x = 700
    y = 500

    
    while 1:
        
        screen.fill(0)
        screen.blit(grass,(0,0))
        screen.blit(statusbar,(0,0))
        
        jav_esquerda.blit(screen,(x,y))        


        
######################## movimenta e blita shuriken ########################
        index=0
        for bullet in shurikens:
            
            velx=math.cos(bullet[0])*5
            vely=math.sin(bullet[0])*5
            bullet[1]+=velx
            bullet[2]+=vely
            if bullet[1]<-0 or bullet[1]>800 or bullet[2]<-0 or bullet[2]>600:
                shurikens.pop(index)
            else:
                index+=1
        for projectile in shurikens:
            shuriken1 = pygame.transform.rotate(shuriken, 360-projectile[0]*57.29)
            screen.blit(shuriken1, (projectile[1], projectile[2]))
        
#################### blitando personagem ############################
     
        if dir_direita == False and dir_esquerda == False and dir_cima == False and dir_baixo == False:
                    screen.blit(IDLE,(playerpos[0],playerpos[1]))

        else:
            esquerda.blit(screen, (playerpos[0], playerpos[1]))   
            cima.blit(screen, (playerpos[0], playerpos[1]))
            baixo.blit(screen, (playerpos[0], playerpos[1]))
            direita.blit(screen, (playerpos[0], playerpos[1]))

############# Captura de eventos ################     
        for event in pygame.event.get(): 
                       
            if event.type == QUIT:
                exit()
                
            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    import menu
                    menu.menu_principal()
                elif event.key== K_w:
                    dir_cima=True                    
                                        
                elif event.key==K_a:
                    dir_esquerda=True                    
                    
                elif event.key==K_s:
                    dir_baixo=True
                    
                elif event.key==K_d:
                    dir_direita=True
                    
##################### shuriken ###############################

                elif event.key == K_UP:
                    shurikens.append([-1.5707963267948966,playerpos[0]+50,playerpos[1]+50])
    
                elif event.key == K_DOWN:
                    shurikens.append([1.5707963267948966,playerpos[0]+50,playerpos[1]+50])
    
                elif event.key == K_LEFT:
                    shurikens.append([3.141592653589793,playerpos[0]+50,playerpos[1]+50])
    
                elif event.key == K_RIGHT:
                    shurikens.append([0.0,playerpos[0]+50,playerpos[1]+50])

######################## desativando eventos ########################

            if event.type == pygame.KEYUP:
                if event.key ==  K_w:
                    dir_cima =False
                    cima.stop()
                    
                elif event.key==K_a:
                    esquerda.stop()
                    dir_esquerda=False
                    
                elif event.key==K_s:
                    baixo.stop()
                    dir_baixo=False
                    
                elif event.key==K_d:
                    direita.stop()
                    dir_direita=False

########################## pra cima e pra baixo #######################################################

        if (dir_cima == True) and (playerpos[1]>70):
            playerpos[1]-= speed
            if dir_baixo==False and dir_esquerda == False and dir_direita == False:
                IDLE = player_subindo
                cima.play()                
            
        elif (dir_baixo == True) and (playerpos[1]<height-100):
            playerpos[1]+=speed
            if dir_cima==False and dir_esquerda == False and dir_direita == False:
                IDLE = player_descendo
                baixo.play()                
            
############################### esquerda e direita ####################################################

        if (dir_esquerda == True)  and (playerpos[0]>-20):
            playerpos[0]-=speed
            if dir_cima==False and dir_baixo == False and dir_direita == False:
                IDLE = player_esquerda
                esquerda.play()
            elif dir_direita==False and dir_cima==True:
                IDLE = player_subindo
                esquerda.stop()
                cima.play()
            elif dir_direita==False and dir_baixo==True:
                IDLE = player_descendo
                esquerda.stop()
                baixo.play()
                            
        elif (dir_direita == True) and (playerpos[0]<width-80):
            playerpos[0]+=speed
            if dir_cima==False and dir_baixo == False and dir_esquerda == False:
                IDLE = player_direita
                direita.play()
            elif dir_esquerda==False and dir_cima==True:
                IDLE = player_subindo
                direita.stop()
                cima.play()
            elif dir_esquerda==False and dir_baixo==True:
                IDLE = player_descendo
                direita.stop()
                baixo.play()   
                

                 
            
        if x < playerpos[0]:
            jav_esquerda.play()
            x+=3
                        
        elif x > playerpos[0]:
            jav_esquerda.play()
            x-=3
            
        if y < playerpos[1]:
            jav_esquerda.play()
            y+=3
                      
        elif y > playerpos[1]:
            jav_esquerda.play()
            y-=3
            
        pygame.display.flip()
        
run()