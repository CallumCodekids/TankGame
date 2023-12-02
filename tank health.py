import pygame
 
class tank_healthbar:
     def __init__ (x, y, height, image):
        self.x = x
        self.y = y
        self.height = height
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image,(self.width,self.height))
    
    def display(self,screen):
        screen.blit(self.image,(self.x,self.y))
        
    def get_rect(self):
        return pygame.Rect(self.x,self.y,self.width,self.height)

