import sys, random, pygame , math, pyganim
import ClassePersonagem


from ClassePersonagem import Personagem

azukay = ClassePersonagem.Personagem("azukay",20,5,100,100,0,"Sprites/azukay_front/frente.png")
azukay.do_Rect()

inimigo1 = ClassePersonagem.Personagem("javali",20,100,400,190,random.randint(1,3),"Sprites/enemy/javali/lado1.png")
inimigo1.do_Rect()


    
'''
    
    if nivel == 1:
        background = level_1
        inimigo1 = ClassePersonagem.Personagem("escorpiao",20,100,400,190,random.randint(1,3),"Sprites/enemy/escorpiao/desce1.png")
        inimigo2 = ClassePersonagem.Personagem("cobra",20,100,40,490,random.randint(1,3),"Sprites/enemy/cobra/lado3.png")
        inimigo3 = ClassePersonagem.Personagem("escorpiao",20,100,90,100,random.randint(1,3),"Sprites/enemy/escorpiao/desce1.png")
        inimigo4 = ClassePersonagem.Personagem("cobra",20,100,700,190,random.randint(1,3),"Sprites/enemy/cobra/lado3.png")
        inimigo5 = ClassePersonagem.Personagem("escorpiao",20,100,190,700,random.randint(1,3),"Sprites/enemy/escorpiao/desce1.png")
        
    elif nivel == 2:
               
''' 

##################################################################################################
#    carregando imagens dos inimigos
################################################################################################## 


javali_esquerda = pyganim.PygAnimation([("Sprites/enemy/javali/lado1.png",0.1),("Sprites/enemy/javali/lado2.png",0.1)])
javali_direita = pyganim.PygAnimation([("Sprites/enemy/javali/lado3.png",0.1),("Sprites/enemy/javali/lado4.png",0.1)])

'''
javali_sobe = pyganim.PygAnimation([("Sprites/enemy/javali/sobe1.png",0.1),
                             ("Sprites/enemy/javali/sobe2.png",0.1)])
javali_desce = pyganim.PygAnimation([("Sprites/enemy/javali/desce1.png",0.1),
                             ("Sprites/enemy/javali/desce2.png",0.1)])
'''

##################################################################################################
#    carregando imagens e boolean dos lados e animacao
################################################################################################## 

dir_cima = False
dir_baixo = False
dir_esquerda = False
dir_direita = False


player_descendo = pygame.image.load("Sprites/azukay_front/frente.png")
player_esquerda = pygame.image.load("Sprites/azukay_left/esquerda0.png")
player_direita = pygame.image.load("Sprites/azukay_right/direita0.png")
player_subindo = pygame.image.load("Sprites/azukay_back/costas_andando.png")


cima = pyganim.PygAnimation([("Sprites/azukay_back/costas_andando.png",0.1),("Sprites/azukay_back/costas_andando1.png",0.1),("Sprites/azukay_back/costas_andando2.png",0.1)])

baixo = pyganim.PygAnimation([("Sprites/azukay_front/frente.png",0.1),("Sprites/azukay_front/frente_andando1.png",0.1),("Sprites/azukay_front/frente_andando2.png",0.1)])

esquerda = pyganim.PygAnimation([("Sprites/azukay_left/esquerda0.png",0.1),("Sprites/azukay_left/esquerda1.png",0.1),("Sprites/azukay_left/esquerda2.png",0.1),("Sprites/azukay_left/esquerda3.png",0.1)])

direita = pyganim.PygAnimation([("Sprites/azukay_right/direita0.png",0.1),("Sprites/azukay_right/direita1.png",0.1),("Sprites/azukay_right/direita2.png",0.1),("Sprites/azukay_right/direita3.png",0.1)])


##definindo o blit dos inimigos


def inimigo_esquerda(inimigo):
    if inimigo.nome == "javali":
        javali_direita.stop()
        javali_esquerda.play()
    '''elif inimigo.nome == "cobra":
        cobra_esquerda.play()
    elif inimigo.nome == "escorpiao":
        escorpiao_esquerda.play()'''
                    
def inimigo_direita(inimigo):
    if inimigo.nome == "javali":
        javali_esquerda.stop()
        javali_direita.play()
    '''elif inimigo.nome == "cobra":
        cobra_direita.play()
    elif inimigo.nome == "escorpiao":
        escorpiao_direita.play()'''
        
'''        
def sobe(inimigo):
    if inimigo.nome == "javali":
        javali_sobe.play()
    elif inimigo.nome == "cobra":
        cobra_sobe.play()
    elif inimigo.nome == "escorpiao":
        escorpiao_sobe.play()
        
def desce(inimigo):
    if inimigo.nome == "javali":
        javali_desce.play()
    elif inimigo.nome == "cobra":
        cobra_desce.play()
    elif inimigo.nome == "escorpiao":
        escorpiao_desce.play()
        
'''
##################################################################################################
#    Movimentando todos os inimigos de acordo com o tipo de movimento
##################################################################################################

def movimenta_inimigo(inimigo,movimento,personagemRect):
    global meta
    # passar paramentro ClassePersonagem.getMovimento para o parametro movimento
    # passar parametro RECT do inimigo para personagemRect
    if inimigo.morreu() == 0:
        if movimento == 1:              
            if inimigo.rect.left > meta and meta == 0 and inimigo.morreu()== 0:
                inimigo.setxy(-speed,0)
                inimigo_esquerda(inimigo)
                if inimigo.rect.left <= meta:
                    meta = 800
                
            if inimigo.rect.right < meta and meta == 800 and inimigo.morreu()== 0:
                inimigo.setxy(speed,0) 
                inimigo_direita(inimigo)
                if inimigo.rect.right >= meta:
                    meta = 0
                      
        elif movimento == 2:
            if inimigo.rect.left > meta and meta == 0 and inimigo.morreu()== 0:
                inimigo.setxy(-speed,0)
                inimigo_esquerda(inimigo)
                if inimigo.rect.left <= meta:
                    meta = 800
                
            if inimigo.rect.right < meta and meta == 800 and inimigo.morreu()== 0:
                inimigo.setxy(speed,0) 
                inimigo_direita(inimigo)
                if inimigo.rect.right >= meta:
                    meta = 0
        
        elif movimento == 3:
            if inimigo.rect.left > meta and meta == 0 and inimigo.morreu()== 0:
                inimigo.setxy(-speed,0)
                inimigo_esquerda(inimigo)
                if inimigo.rect.left <= meta:
                    meta = 800
                
            if inimigo.rect.right < meta and meta == 800 and inimigo.morreu()== 0:
                inimigo.setxy(speed,0) 
                inimigo_direita(inimigo)
                if inimigo.rect.right >= meta:
                    meta = 0
    else: 
        pass

##################################################################################################
#    colisao de azukay com os inimigos
##################################################################################################

def colisao_azukay(inimigo):
    if azukay.rect.colliderect(inimigo1):
        azukay.perdeVida(azukay.getHit)
        azukay.setxy(random.randint(10,100),random.randint(10,100))
        

javali = pygame.image.load("Sprites/enemy/javali/lado1.png")

meta = 0


pygame.init()

size = width,height = 800, 600
screen=pygame.display.set_mode(size)
pygame.display.set_caption('##############  AZUKAY ############### ')

background = pygame.image.load("Sprites/bg/fundo.png")
background1 = pygame.image.load("Sprites/bg/fundo.png")
background2 = pygame.image.load("Sprites/bg/beta.png")
background3 = pygame.image.load("Sprites/bg/beta.png")

statusbar = pygame.image.load("Sprites/bg/statusbar.png")
vida = pygame.image.load("Sprites/bg/vida.png")

shuriken = pygame.image.load("Sprites/shuriken/shuriken.png")

speed = 4

score = 0

shurikens=[]


while 1 :
    screen.blit(background,(0,0))
    
    screen.blit(statusbar,(0,0))
    
    movimenta_inimigo(inimigo1,inimigo1.getMovimento(),azukay.rect)
    
    #inimigo1.blita(screen)
    
    colisao_azukay(inimigo1)
    
    ##################################################################################################
    #    Blitando Score
    ##################################################################################################
    
    font = pygame.font.Font(None, 40)
    font_score = font.render("Score = " + str(score), True, (0,0,0))
    screen.blit(font_score, (600,10))
    
    ##################################################################################################
    #    Blitando Vidas
    ##################################################################################################
    
    for i in range(azukay.vida):
        screen.blit(vida,((20+i*48),10)) 

    ##################################################################################################
    #    blitando inimigos
    ##################################################################################################
        
    javali_esquerda.blit(screen,(inimigo1.pos_x,inimigo1.pos_y))
    javali_direita.blit(screen,(inimigo1.pos_x,inimigo1.pos_y))
    
    
    ##################################################################################################
    #    blitando personagem        
    ##################################################################################################
    
    if dir_direita == False and dir_esquerda == False and dir_cima == False and dir_baixo == False:
                azukay.blita(screen)
                

    elif azukay.morreu() == 0:
        esquerda.blit(screen,(azukay.getx(),azukay.gety()))   
        cima.blit(screen,(azukay.getx(),azukay.gety()))
        baixo.blit(screen,(azukay.getx(),azukay.gety()))
        direita.blit(screen,(azukay.getx(),azukay.gety()))

    ##################################################################################################
    #    movimenta e blita shuriken 
    ##################################################################################################  
    index=0
    for bullet in shurikens:
        
        velx=math.cos(bullet[0])*8
        vely=math.sin(bullet[0])*8
        bullet[1]+=velx
        bullet[2]+=vely       
        
        ##################################################################################################
        #    colisao da shuriken
        ##################################################################################################
        def colisao(inimigo1,azukay,shurikens):
            global index
            global score
            if inimigo1.rect.collidepoint(bullet[1],bullet[2]):
                    inimigo1.perdeVida(azukay.getHit())
                    shurikens.pop(index)
                    score += 256
                    
        colisao(inimigo1,azukay,shurikens)
                            
        if bullet[1]<-0 or bullet[1]>800 or bullet[2]<-0 or bullet[2]>600:
            shurikens.pop(index)
        else:
            index+=1
    for projectile in shurikens:
        shuriken1 = pygame.transform.rotate(shuriken, 360-projectile[0]*57.29)
        screen.blit(shuriken1, (projectile[1], projectile[2]))
                        
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        
        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_w:
                dir_cima = True  
                cima.play()              
                
            elif event.key == pygame.K_s:
                dir_baixo = True
                baixo.play()

            elif event.key == pygame.K_a:
                    dir_esquerda = True
                    direita.stop()
                    esquerda.play()
                
            elif event.key == pygame.K_d:
                    dir_direita = True
                    esquerda.stop()
                    direita.play()
                
            ##################################################################################################            
            #    shuriken
            ################################################################################################## 

            elif event.key == pygame.K_UP and (len(shurikens)< speed):
                shurikens.append([-1.5707963267948966,azukay.rect.centerx,azukay.rect.centery])

            elif event.key == pygame.K_DOWN and (len(shurikens)< speed):
                shurikens.append([1.5707963267948966,azukay.rect.centerx,azukay.rect.centery])

            elif event.key == pygame.K_LEFT and (len(shurikens)< speed):
                shurikens.append([3.141592653589793,azukay.rect.centerx,azukay.rect.centery])

            elif event.key == pygame.K_RIGHT and (len(shurikens)< speed):
                shurikens.append([0.0,azukay.rect.centerx,azukay.rect.centery])
                
                
        if event.type == pygame.KEYUP:
            
                if event.key ==  pygame.K_w:
                    dir_cima =False
                    cima.stop()
        
                elif event.key == pygame.K_s:
                    dir_baixo=False
                    baixo.stop()
                    
                elif event.key == pygame.K_a:
                    dir_esquerda=False
                    esquerda.stop()
                    
                elif event.key == pygame.K_d:
                    dir_direita=False
                    direita.stop()
    ##################################################################################################
    #    movimentacao
    ################################################################################################## 
                    
    if (dir_cima == True) and (azukay.rect.top > 70):
        azukay.setxy(0,-speed)
        dir_baixo = False     
        if dir_baixo==False and dir_esquerda == False and dir_direita == False:
            azukay.setCaminho(player_subindo)
            cima.play()       
        
    elif (dir_baixo == True) and (azukay.rect.bottom < height):
        azukay.setxy(0,speed)   
        dir_cima = False
        if dir_cima==False and dir_esquerda == False and dir_direita == False:
                azukay.setCaminho(player_descendo)
                baixo.play()          

    if (dir_esquerda == True) and (azukay.rect.left > speed):
        azukay.setxy(-speed,0)
        if dir_cima == False and dir_baixo == False and dir_direita == False:
                azukay.setCaminho(player_esquerda)
                esquerda.play()
                baixo.stop()
        elif dir_direita == False and dir_cima == True:
                azukay.setCaminho(player_subindo)
                esquerda.stop()
                cima.play()
        elif dir_direita == False and dir_baixo == True:
                azukay.setCaminho(player_descendo)
                esquerda.stop()
                baixo.play()
        
                        
    elif (dir_direita == True) and (azukay.rect.right < width) and (dir_esquerda == False):
        azukay.setxy(speed,0) 
        if dir_cima == False and dir_baixo == False and dir_esquerda == False:
                azukay.setCaminho(player_direita)
                direita.play()
                baixo.stop()
        elif dir_esquerda == False and dir_cima == True:
                azukay.setCaminho(player_subindo)
                direita.stop()
                cima.play()
        elif dir_esquerda == False and dir_baixo == True:
                azukay.setCaminho(player_descendo)
                direita.stop()
                baixo.play()
                
                
    pygame.display.flip()
               
            
             
        