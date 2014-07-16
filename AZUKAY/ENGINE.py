import sys, random, pygame , math, pyganim
import ClassePersonagem

score = 0

def Jogar(nivel):
    from ClassePersonagem import Personagem
    
    azukay = ClassePersonagem.Personagem("azukay",20,5,100,100,0,"Sprites/azukay_front/frente.png",0)
    azukay.do_Rect()
    
    if nivel == "1":
            
        inimigo1 = ClassePersonagem.Personagem("javali",20,100,random.randint(70,600),random.randint(0,600),random.randint(1,2),"Sprites/enemy/javali/lado1.png",0)
        inimigo1.do_Rect()
        inimigo1.getMeta()
        
        inimigo2 = ClassePersonagem.Personagem("cobra",20,100,random.randint(70,600),random.randint(0,600),random.randint(1,2),"Sprites/enemy/cobra/lado1.png",0)
        inimigo2.do_Rect()
        inimigo2.getMeta()
        
        inimigo3 = ClassePersonagem.Personagem("javali",20,100,random.randint(70,600),random.randint(0,600),random.randint(1,2),"Sprites/enemy/javali/lado1.png",0)
        inimigo3.do_Rect()
        inimigo3.getMeta()
        
        inimigo4 = ClassePersonagem.Personagem("cobra",20,100,random.randint(70,600),random.randint(0,600),random.randint(1,3),"Sprites/enemy/cobra/lado1.png",0)
        inimigo4.do_Rect()
        inimigo4.getMeta()
        
        #inimigo5 = ClassePersonagem.Personagem("javali",20,100,random.randint(70,800),random.randint(0,600),random.randint(1,2),"Sprites/enemy/javali/lado1.png",0)
        #inimigo5.do_Rect()
        #inimigo5.getMeta()
    
    ##################################################################################################
    #    carregando animacao dos inimigos
    ################################################################################################## 
    
    javali_esquerda = pyganim.PygAnimation([("Sprites/enemy/javali/lado1.png",0.1),("Sprites/enemy/javali/lado2.png",0.1)])
    javali_direita = pyganim.PygAnimation([("Sprites/enemy/javali/lado3.png",0.1),("Sprites/enemy/javali/lado4.png",0.1)])
    javali_desce = pyganim.PygAnimation([("Sprites/enemy/javali/desce1.png",0.1),("Sprites/enemy/javali/desce2.png",0.1)])
    javali_sobe = pyganim.PygAnimation([("Sprites/enemy/javali/sobe1.png",0.1),("Sprites/enemy/javali/sobe2.png",0.1)])
    
    
    escorpiao_esquerda = pyganim.PygAnimation([("Sprites/enemy/escorpiao/lado1.png",0.1),("Sprites/enemy/escorpiao/lado2.png",0.1)])
    escorpiao_direita = pyganim.PygAnimation([("Sprites/enemy/escorpiao/lado3.png",0.1),("Sprites/enemy/escorpiao/lado4.png",0.1)])
    escorpiao_desce = pyganim.PygAnimation([("Sprites/enemy/escorpiao/desce1.png",0.1),("Sprites/enemy/escorpiao/desce2.png",0.1)])
    escorpiao_sobe =  pyganim.PygAnimation([("Sprites/enemy/escorpiao/sobe1.png",0.1),("Sprites/enemy/escorpiao/sobe2.png",0.1)])
    
    cobra_esquerda = pyganim.PygAnimation([("Sprites/enemy/cobra/lado1.png",0.1),("Sprites/enemy/cobra/lado2.png",0.1)])
    cobra_direita = pyganim.PygAnimation([("Sprites/enemy/cobra/lado4.png",0.1),("Sprites/enemy/cobra/lado5.png",0.1)])
    cobra_desce = pyganim.PygAnimation([("Sprites/enemy/cobra/desce1.png",0.1),("Sprites/enemy/cobra/desce2.png",0.1)])
    cobra_sobe =  pyganim.PygAnimation([("Sprites/enemy/cobra/sobe1.png",0.1),("Sprites/enemy/cobra/sobe2.png",0.1)])
    
    
    ##################################################################################################
    #    carregando imagens e boolean dos lados e animacao do personagem
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
    
    
    
    ################################################################################################## 
    #definindo o blit dos inimigos
    ################################################################################################## 
    
    def inimigo_esquerda(inimigo):
        if inimigo.nome == "javali":
            blitar(inimigo)
            #blitar(javali_esquerda,inimigo)
            #javali_direita.stop()
            javali_desce.stop()
            javali_direita.stop()
            javali_sobe.stop()
            javali_esquerda.play()
        elif inimigo.nome == "cobra":
            blitar(inimigo)
            #blitar(cobra_esquerda,inimigo)
            #cobra_direita.stop()
            cobra_esquerda.play()
        elif inimigo.nome == "escorpiao":
            escorpiao_direita.stop()
            escorpiao_esquerda.play()
                        
    def inimigo_direita(inimigo):
        if inimigo.nome == "javali":
            blitar(inimigo)
            #blitar(javali_direita,inimigo)
            #javali_esquerda.stop()
            javali_esquerda.stop()
            javali_desce.stop()
            javali_sobe.stop()
            javali_direita.play()
        elif inimigo.nome == "cobra":
            blitar(inimigo)
            #blitar(cobra_direita,inimigo)
            #cobra_esquerda.stop()
            cobra_direita.play()
        elif inimigo.nome == "escorpiao":
            escorpiao_esquerda.stop()
            escorpiao_direita.play()
            
         
    def inimigo_sobe(inimigo):
        if inimigo.nome == "javali":
            blitar(inimigo)
            javali_esquerda.stop()
            javali_direita.stop()
            javali_desce.stop()
            #blitar(javali_sobe,inimigo)
            #javali_desce.stop()
            javali_sobe.play()
            
        elif inimigo.nome == "cobra":
            blitar(inimigo)
            #blitar(cobra_sobe,inimigo)
            #cobra_desce.stop()
            cobra_sobe.play()
        elif inimigo.nome == "escorpiao":
            escorpiao_desce.stop()
            escorpiao_sobe.play()
            
    def inimigo_desce(inimigo):
        blitar(inimigo)
        javali_desce.play()
        cobra_desce.play()
        '''
        if inimigo.nome == "javali":
            blitar(inimigo)
            #blitar(javali_desce,inimigo)
            javali_esquerda.stop()
            javali_direita.stop()
            javali_sobe.stop()
            javali_desce.play()
        elif inimigo.nome == "cobra":
            blitar(inimigo)
            #blitar(cobra_desce,inimigo)
            #cobra_sobe.stop()
            cobra_desce.play()
        elif inimigo.nome == "escorpiao":
            escorpiao_sobe.stop()
            escorpiao_desce.play()
        '''
        
    ##################################################################################################
    #    Verifica falha ou sucesso
    ##################################################################################################        
        
    def perdeu_ganhou():
        if azukay.morreu() == 1:
            import menu
            menu.tela_perdeu()
        '''
        parametro = arq.read()
        elif score == 6400:
            import menu
            menu.tela_proxima_fase(parametro+1) 
        '''
    ##################################################################################################
    #    Movimentando todos os inimigos de acordo com o tipo de movimento
    ##################################################################################################
    
    def movimenta_inimigo(inimigo,movimento,personagemRect):
        # passar paramentro ClassePersonagem.getMovimento para o parametro movimento
        # passar parametro RECT do inimigo para personagemRect
        if inimigo.morreu() == 0:
            if movimento == 1:              
                if inimigo.rect.left > inimigo.meta and inimigo.meta == 0 and inimigo.morreu()== 0:
                    inimigo.setxy(-speed,0)
                    inimigo_esquerda(inimigo)
                    if inimigo.rect.left <= inimigo.meta:
                        inimigo.meta = 800
                    
                if inimigo.rect.right < inimigo.meta and inimigo.meta == 800 and inimigo.morreu()== 0:
                    inimigo.setxy(speed,0) 
                    inimigo_direita(inimigo)
                    if inimigo.rect.right >= inimigo.meta:
                        inimigo.meta = 0
            elif movimento == 2:
                if inimigo.rect.top > inimigo.meta and inimigo.meta == 90 and inimigo.morreu()== 0:
                    inimigo.setxy(0,-speed)
                    inimigo_sobe(inimigo)
                    if inimigo.rect.top <= inimigo.meta:
                        inimigo.meta = 600
                    
                if inimigo.rect.bottom < inimigo.meta and inimigo.meta == 600 and inimigo.morreu()== 0:
                    inimigo.setxy(0,speed) 
                    inimigo_desce(inimigo)
                    if inimigo.rect.bottom >= inimigo.meta:
                        inimigo.meta = 90
            '''
            elif movimento == 3:
                if inimigo.pos_x != inimigo.meta[0] or inimigo.pos_y != inimigo.meta[1]: # and (not(inimigo.collidepoint(inimigo.meta[0],inimigo.meta[1])))
                    if inimigo.pos_x > inimigo.meta[0]:
                        inimigo.setxy(-speed,0)
                    elif inimigo.pos_x < inimigo.meta[0]:
                        inimigo.setxy(speed,0)
                    elif inimigo.pos_y > inimigo.meta[1]: 
                        inimigo.setxy(0,-speed)
                    elif inimigo.pos_y < inimigo.meta[1]:
                        inimigo.setxy(0,speed) 
                    elif inimigo.pos_x == inimigo.meta[0] and inimigo.pos_y > inimigo.meta[1]:
                        inimigo.setxy(0,-speed)
                    elif inimigo.pos_x == inimigo.meta[0] and inimigo.pos_y < inimigo.meta[1]: 
                        inimigo.setxy(0,speed)
                    elif inimigo.pos_y == inimigo.meta[1] and inimigo.pos_x > inimigo.meta[0]:#CASO O Y DO PACMAN SEJA IGUAL AO Y DA COMIDA VAI VARIAR SOMENTE O X DO PACMAN
                        inimigo.setxy(-speed,0)
                    elif inimigo.pos_y == inimigo.meta[1] and inimigo.pos_x < inimigo.meta[0]:
                        inimigo.setxy(speed,0)    
                else:
                    if inimigo.meta == [0,550]:
                        inimigo.meta = [700,0]
                    elif inimigo.meta == [700,0]:
                        inimigo.meta = [0,550]  
            '''  
        else: 
            pass
        
        
    def blitar(inimigo):
        #def blitar(nome,inimigo):        
        #nome.blit(screen,(inimigo.pos_x,inimigo.pos_y))
        if inimigo.nome == "javali":
            javali_esquerda.blit(screen,(inimigo.pos_x,inimigo.pos_y))
            javali_direita.blit(screen,(inimigo.pos_x,inimigo.pos_y))
            javali_sobe.blit(screen,(inimigo.pos_x,inimigo.pos_y))
            javali_desce.blit(screen,(inimigo.pos_x,inimigo.pos_y))
        
        if inimigo.nome == "cobra":
            cobra_esquerda.blit(screen,(inimigo.pos_x,inimigo.pos_y))
            cobra_direita.blit(screen,(inimigo.pos_x,inimigo.pos_y))
            cobra_sobe.blit(screen,(inimigo.pos_x,inimigo.pos_y))
            cobra_desce.blit(screen,(inimigo.pos_x,inimigo.pos_y))
            
    ##################################################################################################
    #    colisao de azukay com os inimigos
    ##################################################################################################
    
    def colisao_azukay(inimigo):
        if azukay.rect.colliderect(inimigo):
            azukay.perdeVida(azukay.getHit)
            azukay.pos_x = random.randint(0,500)
            azukay.pos_y = random.randint(70,500)
    
    
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
    
    shurikens=[]
    
    
    while 1 :
        screen.blit(background,(0,0))
        
        screen.blit(statusbar,(0,0))
        
        perdeu_ganhou()
        
        movimenta_inimigo(inimigo1,inimigo1.getMovimento(),azukay.rect)
        
        movimenta_inimigo(inimigo2,inimigo2.getMovimento(),azukay.rect)
        
        movimenta_inimigo(inimigo3,inimigo3.getMovimento(),azukay.rect)
        
        movimenta_inimigo(inimigo4,inimigo4.getMovimento(),azukay.rect)
        
        #movimenta_inimigo(inimigo5,inimigo5.getMovimento(),azukay.rect)
        
        colisao_azukay(inimigo1)
        
        colisao_azukay(inimigo2)
        
        colisao_azukay(inimigo3)
        
        colisao_azukay(inimigo4)
        
        #colisao_azukay(inimigo5)
        
        ##################################################################################################
        #    Blitando Score
        ##################################################################################################
        global score
        font = pygame.font.Font(None, 40)
        font_score = font.render("Score = " + str(score), True, (255,255,255))
        screen.blit(font_score, (600,10))
        
        ##################################################################################################
        #    Blitando Vidas
        ##################################################################################################
        
        for i in range(azukay.vida):
            screen.blit(vida,((20+i*48),10)) 
        
        
        '''
        ##################################################################################################
        #    blitando inimigos
        ##################################################################################################     
        
           
        javali_esquerda.blit(screen,(inimigo1.pos_x,inimigo1.pos_y))
        javali_direita.blit(screen,(inimigo1.pos_x,inimigo1.pos_y))
        javali_sobe.blit(screen,(inimigo1.pos_x,inimigo1.pos_y))
        javali_desce.blit(screen,(inimigo1.pos_x,inimigo1.pos_y))
        
        cobra_esquerda.blit(screen,(inimigo2.pos_x,inimigo2.pos_y))
        cobra_direita.blit(screen,(inimigo2.pos_x,inimigo2.pos_y))
        cobra_sobe.blit(screen,(inimigo2.pos_x,inimigo2.pos_y))
        cobra_desce.blit(screen,(inimigo2.pos_x,inimigo2.pos_y))
        
        '''
        
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
                global score
                if inimigo1.rect.collidepoint(bullet[1],bullet[2]):
                        inimigo1.perdeVida(azukay.getHit())
                        shurikens.pop(index)
                        score += 256
                        
            colisao(inimigo1,azukay,shurikens)
            colisao(inimigo2,azukay,shurikens)
            colisao(inimigo3,azukay,shurikens)
            colisao(inimigo4,azukay,shurikens)
            #colisao(inimigo5,azukay,shurikens)
            
                                
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