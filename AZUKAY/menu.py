import pygame , sys

pygame.init()        

pygame.display.set_caption('##############  AZUKAY ############### ')

size = 800,600
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

##################################################################################################
#AUDIO
##################################################################################################

pygame.mixer.init()
musica = pygame.mixer.Sound('sons/MENU.wav')   
musica.play()


def selecao_fase():    
    bg_level = pygame.image.load("Sprites/bg/azuka_selecao.png")
    while 1:
        for event in pygame.event.get():                     
            if event.type == pygame.QUIT: 
                sys.exit()
            if event.type==pygame.MOUSEBUTTONDOWN:                    
                pos = pygame.mouse.get_pos()
                
                if (pos[1] > 50) and (pos[1]< 132) and ((pos[0]>48) and (pos[0]<370)):
                    musica.stop()
                    cut1()                    
                elif (pos[1] >51) and (pos[1]<132) and ((pos[0]>438) and (pos[0]<760)):
                    print ('pegou2')
                elif (pos[1] >190) and (pos[1]<272) and ((pos[0]>240) and (pos[0]<560)):
                    
                    print ('pegou3')        
                elif (pos[1] > 334) and (pos[1]< 416) and ((pos[0]>48) and (pos[0]<370)):
                    
                    print ('pegou4')
                elif (pos[1] >334) and (pos[1]< 416) and ((pos[0]>438) and (pos[0]<760)):
                    
                    print ('pegou5')
                elif (pos[1] >472) and (pos[1]<550) and ((pos[0]>438) and (pos[0]<760)):
                    menu_principal()
        
        screen.blit(bg_level,(0,0))        
        pygame.display.flip() 


def configuracoes():
    bg_config = pygame.image.load("Sprites/bg/azuka_config.png")
    while 1:
        for event in pygame.event.get():                     
            if event.type == pygame.QUIT: 
                sys.exit()
            if event.type==pygame.MOUSEBUTTONDOWN:                    
                pos = pygame.mouse.get_pos()
                if (pos[1] >472) and (pos[1]<550) and ((pos[0]>438) and (pos[0]<760)):
                    menu_principal()
                    
        screen.blit(bg_config,(0,0))
        pygame.display.flip()    
    
def menu_principal():
    while 1:
        bg = pygame.image.load("Sprites/bg/azuka.png")
        for event in pygame.event.get():                     
            if event.type == pygame.QUIT: 
                sys.exit()
            if event.type==pygame.MOUSEBUTTONDOWN:                    
                pos = pygame.mouse.get_pos()
                if (pos[1] > 280) and (pos[1]< 361) and ((pos[0]>450) and (pos[0]<774)):
                    selecao_fase()
                elif (pos[1] >385) and (pos[1]<463) and ((pos[0]>450) and (pos[0]<774)):
                    configuracoes()
                elif (pos[1] >488) and (pos[1]<569) and ((pos[0]>450) and (pos[0]<774)):
                    sys.exit()
                                          
        screen.blit(bg,(0,0))
                
        pygame.display.flip()
        
def cut1():
    cutscene1 = pygame.image.load("Sprites/cutscene/cutscene.png")
    botao_proxima_fase = pygame.image.load("Sprites/cutscene/botao_proxima_fase.png") 
    x,y= 0,90
    while 1:
        screen.fill(0)
        screen.blit(cutscene1,(x,y))
        
        if y > -1152:
            y -= 3.5
            
        else : 
            screen.blit(botao_proxima_fase,(287,460))
            botaorect = botao_proxima_fase.get_rect()
            botaorect.x  = 287
            botaorect.y = 460               
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    sys.exit()
                
    
                if event.type==pygame.MOUSEBUTTONDOWN:             
                    pos = pygame.mouse.get_pos()
                   
                    if botaorect.collidepoint(pos[0],pos[1]):
                            x = open("nivel.txt","r")
                            nivel = x.read()
                            x.close()
                            import ENGINE
                            ENGINE.Jogar(nivel)

                    else: 
                        pass 
         
        pygame.display.flip()       
 
def tela_perdeu():
    x = open("nivel.txt","r")
    nivel = x.read()
    x.close()
    
    bg_perdeu = pygame.image.load("Sprites/bg/bg_morreu.png")
    
    menu = pygame.image.load("Sprites/botoes/menu.png")
    menuRect = menu.get_rect()
    menuRect.x = 90
    menuRect.y = 400
    
    jogar_dnv = pygame.image.load("Sprites/botoes/tentar_novamente.png")
    jogar_dnvRect = jogar_dnv.get_rect()
    jogar_dnvRect.x = 410
    jogar_dnvRect.y =  400
    
    
    while 1:
        screen.blit(bg_perdeu,(0,0))
        screen.blit(menu,(90,400))
        screen.blit(jogar_dnv,(410,400))
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()
            

            if event.type==pygame.MOUSEBUTTONDOWN:             
                pos = pygame.mouse.get_pos()
               
                if menuRect.collidepoint(pos[0],pos[1]):
                    menu_principal()
                    
                elif jogar_dnvRect.collidepoint(pos[0],pos[1]):
                    import ENGINE
                    ENGINE.Jogar(nivel) 
                else: 
                    pass
        pygame.display.flip() 
        
'''
def tela_ganhou(parametro):
    anterior = open("nivel.txt","w")
    anterior.write(str(parametro))
    anterior.close()
    cut2()
'''    
        