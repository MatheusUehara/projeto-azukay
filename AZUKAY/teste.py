import pygame , sys ,math , random
from pygame.locals import *
import pyganim
pygame.init()

def Jogar():
    size = width,height = 800, 600
    screen=pygame.display.set_mode(size)
    pygame.display.set_caption('##############  AZUKAY ############### ')
    shurikens=[]
    speed = 4

    dir_direita = False
    dir_esquerda = False
    dir_cima = False
    dir_baixo = False       
    
    player_descendo = pygame.image.load("Sprites/azukay_front/frente.png")
    player_esquerda = pygame.image.load("Sprites/azukay_left/esquerda0.png")
    player_direita = pygame.image.load("Sprites/azukay_right/direita0.png")
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
    
    esquerda = pyganim.PygAnimation([("Sprites/azukay_left/esquerda0.png",0.1),
                                     ("Sprites/azukay_left/esquerda1.png",0.1),
                                     ("Sprites/azukay_left/esquerda2.png",0.1),
                                     ("Sprites/azukay_left/esquerda3.png",0.1)])
    
    direita = pyganim.PygAnimation([("Sprites/azukay_right/direita0.png",0.1),
                                    ("Sprites/azukay_right/direita1.png",0.1),
                                    ("Sprites/azukay_right/direita2.png",0.1),
                                    ("Sprites/azukay_right/direita3.png",0.1)])
   
   
    IDLE = pygame.image.load("Sprites/azukay_front/frente.png")
    IDLERect = IDLE.get_rect()
    IDLERect.x = 200
    IDLERect.y = 200
   
    javali = pygame.image.load("Sprites/enemy/javali/lado1.png")
    javaliRect = javali.get_rect()
    javaliRect.x = 700  
    javaliRect.y = 500
    


    
    while 1:
        
        screen.fill(0)
        screen.blit(grass,(0,0))
        screen.blit(statusbar,(0,0))        
        screen.blit(javali,(javaliRect.x,javaliRect.y))     
          


        ##################################################################################################
        #####     movimenta e blita shuriken 
        ##################################################################################################
        
        index=0
        for bullet in shurikens:
            
            velx=math.cos(bullet[0])*8
            vely=math.sin(bullet[0])*8
            bullet[1]+=velx
            bullet[2]+=vely
            if bullet[1]<-0 or bullet[1]>800 or bullet[2]<-0 or bullet[2]>600:
                shurikens.pop(index)
            else:
                index+=1
        for projectile in shurikens:
            shuriken1 = pygame.transform.rotate(shuriken, 360-projectile[0]*57.29)
            screen.blit(shuriken1, (projectile[1], projectile[2]))
            
        ##################################################################################################
        ############ blitando personagem        
        ##################################################################################################
        
        if dir_direita == False and dir_esquerda == False and dir_cima == False and dir_baixo == False:
                    screen.blit(IDLE,(IDLERect.x,IDLERect.y))

        else:
            esquerda.blit(screen, (IDLERect.x,IDLERect.y))   
            cima.blit(screen, (IDLERect.x,IDLERect.y))
            baixo.blit(screen, (IDLERect.x,IDLERect.y))
            direita.blit(screen, (IDLERect.x,IDLERect.y))

        ##################################################################################################
        ##### Captura de eventos      
        ##################################################################################################
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
                    
        ##################################################################################################            
        ########## shuriken
        ################################################################################################## 

                elif event.key == K_UP and (len(shurikens)< speed):
                    shurikens.append([-1.5707963267948966,IDLERect.centerx,IDLERect.centery])
    
                elif event.key == K_DOWN and (len(shurikens)< speed):
                    shurikens.append([1.5707963267948966,IDLERect.centerx,IDLERect.centery])
    
                elif event.key == K_LEFT and (len(shurikens)< speed):
                    shurikens.append([3.141592653589793,IDLERect.centerx,IDLERect.centery])
    
                elif event.key == K_RIGHT and (len(shurikens)< speed):
                    shurikens.append([0.0,IDLERect.centerx,IDLERect.centery])

        ##################################################################################################
        ############ desativando eventos 
        ##################################################################################################
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

        ##################################################################################################
        ###########    pra cima e pra baixo 
        ##################################################################################################
        
        if (dir_cima == True) and (IDLERect.y>70):
            IDLERect.y-= speed
            if dir_baixo==False and dir_esquerda == False and dir_direita == False:
                IDLE = player_subindo
                cima.play()                
            
        elif (dir_baixo == True) and (IDLERect.y<height-100):
            IDLERect.y+=speed
            if dir_cima==False and dir_esquerda == False and dir_direita == False:
                IDLE = player_descendo
                baixo.play()                
            
        ####################### esquerda e direita ####################################################

        if (dir_esquerda == True)  and (IDLERect.x>-20):
            IDLERect.x-=speed
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
                            
        elif (dir_direita == True) and (IDLERect.x<width-80):
            IDLERect.x+=speed
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
                
        if IDLERect.colliderect(javaliRect):
            x = random.randint(0,1)
            if x == 0:
                javaliRect.x -= 30
            else: 
                javaliRect.y -= 30           
        
        pygame.display.flip()


'''
############################ esboco da funcao que movimenta os inimigos
 
def movimenta_inimigo(inimigo,movimento,personagemRect):
    #global IDLERect
    #global x,y
    # passar paramentro ClassePersonagem.getMovimento para o parametro movimento
    # passar parametro RECT do inimigo para personagemRect
    
    if movimento == 1:  
        meta = 0
        print "movimento = 1"
            if inimigo.rect.left > meta and meta == 0 and inimigo.morreu()== 0:
                inimigo.setxy(-speed,0)
                if inimigo.rect.left <= meta:
                    meta = 800
                
            if inimigo.rect.right < meta and meta == 800 and inimigo.morreu()== 0:
                inimigo.setxy(speed,0) 
                if inimigo.rect.right >= meta:
                    meta = 0
                  
    elif movimento == 2:
        meta = 0
        print "movimento = 2"
            if inimigo.rect.left > meta and meta == 0 and inimigo.morreu()== 0:
                inimigo.setxy(-speed,0)
                if inimigo.rect.left <= meta:
                    meta = 800
                
            if inimigo.rect.right < meta and meta == 800 and inimigo.morreu()== 0:
                inimigo.setxy(speed,0) 
                if inimigo.rect.right >= meta:
                    meta = 0
    
    elif movimento == 3:
        meta = 0
        print "movimento = 3"
            if inimigo.rect.left > meta and meta == 0 and inimigo.morreu()== 0:
                inimigo.setxy(-speed,0)
                if inimigo.rect.left <= meta:
                    meta = 800
                
            if inimigo.rect.right < meta and meta == 800 and inimigo.morreu()== 0:
                inimigo.setxy(speed,0) 
                if inimigo.rect.right >= meta:
                    meta = 0
        '''

            
            
        