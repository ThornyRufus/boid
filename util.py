import pygame
from math import cos,sin,radians

def vectorSearch(surface,start,angle,length):
    colorList = []
    for i in range(10,length):
        point = [start.x + cos(radians(angle))*i ,start.y + sin(radians(angle))*i]
        colorList.append(surface.get_at(point))

    #return if boid found or not