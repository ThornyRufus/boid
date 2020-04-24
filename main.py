import pygame
pygame.init()

back_color = pygame.Color('#86BBD8')
boid_color = pygame.Color('#2F4858')


class boid:
    def __init__(self,surface,size,posx, posy):
        self.surface = surface
        self.size = size
        self.posx = posx
        self.posy = posy
        body_points = [  (self.posx - (self.size/2),self.posy),(self.posx + (self.size/2),self.posy),(self.posx,self.posy + self.size) ]

        body = pygame.draw.polygon(surface,boid_color,body_points,0)


class arena:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        #pygame.display.set_icon()
        pygame.display.set_caption('BOID simulation')
        screen = pygame.display.set_mode([self.x,self.y])
        screen.fill(back_color)
        boid(screen,20,50,50)
        pygame.display.update()


        pygame.event.clear()
        pygame.event.wait()

display = arena(800,400)