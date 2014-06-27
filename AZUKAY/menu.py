import pygame , sys

pygame.init()        

pygame.display.set_caption('##############  AZUKAY ############### ')

size = 800,600
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

#Carregando os BACKGROUNDS

bg_config = pygame.image.load("Sprites/bg/azuka_config.png")
bg = pygame.image.load("Sprites/bg/azuka.png")
bg_level = pygame.image.load("Sprites/bg/azuka_selecao.png")

#AUDIO

pygame.mixer.init()
musica = pygame.mixer.Sound('sons/MENU.wav')   
musica.play()

clock.tick(30)

def selecao_fase():
    while 1:
        for event in pygame.event.get():                     
            if event.type == pygame.QUIT: 
                sys.exit()
            if event.type==pygame.MOUSEBUTTONDOWN:                    
                pos = pygame.mouse.get_pos()
                
                if (pos[1] > 50) and (pos[1]< 132) and ((pos[0]>48) and (pos[0]<370)):
                    musica.stop()
                    import teste
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
        
menu_principal()