import pygame, sys, math, random, statistics
pygame.init()

back_color = pygame.Color('#86BBD8')
boid_color = pygame.Color('#2F4858')


class boid:
    def __init__(self,surface,size,posx, posy,speed=1):
        self.surface = surface
        self.size = size
        '''
        self.posx = posx
        self.posy = posy
        '''
        self.posx = random.randrange(0,1920)
        self.posy = random.randrange(0,1080)
        self.speed = speed
        self.total_angle = random.randrange(0,360)
        self.objective = 0
        self.alpha = math.radians(self.total_angle % 360)

    def find_objective(self,object_list):

        for object in object_list:
            near_list = []
            vect = []
            sum = 0
            vect.append(self.posx - object.posx)
            vect.append(self.posy - object.posy)
            dist = math.sqrt( math.pow(vect[0],2) + math.pow(vect[1],2) )

            if dist < 300:
                near_list.append(object)
            if len(near_list) == 0:
                self.objective = 0
            else:
                angle_list = []
                for object in near_list:
                    angle_list.append(object.alpha)
                self.objective = statistics.median(angle_list)

    def actualize(self):
        self.alpha = math.radians(self.total_angle % 360)
        self.beta = math.radians((self.total_angle + 90) % 360)
        self.delta = math.radians((self.total_angle + 270) % 360)

    def draw(self):
        self.actualize()
        self.body_points = [(self.posx + ( math.cos(self.alpha) * self.size ), self.posy + ( math.sin(self.alpha) * self.size ) ),
                                    (self.posx + ( math.cos(self.beta) * (self.size/3) ), self.posy + ( math.sin(self.beta) * (self.size/3) ) ),
                                    (self.posx + ( math.cos(self.delta) * (self.size/3) ), self.posy + ( math.sin(self.delta) * (self.size/3) ) )]
        body = pygame.draw.polygon(self.surface,boid_color,self.body_points,0)

    def move(self,speed=10): #calculer les nouveaux body points selon l'angle

        if self.objective > self.alpha:
            self.total_angle += 1
        if self.objective < self.alpha:
            self.total_angle -= 1
        self.actualize()
        self.posx +=  ( math.cos(self.alpha) * speed )
        self.posy += ( math.sin(self.alpha) * speed )

class arena: #classe principale, initialisation et game loop
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.object_list = []
        #pygame.display.set_icon()
        pygame.display.set_caption('BOID simulation')
        screen = pygame.display.set_mode([self.x,self.y])
        screen.fill(back_color)

        for i in range(120):
            self.object_list.append(boid(screen,25,50+i*15,50+i*3))

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
                #object.total_angle += random.randrange(-5,5)
                object.move()


            for object in self.object_list: #a changer, methode pour remetre les objets dans le cadre
                if object.posx > self.x:
                    object.posx = 0
                if object.posx < 0:
                    object.posx = self.x
                if object.posy < 0:
                    object.posy = self.y
                if object.posy > self.y:
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
display = arena(1920,1080)