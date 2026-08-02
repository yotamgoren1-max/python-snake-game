import pygame
import config
import random

#draw the main screen with Grid of lines my 20 x 20 cells
def basic_screen(surface):
    for x in range (0,config.WINDOW_WIDTH,config.CELL_SIZE):
        pygame.draw.line(surface,(40,40,40),(x,0),(x,config.WINDOW_HEIGHT))
    for y in range (0,config.WINDOW_HEIGHT,config.CELL_SIZE):
        pygame.draw.line(surface,(40,40,40),(0,y),(config.WINDOW_WIDTH,y))

class Apple:

    def __init__(self):
        self.x=(config.WINDOW_WIDTH // 2 // config.CELL_SIZE) * config.CELL_SIZE # middle of the screen
        self.y=(config.WINDOW_HEIGHT // 2 // config.CELL_SIZE) * config.CELL_SIZE
        self.surface=pygame.Surface((config.CELL_SIZE,config.CELL_SIZE))#the surface of the apple and fill it with red
        self.surface.fill(config.RED)
        self.rect=pygame.Rect(self.x,self.y,config.CELL_SIZE,config.CELL_SIZE) #the position of the apple starting from the middle

    # for every apple that have been eaten get a random location new
    def Random_Apple(self):
        new_x= random.randrange(0,config.WINDOW_WIDTH, config.CELL_SIZE)
        new_y= random.randrange(0,config.WINDOW_HEIGHT, config.CELL_SIZE)
        self.x=new_x
        self.y=new_y
        self.rect.x=new_x #update the rect object
        self.rect.y=new_y

    # draw the apple to the surface
    def draw_apple(self,surface):
        surface.blit(self.surface, self.rect)





