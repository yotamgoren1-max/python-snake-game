import pygame #imports
import config
import game_objects
pygame.init()  #starting the pygame Tools
screen=pygame.display.set_mode() #creates the monitor
running=True

while running: #the main loop of the game
    for event in pygame.event.get(): #check for every event possible
        if event.type == pygame.QUIT:
            running = False # if the event is QUIT End the loop




    pygame.display.update() #update the screen for each event
