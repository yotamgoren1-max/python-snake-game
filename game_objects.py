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

class Snake:

    def __init__(self):
        self.x = (config.WINDOW_WIDTH // 2 // config.CELL_SIZE) * config.CELL_SIZE  # middle of the screen
        self.y = (config.WINDOW_HEIGHT // 2 // config.CELL_SIZE) * config.CELL_SIZE
        self.body=[]
        head_po=pygame.Rect((self.x, self.y, config.CELL_SIZE, config.CELL_SIZE))
        body_po=pygame.Rect((self.x-config.CELL_SIZE, self.y, config.CELL_SIZE, config.CELL_SIZE))
        self.body.append(head_po)
        self.body.append(body_po)
        self.surface = pygame.Surface((config.CELL_SIZE, config.CELL_SIZE))  # the surface of the head and fill it with green
        self.surface.fill(config.GREEN)
        self.direction = config.RIGHT

    def draw(self,surface):
        for i in range (0,len(self.body)):
            surface.blit(self.surface, self.body[i])

    def move (self):
        new_x = self.body[0].x + self.direction[0]
        new_y = self.body[0].y + self.direction[1]
        new_head=pygame.Rect((new_x, new_y, config.CELL_SIZE, config.CELL_SIZE))
        self.body.insert(0,new_head)
        self.body.pop()

    def grow (self):
        dir_x = self.body[-1].x - self.body[-2].x
        dir_y = self.body[-1].y - self.body[-2].y
        new_x = self.body[-1].x + dir_x
        new_y = self.body[-1].y + dir_y
        new_tail=pygame.Rect((new_x, new_y, config.CELL_SIZE, config.CELL_SIZE))
        self.body.append(new_tail)

    def check_apple_collision(self,apple):
        return self.body[0].colliderect(apple.rect)


    def check_wall_collision(self):
        flag=False
        head=self.body[0]
        if head.x < 0 or head.x >= config.WINDOW_WIDTH or head.y < 0 or head.y >= config.WINDOW_HEIGHT:
            flag=True
        return flag

    def check_self_collision(self):
        head = self.body[0]
        for i in range(1,len(self.body)):
            if head.x== self.body[i].x and head.y== self.body[i].y:
                return True
        return False









