import pygame
import math

pygame.init()


WIDTH = HEIGHT = 500
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Fidget Spinner")
clock = pygame.time.Clock()
done = False

CENTER = (WIDTH//2,HEIGHT//2)

class Spinner:
    
    colors = [(255,0,0),(0,255,0),(0,0,255)]
    def __init__(self,length=20):
        '''spinner with passed in length to represent length of the arms'''
        self.initial_degrees = 0 #initial orientation of red circle
        self.degree_speed = 0 #how many degrees per frame is it turning
        self.length = length

    def draw(self):
        CENTER_X,CENTER_Y = CENTER
        start_degrees = self.initial_degrees 
        
        for i in range(3):
            degree = start_degrees + 120 * i
            degree_radians = degree * math.pi /180
            pygame.draw.line(screen,(0,0,0),CENTER,(CENTER_X + math.cos(degree_radians) * self.length,CENTER_Y - math.sin(degree_radians) * self.length),20)
            pygame.draw.circle(screen,self.colors[i],(CENTER_X + int(math.cos(degree_radians) * self.length),int(CENTER_Y - math.sin(degree_radians) * self.length)),100)

    
    def spin(self):
        self.degree_speed += 1

        self.degree_speed = min(self.degree_speed,50)

    def update(self):
        self.initial_degrees += self.degree_speed
        
        self.degree_speed -= 1/30

        self.degree_speed = max(0,self.degree_speed)


spinner = Spinner(150)

while not done:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                spinner.spin()
    
    print(spinner.degree_speed)
    spinner.update()
    
    screen.fill((255,255,255))
    spinner.draw()
    pygame.display.update()
    clock.tick(30)










