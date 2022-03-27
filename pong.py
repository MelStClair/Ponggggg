import pygame
import pong_aux

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
# todo fix pong spawn
player1 = pygame.Rect((30, height/2 - p_height/2),(p_width,p_height))
player2 = pygame.Rect((width-30-p_width,height/2 - p_height/2 ),(p_width, p_height ))
pong = pygame.Rect((width/2,height/2), (p_width, p_width))
topWall = pygame.Rect((0,0),(width, 30))
bottomWall = pygame.Rect((0,height - 30),(width, 30)) # coordinates upper left corner, width and height

object_array= [[player1, (0,0,0)],
               [player2, (0,0,0)],
               [pong, (0,0,0)],
               [topWall, (165, 165, 165)],
               [bottomWall, (165, 165, 165)]]

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

    pong_aux.draw_everything(screen, object_array)
    pygame.display.flip()

# Run until the user asks to quit
running = True
# init states - states show if a button is being pressed for a longer time
stateP1 = "none"
stateP2 = "none"

while running:

    # keeping button pressed P1
    if stateP1 == "up":
        pong_aux.move_player(player1, 0, -1, topWall, bottomWall)
    elif stateP1 == "down":
        pong_aux.move_player(player1, 0, 1, topWall, bottomWall)


    # keeping button pressed P2
    if stateP2 == "up":
        pong_aux.move_player(player2, 0, -1, topWall, bottomWall)
    elif stateP2 == "down":
        pong_aux.move_player(player2, 0, 1, topWall, bottomWall)


    # event handling - we wait for event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()

            # build a state machine for each button press
            # player 1 events
            if event.key == pygame.K_w:
                pong_aux.move_player(player1, 0, -1, topWall, bottomWall)
                stateP1 = "up"
            elif event.key == pygame.K_s:
                pong_aux.move_player(player1, 0, 1, topWall, bottomWall)
                stateP1 = "down"


            # player2 events
            if event.key == pygame.K_UP:
                pong_aux.move_player(player2, 0, -1, topWall, bottomWall)
                stateP2 = "up"
            elif event.key == pygame.K_DOWN:
                pong_aux.move_player(player2, 0, -1, topWall, bottomWall)
                stateP2 = "down"

        # pong events
        # todo: implement this

        # reset state
        if event.type == pygame.KEYUP:
            if (event.key == pygame.K_w) or (event.key == pygame.K_s):
                stateP1 = "none"
            elif (event.key == pygame.K_UP) or (event.key == pygame.K_DOWN):
                stateP2 = "none"

    pong_aux.draw_everything(screen, object_array)
    pygame.display.flip()

# Done! Time to quit.
print("i quit.")
pygame.quit()

