import pygame
class Collectables:
    def __init__ (self, x, y, width, height, image, cannon_increase):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image,(self.width,self.height))
        self.cannon_increase = cannon_increase
    
    def display(self,screen):
        screen.blit(self.image,(self.x,self.y))
        
    def get_rect(self):
        return pygame.Rect(self.x,self.y,self.width,self.height)
