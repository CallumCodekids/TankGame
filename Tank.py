import pygame

class Tank:
    
    def __init__(self,x,y,width, height, image):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image,(self.width,self.height))
        
    def display(self,screen):
        screen.blit(self.image,(self.x,self.y))