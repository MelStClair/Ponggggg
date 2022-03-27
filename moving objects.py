import pygame

pygame.init()

# Set up the drawing window
size = width, height = 500, 500
screen = pygame.display.set_mode(size)


# create rect object (rect objecta are basically the hitboxes of the objects we draw)
rect1 = pygame.Rect((20, 50),(100, 100))

# Run until the user asks to quit
running = True
state= "none"
while running:
    # this goes in one direction until we let go of the button
    if state == "W":
        rect1.move_ip(0, -10)
    elif state == "A":
        rect1.move_ip(-10, 0)
    elif state == "S":
        rect1.move_ip(0, 10)
    elif state == "D":
        rect1.move_ip(10, 0)

    # event handling - we wait for event
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        running = False
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            pygame.quit()
        # build a state machine for each button press
        if event.key == pygame.K_w:
            state = "W"
            rect1.move_ip(0, -10)  # move the rect object by given int offset
        if event.key == pygame.K_a:
            state = "A"
            rect1.move_ip(-10, 0)  # move the rect object by given int offset
        if event.key == pygame.K_s:
            state = "S"
            rect1.move_ip(0, 10)  # move the rect object by given int offset
        if event.key == pygame.K_d:
            state = "D"
            rect1.move_ip(10, 0)  # move the rect object by given int offset
    if event.type == pygame.KEYUP:
        state = "none"



    # Fill the background with white
    screen.fill((255, 255, 255))

    # do the comedian leaving-room-entering-from-other-side thing
    # TODO: fix the mod thing because the pov is the upper left vertices
    rect1.left %= width
    rect1.top %= height
    # draw rect
    pygame.draw.rect(screen, (250,0,0),rect1)


    # Flip the display aka apply changes
    pygame.display.flip()


# Done! Time to quit.
print("i quit.")
pygame.quit()

# todo: make controls less clunky - cant handle 2 buttons at once