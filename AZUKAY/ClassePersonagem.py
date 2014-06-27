import pygame

class Personagem():
    def __init__(self,nome,hit,vida,pos_x, pos_y):
        self.nome = nome
        self.pos_x = pos_x 
        self.pos_y = pos_y
        self.vida = vida
        self.hit = hit

    def getx(self):
        return self.pos_x

    def gety(self):
        return self.pos_y
    
    def setx (self, x,y):
        self.pos_x = x
        self.pos_y = y
        self.andar(x,y)
        
         
    def andar(self,x,y):
        self.rect.x = x
        self.rect.y = y
        return self.rect.x,self.rect.y
    
    def perdeVida(self):
        if self.nome == "azukay":
            self.vida -= 1
        else:
            self.vida -= self.hit