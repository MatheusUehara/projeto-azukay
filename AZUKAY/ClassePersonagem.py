##################################################################################################
# Classe com nome . vida , tipo de movimentacao , e tudo a respeito dos personagens do jogo ... 
##################################################################################################
import pygame


class Personagem:
    inimigos = []
    
    def __init__(self,nome,hit,vida,pos_x, pos_y,movimento,caminho):
        self.nome = nome
        self.pos_x = pos_x 
        self.pos_y = pos_y
        self.vida = vida
        self.hit = hit
        self.movimento = movimento
        self.caminho = pygame.image.load(caminho)
        
    def do_Rect(self):
        if self.nome == 'azukay':
            self.rect = pygame.Rect(self.pos_x, self.pos_y, 60, 100)
        elif self.nome == 'cobra':
            self.rect = pygame.Rect(self.pos_x, self.pos_y, 44, 72)
        elif self.nome == 'escorpiao':
            self.rect = pygame.Rect(self.pos_x, self.pos_y, 48, 67)
        elif self.nome == 'javali':
            self.rect = pygame.Rect(self.pos_x, self.pos_y, 46, 51)
                        
    def blita(self,screen):
        #if tipo == 1 :
        if self.morreu() == 0 :
            screen.blit(self.caminho,(self.pos_x,self.pos_y))             
            
    def setCaminho(self,caminho):
        self.caminho = caminho
        
    def getMovimento(self):
        return self.movimento
    
    def getHit(self):
        return self.hit

    def getx(self):
        return self.pos_x    
    
    def gety(self):
        return self.pos_y
        
    def setxy (self, x,y):
        self.pos_x += x
        self.pos_y += y
        self.moveRect(self.pos_x,self.pos_y)
         
    def moveRect(self,x,y):
        self.rect.x = x
        self.rect.y = y
        return self.rect.x,self.rect.y
    
    def morreu(self):
        if self.vida > 0:
            return 0
        else: 
            self.setxy(900,800)
            return 1           
        
    ##################################################################################################
    # when i will pass parameters hit = azukay.getHit()
    ##################################################################################################
    
    def perdeVida(self,hit):
        if self.nome == "azukay":
            self.vida -= 1
        else:
            self.vida -= hit

            
            
        
            