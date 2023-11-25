class Pickle_Power:

    def __init__(self, x, y, width, length, image, speed, angle):
        self.x = x
        self.y = y
        self.width = width
        self.length = length
        self.image = pygame.image.load("Pickle bullet.png")
        self.image = pygame.transform.scale(self.image,(self.width, self.height))
        self.angle = angle
        
    def display (self, screen):
        screen.blit(pygame.transform.rotate(self.image, self.angle),
                    (self.x,self.y))
        
    def update (self):
        x = math.sin(math.radians(self.angle))*self.speed
        y = math.cos(math.radians(self.angle))*self.speed
        self.x = self.x - x
        self.y = self.y - y 
        
    
    
        
        
        
    
    
                     