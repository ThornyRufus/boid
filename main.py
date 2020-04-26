import pygame, sys
pygame.init()

back_color = pygame.Color('#86BBD8')
boid_color = pygame.Color('#2F4858')
object_list = []


class boid:
    def __init__(self,surface,size,posx, posy):
        self.surface = surface
        self.size = size
        self.posx = posx
        self.posy = posy

    def draw(self):
        body_points = [(self.posx - (self.size / 2), self.posy), (self.posx + (self.size / 2), self.posy),
                       (self.posx, self.posy + self.size)]
        body = pygame.draw.polygon(self.surface,boid_color,body_points,0)


class arena:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        #pygame.display.set_icon()
        pygame.display.set_caption('BOID simulation')
        screen = pygame.display.set_mode([self.x,self.y])
        screen.fill(back_color)

        for i in range(20):
            object_list.append(boid(screen,20,50+30*i,50))

        pygame.display.update()
        clock = pygame.time.Clock()

        while True:
            clock.tick(50)

            # Process events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            #clear screen
            screen.fill(back_color)

            # Check input

            for i in range(len(object_list)):
                object_list[i].posy += 2*(i+1)
            for object in object_list:
                if object.posx > self.x:
                    object.posx = 0
                if object.posx < 0:
                    object.posx = self.x
                if object.posy < 0:
                    object.posy = self.y
                if object.posy > self.y:
                    object.posy = 0

            # Move objects ...
            for object in object_list:
                object.draw()

            # Draw objects ...

            # Update the screen
            pygame.display.flip()
'''
        pygame.event.clear()
        pygame.event.wait()
'''



display = arena(800,400)