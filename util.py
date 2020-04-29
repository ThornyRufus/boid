import pygame
from math import cos,sin,radians



def vectorSearch(surface,start,angle,length=100,SCREEN_WIDTH=1200,SCREEN_HEIGHT=800):
    colorList = []
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
        colorList.append(surface.get_at(point))



    #return if boid found or not