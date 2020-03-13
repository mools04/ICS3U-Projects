#Myles Anderson Easter House
#imports:
import os
import pygame
import random
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d, %d" %(20, 20)

pygame.init() #initialise pygame

#defining colours and constants
RED = (255, 0, 0)
BLACK = (0, 0, 0)
SKYBLUE = (155, 239, 250)
PINK = (237, 149, 212)
GRASSGREEN = (117, 209, 100)
BLADEGREEN = (98, 176, 84)
BEIGE = (237, 228, 183)

SIZE = (1000, 700)

#setting up screen w/ caption and background
screen = pygame.display.set_mode(SIZE) 
pygame.display.set_caption("Easter House")
screen.fill(SKYBLUE)

def drawGrass():
    #fills part of the screen green, thus drawing grass
    pygame.draw.rect(screen, GRASSGREEN, (0, 500, 1000, 500))

def drawBlades():
    #blades of grass with random coordinates
    x = random.randint(0, 1000)
    y = random.randint(500, 700)
    pygame.draw.polygon(screen, BLADEGREEN, [(x, y), (x+5, y-20), (x+10, y)])

def drawHouse():
    #draws the base of the house
    pygame.draw.polygon(screen, BEIGE, [(450, 500), (650, 500), (660, 420), (440, 420)])
    #even out top and enlarge
    
#things to add:
#easter egss
#windows, door different shapes
#bunnies (if time)

drawGrass()
drawHouse()
a = 0
while a < 10:
    drawBlades()
    a = a+1
    
pygame.display.flip()
pygame.time.wait(3000)
pygame.quit()
