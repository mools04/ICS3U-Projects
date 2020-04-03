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
WOOD = (193, 154, 107)
DARKWOOD = (133, 94, 66)
YELLOW = (255, 241, 115)
GREY = (156, 151, 146)
LIGHTGREY = (204, 201, 192)
ORANGE = (245, 164, 66)
CLOUDWHITE = (242, 242, 242)
SUN1 = (252, 150, 3)
SUN2 = (252, 170, 3)
SUN3 = (252, 190, 3)
SUN4 = (252, 210, 3)
SUN5 = (252, 230, 3)
SUN6 = (252, 250, 3)

SIZE = (1000, 700)

# setting up screen w/ caption and background
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Easter House")
screen.fill(SKYBLUE)

# defining functions
def drawBunny(x, y):
    # draws an easter bunny
    # ears:
    surface = pygame.Surface((25, 50))  # to be able to draw a rotated ellipse, I created a new surface
    surface.fill(GRASSGREEN)  # it needs to blend in with the rest of the background
    pygame.draw.ellipse(surface, WHITE, (0, 0, 25, 50))  # draw the ellipse on this new surface
    pygame.draw.ellipse(surface, PINK, (8, 7, 10, 35))
    surface2 = pygame.transform.rotate(surface, 45)  # rotate the surface (ear 1)
    surface3 = pygame.transform.rotate(surface, 315)  # ear 2
    screen.blit(surface2, (x, y))  # 55, 50 put the new surface on the original surface
    screen.blit(surface3, (x + 80, y))  # 135, 50
    # head:
    pygame.draw.circle(screen, WHITE, (x + 67, y + 70), 35)
    pygame.draw.circle(screen, BLACK, (x + 75, y + 70), 3)  # eyes:
    pygame.draw.circle(screen, BLACK, (x + 45, y + 70), 3)
    # body:
    pygame.draw.ellipse(screen, WHITE, (x + 55, y + 85, 60, 50))
    pygame.draw.ellipse(screen, WHITE, (x + 65, y + 130, 25, 10))
    pygame.draw.ellipse(screen, WHITE, (x + 90, y + 128, 25, 10))
    pygame.draw.circle(screen, WHITE, (x + 120, y + 110), 10)

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
    # draws one fencepost (to be repeated line 164)
    pygame.draw.polygon(screen, BEIGE, [(x, y), (x + 30, y), (x + 30, y - 100), (x + 15, y - 110), (x, y - 100)])

def drawCloud():
    # random numbers:
    x = random.randint(0, 1000)
    y = random.randint(40, 50)
    # ellipse and circles to form cloud
    pygame.draw.ellipse(screen, CLOUDWHITE, (x - 25, y - 5, 220, 100))
    pygame.draw.circle(screen, CLOUDWHITE, (x + 20, y + 30), 50)
    pygame.draw.circle(screen, CLOUDWHITE, (x + 80, y + 20), 60)
    pygame.draw.circle(screen, CLOUDWHITE, (x + 150, y + 30), 50)

def drawWindow(x, y):
    # draws one window
    pygame.draw.rect(screen, WHITE, (x, y, 100, 100))
    pygame.draw.rect(screen, SKYBLUE, (x + 10, y + 10, 80, 80))
    pygame.draw.rect(screen, WHITE, (x + 45, y, 10, 100))
    pygame.draw.rect(screen, WHITE, (x, y + 45, 100, 10))
    x = x + 20
    y = y + 35
    # reflective lines
    pygame.draw.polygon(screen, WHITE, [(x, y), (x + 2, y), (x + 4, y - 24), (x + 2, y - 24)])
    pygame.draw.polygon(screen, WHITE, [(x + 10, y), (x + 12, y), (x + 14, y - 24), (x + 12, y - 24)])

def drawEgg1(x, y):
    # draws one egg in a random position
    # pink dots on the egg
    pygame.draw.ellipse(screen, WHITE, (x, y, 50, 62))
    pygame.draw.circle(screen, PINK, (x + 25, y + 12), 5)
    pygame.draw.circle(screen, PINK, (x + 37, y + 20), 5)
    pygame.draw.circle(screen, PINK, (x + 15, y + 25), 5)
    pygame.draw.circle(screen, PINK, (x + 40, y + 32), 5)
    pygame.draw.circle(screen, PINK, (x + 10, y + 32), 5)
    pygame.draw.circle(screen, PINK, (x + 25, y + 50), 5)
    pygame.draw.circle(screen, PINK, (x + 12, y + 12), 5)
    pygame.draw.circle(screen, PINK, (x + 25, y + 31), 5)

def drawEgg2(x, y):
    pygame.draw.ellipse(screen, YELLOW, (x, y, 50, 62))

def drawBird(x, y):
    pygame.draw.ellipse(screen, YELLOW, (x, y, 40, 20))  # body of the bird
    pygame.draw.polygon(screen, GREY, [(x + 35, y + 10), (x + 45, y + 10), (x + 35, y + 15)])  # beak
    pygame.draw.circle(screen, BLACK, (x + 25, y + 10), 2)  # eye
    pygame.draw.line(screen, BLACK, (x + 5, y + 16), (x + 2, y + 20), 2)  # claw

def drawBark(x, y):
    pygame.draw.line(screen, DARKWOOD, (x, y), (x, y + 25), 2)


# fills part of the screen green, thus drawing grass
pygame.draw.rect(screen, GRASSGREEN, (0, 500, 1000, 500))

# draws the sun in a random position (in the sky)
sunX = random.randint(0, 800)
sunY = random.randint(0, 50)
pygame.draw.circle(screen, YELLOW, (sunX, sunY), 100)
pygame.draw.rect(screen, SUN1, (sunX - 100, sunY + 71, 200, 29))
pygame.draw.rect(screen, SUN2, (sunX - 100, sunY + 42, 200, 29))
pygame.draw.rect(screen, SUN3, (sunX - 100, sunY + 13, 200, 29))
pygame.draw.rect(screen, SUN4, (sunX - 100, sunY - 16, 200, 29))
pygame.draw.rect(screen, SUN5, (sunX - 100, sunY - 45, 200, 29))
pygame.draw.rect(screen, SUN6, (sunX - 100, sunY - 74, 200, 29))
pygame.draw.circle(screen, SKYBLUE, (sunX, sunY), 150, 50)

# draws the clouds
drawCloud()

# drawing the tree:
pygame.draw.rect(screen, WOOD, (80, 300, 30, 200))  # trunk
pygame.draw.polygon(screen, BLADEGREEN, [(10, 350), (180, 350), (95, 250)])  # leaves
pygame.draw.polygon(screen, BLADEGREEN, [(10, 310), (180, 310), (95, 210)])
pygame.draw.polygon(screen, BLADEGREEN, [(10, 270), (180, 270), (95, 170)])

# lines on the bark using the drawBark() function
drawBark(90, 350)
drawBark(97, 390)
drawBark(100, 350)
drawBark(100, 450)

counter1 = 0
k = 340
# this loop repeatedly draws the chain links to connect with the seat of the swing set:
while counter1 < 11:
    k = k + 10
    pygame.draw.ellipse(screen, GREY, (175, k, 6, 10), 3)
    pygame.draw.ellipse(screen, GREY, (120, k, 6, 10), 3)
    counter1 = counter1 + 1
pygame.draw.arc(screen, BLACK, (124, 440, 57, 40), math.pi, 0, 10)  # seat (black arc)

# draws the basic house
drawHouse()
drawWindow(325, 300)  # draws the first window
drawWindow(575, 300)  # draws the second window (using the same function, different parameters)

# door
pygame.draw.circle(screen, WOOD, (500, 400), 60)
pygame.draw.rect(screen, WOOD, (440, 400, 120, 100))
# lines on door
pygame.draw.line(screen, DARKWOOD, (440, 400), (440, 500), 3)
pygame.draw.line(screen, DARKWOOD, (460, 356), (460, 500), 3)
pygame.draw.line(screen, DARKWOOD, (480, 345), (480, 500), 3)
pygame.draw.line(screen, DARKWOOD, (500, 342), (500, 500), 3)
pygame.draw.line(screen, DARKWOOD, (520, 346), (520, 500), 3)
pygame.draw.line(screen, DARKWOOD, (540, 357), (540, 500), 3)
pygame.draw.line(screen, DARKWOOD, (560, 400), (560, 500), 3)

# loop that draws 10 blades of grass
counter = 0
while counter < 10:
    drawBlades()
    counter = counter + 1

# the following is a loop that draws the fence posts repeatedly across the screen, using the drawFence() function's parameters
counter2 = 0
drawFence(0, 500)
while counter2 < 1000:
    counter2 = counter2 + 60
    drawFence(counter2, 500)

# line to connect the fence posts done by drawFence()
pygame.draw.rect(screen, BEIGE, (0, 425, 1000, 20))

# this loop draws the singles in layers of 12 over the roof, using the parameters of the drawShingles() function.
shinglesX = 220
counter3 = 0
while counter3 < 12:
    shinglesX = shinglesX + 40
    drawShingles(shinglesX, 210)
    drawShingles(shinglesX, 190)
    drawShingles(shinglesX, 170)
    drawShingles(shinglesX, 150)
    drawShingles(shinglesX, 130)
    counter3 = counter3 + 1

# polygons to hide access shingles
pygame.draw.polygon(screen, SKYBLUE, [(740, 250), (500, 150), (800, 150), (900, 250)])
pygame.draw.polygon(screen, SKYBLUE, [(260, 250), (500, 150), (200, 150), (100, 150)])

eggX1 = random.randint(0, 1000)
eggX2 = random.randint(0, 1000)
eggX3 = random.randint(0, 1000)

# draw 3 eggs
drawEgg1(eggX1, 438)
drawEgg1(eggX2, 438)
drawEgg2(eggX3, 438)

drawBunny(random.randint(0, 900), random.randint(500, 550)) # drawing a bunny using the drawBunny() function and random

drawBird(random.randint(0, 960), random.randint(0, 500)) # drawing two birds using drawBird() and random
drawBird(random.randint(0, 960), random.randint(0, 500))

pygame.display.flip()
pygame.time.wait(10000)
pygame.quit()

# question:
# - definition of "fully commented"?
# things to add:
# - details on sun
# - better eggs
# - window on door
