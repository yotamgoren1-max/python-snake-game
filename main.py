import time
import pygame #imports
import config
import game_objects

pygame.init()  #starting the pygame Tools
screen=pygame.display.set_mode((config.WINDOW_WIDTH,config.WINDOW_HEIGHT)) #creates the monitor
pygame.display.set_caption("python-Snake-Game")
running=True
clock=pygame.time.Clock() #creating the clock
curr_score=0 #number of apples

grid_surface=pygame.Surface((config.WINDOW_WIDTH,config.WINDOW_HEIGHT)) #creating the basic grid screen
game_objects.basic_screen(grid_surface)

score_font=pygame.font.Font(None,36) #creating the basic class for a text

while running: #the main loop of the game
    for event in pygame.event.get(): #check for every event possible
        if event.type == pygame.QUIT:
            running = False # if the event is QUIT End the loop

    score_text="score: " + str(curr_score) #score tracker
    text_score_surface=score_font.render(score_text,True,config.WHITE)

    screen.blit(grid_surface,(0,0))
    screen.blit(text_score_surface,(20,20))

    curr_level=(curr_score//5)+1 #start from level 1
    curr_fps=min(config.INITIAL_FPS+(curr_score//5 * config.SPEED_BOOST_PER_LEVEL),config.MAX_FPS)
    clock.tick(curr_fps)




    pygame.display.update() #update the screen for each event

pygame.quit() #end the pygame init func