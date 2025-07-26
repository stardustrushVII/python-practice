import pygame
import sys

# initial setup
pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Sonic Forces sux")

# colours (RGB)
WHITE = (255, 255, 255)
BLUE = (50, 50, 255)
RED = (255, 50, 50)
GREEN = (50, 255, 100)

# main importan loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # background
    screen.fill(RED)

    # shape draw
    pygame.draw.rect(screen, BLUE, (50, 50, 150, 100))         # rectangle
    pygame.draw.circle(screen, RED, (300, 200), 50)            # circle
    pygame.draw.line(screen, GREEN, (400, 300), (550, 350), 5) # line

    # everything show
    pygame.display.flip()

# exit
pygame.quit()
sys.exit()
