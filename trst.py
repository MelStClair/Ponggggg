import pygame

pygame.init()

# Set up the drawing window
size = width, height = 500, 500
screen = pygame.display.set_mode(size)


# Run until the user asks to quit
running = True
x = 250
y = 250
r = 50
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False


    # Fill the background with white
    screen.fill((255, 255, 255))


    # Draw a solid blue circle in the center
    pygame.draw.circle(screen, (0, 0, 255), (x, y), r) # circle(surface, color, center, radius) -> Rect
    """
    x += 1
    y += 1
    r += 1
    r %= 300
    x %= 500
    y %= 500
    """
   # draw rectangle: (surface, colour, (x1, x2, y1,y2))
    pygame.draw.rect(screen, (255, 0, 0),(30, 30, 50, 50 ))

    # Flip the display aka apply changes
    pygame.display.flip()


# Done! Time to quit.
pygame.quit()