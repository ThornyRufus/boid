import pygame
from math import cos,sin,radians

back_color = pygame.Color('#86BBD8')
boid_color = pygame.Color('#2F4858')


def LinearSearch(surface,start,angle,length=100,SCREEN_WIDTH=1200,SCREEN_HEIGHT=800):
    farEnough = False
    for i in range(10,length,10):

        posx = start.x + cos(radians(angle))*i
        if posx > SCREEN_WIDTH:
            posx = posx - SCREEN_WIDTH
        elif posx < 0:
            posx = SCREEN_WIDTH - posx

        posy = start.y + sin(radians(angle))*i
        if posy > SCREEN_HEIGHT:
            posy = posy - SCREEN_HEIGHT
        elif posy < 0:
            posy = posy + SCREEN_HEIGHT

        point = [posx, posy]
        if surface.get_at(point) == back_color:
            farEnough = True
        if surface.get_at(point) == boid_color and farEnough == True:
            return True
    return False

def deployVectors(surface,start,startAngle,length,SCREEN_WIDTH=1200,SCREEN_HEIGHT=800):

    while LinearSearch(surface,start,startAngle,length,SCREEN_WIDTH,SCREEN_HEIGHT) == False:
        pass