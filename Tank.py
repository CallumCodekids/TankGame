import pygame

class Tank:
    
    def __init__(self,x,y,width, height, image):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image,(self.width,self.height))
        self.speed = 0
        self.angle = 0
        
    def display(self,screen):
        screen.blit(pygame.transform.rotate(self.image,self.angle),
                    (self.x,self.y))
        
    def update(self):
        self.rotate()
        self.back_and_forward()
        
    def rotate(self):
        self.angle = self.angle +1
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            print("a was pressed")
        if keys[pygame.K_d]:
            print("d was pressed")

        
    def back_and_forward(self):
        pass
        