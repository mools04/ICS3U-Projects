# Myles Anderson Easter House
# imports:
import pygame, os, random, math

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d, %d" % (20, 20)

pygame.init()  # initialise pygame

# defining colours and constants

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SKYBLUE = (155, 239, 250)
BLUE = (92, 123, 247)
DARKBLUE = (76, 102, 207)
PINK = (255, 176, 251)
PURPLE = (237, 161, 233)
GRASSGREEN = (117, 209, 100)
BLADEGREEN = (98, 176, 84)
BEIGE = (237, 228, 183)
BROWN = (148, 104, 65)
YELLOW = (255, 241, 115)

SIZE = (1000, 700)

# setting up screen w/ caption and background
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Easter House")
screen.fill(SKYBLUE)

def drawBunny(x, y):
    # draws an easter bunny
    # ears:
    surface = pygame.Surface((25, 50)) # to be able to draw a rotated ellipse, I created a new surface
    surface.fill(GRASSGREEN) # it needs to blend in with the rest of the background
    pygame.draw.ellipse(surface, WHITE, (0, 0, 25, 50)) # draw the ellipse on this new surface
    pygame.draw.ellipse(surface, PINK, (8, 7, 10, 35))
    surface2 = pygame.transform.rotate(surface, 45) # rotate the surface (ear 1)
    surface3 = pygame.transform.rotate(surface, 315)
    screen.blit(surface2, (x, y)) # 55, 50 put the new surface on the original surface
    screen.blit(surface3, (x + 80, y)) # 135, 50

    # head:
    pygame.draw.circle(screen, WHITE, (x + 67, y + 70), 35) # 122, 120
    pygame.draw.circle(screen, BLACK, (x + 75, y + 70), 3) # 130, 120 eyes
    pygame.draw.circle(screen, BLACK, (x + 45, y + 70), 3) # 100, 120

    # body:
    pygame.draw.ellipse(screen, WHITE, (x + 55, y + 85, 60, 50)) # 110, 135
    pygame.draw.ellipse(screen, WHITE, (x + 65, y + 130, 25, 10)) # 115, 180
    pygame.draw.ellipse(screen, WHITE, (x + 90, y + 128, 25, 10)) # 145, 180
    pygame.draw.circle(screen, WHITE, (x + 120, y + 110), 10) # 175, 160

def drawBlades():
    # blades of grass with random coordinates
    x = random.randint(0, 1000)
    y = random.randint(500, 700)
    pygame.draw.polygon(screen, BLADEGREEN, [(x, y), (x + 5, y - 20), (x + 10, y)])

def drawHouse():
    # draws the base house (without details, windows, etc.)
    pygame.draw.rect(screen, PINK, (300, 250, 400, 250))  # base of house
    pygame.draw.polygon(screen, BLUE, [(500, 150), (740, 250), (260, 250)])  # roof
    counter = 690
    while 340 < counter < 700:
        pygame.draw.rect(screen, PURPLE, (counter - 40, 251, 10, 250))
        counter = counter - 40
    pygame.draw.rect(screen, PURPLE, (690, 251, 10, 250))

def drawShingles(x, y):
    pygame.draw.arc(screen, DARKBLUE, (x, y, 40, 40), math.pi, 0, 3)

def drawFence(x, y):
    # draws one fencepost (to be repeated below)
    pygame.draw.polygon(screen, BEIGE, [(x, y), (x + 30, y), (x + 30, y - 100), (x + 15, y - 110), (x, y - 100)])

def drawCloud():
    # random numbers:
    x = random.randint(0, 1000)
    y = random.randint(0, 70)
    pygame.draw.ellipse(screen, WHITE, (x, y, 200, 100))
    pygame.draw.ellipse(screen, WHITE, (x+20, y-10, 100, 50))

def drawWindow(x, y):
    # draws one window
    pygame.draw.rect(screen, WHITE, (x, y, 100, 100))
    pygame.draw.rect(screen, SKYBLUE, (x + 10, y + 10, 80, 80))
    pygame.draw.rect(screen, WHITE, (x + 45, y, 10, 100))
    pygame.draw.rect(screen, WHITE, (x, y + 45, 100, 10))
    x = x + 20
    y = y + 35
    pygame.draw.polygon(screen, WHITE, [(x, y), (x + 2, y), (x + 4, y - 24), (x + 2, y - 24)])
    pygame.draw.polygon(screen, WHITE, [(x + 10, y), (x + 12, y), (x + 14, y - 24), (x + 12, y - 24)])

def drawEgg1():
    # draws one egg in a random position
    x = random.randint(0, 1000)
    y = 438

    pygame.draw.ellipse(screen, WHITE, (x, y, 50, 62))
    pygame.draw.circle(screen, PINK, (x + 25, y + 12), 5)
    pygame.draw.circle(screen, PINK, (x + 37, y + 20), 5)
    pygame.draw.circle(screen, PINK, (x + 15, y + 25), 5)
    pygame.draw.circle(screen, PINK, (x + 40, y + 32), 5)
    pygame.draw.circle(screen, PINK, (x + 10, y + 32), 5)
    pygame.draw.circle(screen, PINK, (x + 25, y + 50), 5)
    pygame.draw.circle(screen, PINK, (x + 12, y + 12), 5)
    pygame.draw.circle(screen, PINK, (x + 25, y + 31), 5)

# fills part of the screen green, thus drawing grass
pygame.draw.rect(screen, GRASSGREEN, (0, 500, 1000, 500))

# draws the sun
pygame.draw.circle(screen, YELLOW, (900, 50), 100)
pygame.draw.polygon(screen, YELLOW, [(850, 50), (800, 60), (800, 40)])

# draws the clouds
drawCloud()

drawHouse()  # calling the drawHouse function
drawWindow(325, 300)  # draws the first window
drawWindow(575, 300)  # draws the second window

# door
pygame.draw.circle(screen, BROWN, (500, 400), 60)
pygame.draw.rect(screen, BROWN, (440, 400, 120, 100))

# loop that draws 10 blades of grass
a = 0
while a < 10:
    drawBlades()
    a = a + 1

# the following is a loop that draws the fence repeatedly across the screen
h = 0
drawFence(0, 500)
while h < 1000:
    h = h + 60
    drawFence(h, 500)

# this loop draws the singles in layers of 12 over the roof.
p = 220
counter = 0
while counter < 12:
    p = p + 40
    drawShingles(p, 210)
    drawShingles(p, 190)
    drawShingles(p, 170)
    drawShingles(p, 150)
    drawShingles(p, 130)
    counter = counter + 1

# polygons to hide access shingles
pygame.draw.polygon(screen, SKYBLUE, [(740, 250), (500, 150), (800, 150), (900, 250)])
pygame.draw.polygon(screen, SKYBLUE, [(260, 250), (500, 150), (200, 150), (0, 150)])

# fence connector
pygame.draw.rect(screen, BEIGE, (0, 425, 1000, 20))

# draw 3 eggs
drawEgg1()
drawEgg1()
drawEgg1()

# defining random numbers:
q = random.randint(0, 1000)
w = random.randint(500, 600)
# drawing a bunny
drawBunny(q, w)

pygame.display.flip()
pygame.time.wait(10000)
pygame.quit()
