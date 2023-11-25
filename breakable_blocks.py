import pygame
class Breakable_Blocks:
    
    def __init__(self, x, y, width, height, image, shots_per_break):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image,(self.width,self.height))
        self.shots_per_break = shots_per_break
        
    def display(self, screen):
        screen.blit(self.image,(self.x, self.y))
    
    def get_rect(self):
        return pygame.Rect(self.x,self.y,self.width,self.height)