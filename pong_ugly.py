import pygame


pygame.init()

def iquit():
    pygame.quit()


print("welcome to pong: player1 uses W,S Player 2 uses arrows")
print("use space to start a game")
# Set up the drawing window
size = width, height = 700, 500
screen = pygame.display.set_mode(size)
players = p_width, p_height = 30, (height - 100)/4

# create rect objects aka the player avatars and the ball
player1 = pygame.Rect((30, height/2 - p_height/2),(p_width,p_height))
player2 = pygame.Rect((width-30-p_width,height/2 - p_height/2 ),(p_width, p_height ))
pong = pygame.Rect((width/2,height/2), (p_width, p_width))
topWall = pygame.Rect((0,0),(width, 30))
bottomWall = pygame.Rect((0,height - 30),(width, 30)) # coordinates upper left corner, width and height

# starting screen (starting screen works)
startingScreen = True
while startingScreen:
    startscreenEvent = pygame.event.wait()
    if startscreenEvent.type == pygame.QUIT:
        iquit()
    if startscreenEvent.type == pygame.KEYDOWN:
        if startscreenEvent.key == pygame.K_SPACE:
            print("starting game, get ready")
            startingScreen = False

    screen.fill((255, 255, 255))    # Fill the background with white
    pygame.draw.rect(screen, (165, 165, 165), topWall)
    pygame.draw.rect(screen, (165, 165, 165), bottomWall)
    pygame.draw.rect(screen, (0,0,0), player1)
    pygame.draw.rect(screen, (0,0,0), player2)
    pygame.draw.rect(screen, (0,0,0), pong)

    pygame.display.flip()

# Run until the user asks to quit
running = True
stateP1 = "none"
stateP2 = "none"
while running:

    # keeping button pressed P1
    if stateP1 == "W":
        player1.move_ip(0, -1)
    elif stateP1 == "S":
        player1.move_ip(0, 1)

    # keeping button pressed P2
    if stateP2 == "up":
        player2.move_ip(0, -1)
    elif stateP2 == "down":
        player2.move_ip(0,1)

    # event handling - we wait for event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()

            # build a state machine for each button press
            #player 1 events
            if event.key == pygame.K_w:

                stateP1 = "W"
                player1.move_ip(0, -1)  # move the rect object by given int offset
            elif event.key == pygame.K_s:
                stateP1 = "S"
                player1.move_ip(0, 1)  # move the rect object by given int offset

            # player2 events
            if event.key == pygame.K_UP:
                print("p2 ")
                stateP2 = "up"
                player2.move_ip(0, -1)
            elif event.key == pygame.K_DOWN:
                stateP2 = "down"
                player2.move_ip(0, 1)

        # pong events
        # implement this

    # reset state
    if event.type == pygame.KEYUP:
        if (event.key == pygame.K_w) or (event.key == pygame.K_s):
            stateP1 = "none"
        elif (event.key == pygame.K_UP) or (event.key == pygame.K_DOWN):
            stateP2 = "none"



    # Fill the background with white
    screen.fill((255, 255, 255))

    """
    # do the comedian leaving-room-entering-from-other-side thing
    # TODO: fix the mod thing because the pov is the upper left vertices
    rect1.left %= width
    rect1.top %= height
    """
    # draw game todo: make this a function
    pygame.draw.rect(screen, (165, 165, 165), topWall)
    pygame.draw.rect(screen, (165, 165, 165), bottomWall)
    pygame.draw.rect(screen, (0, 0, 0), player1)
    pygame.draw.rect(screen, (0, 0, 0), player2)
    pygame.draw.rect(screen, (0, 0, 0), pong)


    # Flip the display aka apply changes
    pygame.display.flip()

# Done! Time to quit.
print("i quit.")
pygame.quit()

# todo: make controls less clunky - cant handle 2 buttons at once