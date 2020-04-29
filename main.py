import pygame, sys

from random import randrange
from statistics import median
from math import cos,sin,radians,pow,sqrt
pygame.init()

back_color = pygame.Color('#86BBD8')
boid_color = pygame.Color('#2F4858')
red_color = pygame.Color('#FF0000')
global screen
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800


class boid:

    def __init__(self,size,speed=1):
        global screen
        self.size = size
        self.posx = randrange(0,SCREEN_WIDTH)
        self.posy = randrange(0,SCREEN_HEIGHT)
        self.speed = speed
        self.total_angle = randrange(0,360)
        self.objective = randrange(0,360)
        self.alpha = radians(self.total_angle % 360)
        self.turn_speed = 1

    def find_objective(self,object_list):

        for object in object_list:
            near_list = []
            danger_list = []
            vect = []
            vect.append(self.posx - object.posx)
            vect.append(self.posy - object.posy)
            dist = sqrt( pow(vect[0],2) + pow(vect[1],2) )

            if dist < 300:
                near_list.append(object)
            if dist < 1:
                danger_list.append(object)
            if len(near_list) == 0:
                self.turn_speed = 1
                self.objective = randrange(0,360)
            elif len(danger_list) > 100000: #dont use danger list anymore
                self.turn_speed = 10
                angle_list = []
                for object in danger_list:
                    angle_list.append(object.alpha)
                self.objective = (median(angle_list) + 180)%360
            else:
                self.turn_speed = 1
                angle_list = []
                for object in near_list:
                    angle_list.append(object.alpha)
                self.objective = median(angle_list)

    '''
    def refactoredFindObj(self,board):
        center = (self.x,self.y)
        radius = 100
        direction = self.alpha
    '''


    def actualize(self):
        self.alpha = radians(self.total_angle % 360)
        self.beta = radians((self.total_angle + 90) % 360)
        self.delta = radians((self.total_angle + 270) % 360)

    def draw(self):
        self.actualize()
        self.body_points = [(self.posx + ( cos(self.alpha) * self.size ), self.posy + ( sin(self.alpha) * self.size ) ),
                                    (self.posx + ( cos(self.beta) * (self.size/3) ), self.posy + ( sin(self.beta) * (self.size/3) ) ),
                                    (self.posx + ( cos(self.delta) * (self.size/3) ), self.posy + ( sin(self.delta) * (self.size/3) ) )]
        body = pygame.draw.polygon(screen,boid_color,self.body_points,0)



    def move(self,speed=10):

        if self.objective > self.alpha:
            self.total_angle += self.turn_speed
        if self.objective < self.alpha:
            self.total_angle -= self.turn_speed
        self.actualize()

        self.posx +=  int(( cos(self.alpha) * speed ))
        self.posy += int(( sin(self.alpha) * speed ))



class arena:
    def __init__(self,x,y,bd_num):
        self.width = x
        self.height = y

        self.object_list = []
        #pygame.display.set_icon()
        pygame.display.set_caption('BOID simulation')
        global screen
        screen = pygame.display.set_mode([self.width,self.height])
        screen.fill(back_color)

        for i in range(bd_num):
            self.object_list.append(boid(randrange(5,25)))

        pygame.display.update()
        clock = pygame.time.Clock()

        while True:
            clock.tick(60)

            # Process events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            #clear screen
            screen.fill(back_color)

            for object in self.object_list:
                object.find_objective(self.object_list)

                object.move()



            for object in self.object_list: #a changer, methode pour remetre les objets dans le cadre
                if object.posx > self.width:
                    object.posx = 0
                if object.posx < 0:
                    object.posx = self.width
                if object.posy < 0:
                    object.posy = self.height
                if object.posy > self.height:
                    object.posy = 0

            # Move objects ...
            for object in self.object_list: #draw, pas de probleme
                object.draw()

            # Draw objects ...

            # Update the screen
            pygame.display.flip()
'''
        pygame.event.clear()
        pygame.event.wait()
'''
display = arena(SCREEN_WIDTH,SCREEN_HEIGHT,100)