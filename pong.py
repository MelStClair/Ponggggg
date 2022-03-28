import pygame
import pong_aux

pygame.init()

def iquit():        # bruteforce shut down
    pygame.quit()


print("welcome to pong: player1 uses W,S Player 2 uses arrows")
print("use space to start a game")

# Set up the drawing window
size = width, height = 700, 500
screen = pygame.display.set_mode(size)
players = p_width, p_height = 30, (height - 100)/4

# create rect objects aka the player avatars and the ball
# todo fix pong spawn
player1_1 = pygame.Rect((30, height/2 - p_height/2),(p_width,p_height/5))
player1_2 = pygame.Rect((30, height/2 - p_height/2 + p_height/5),(p_width,p_height/5))
player1_3 = pygame.Rect((30, height/2 - p_height/2 + (p_height/5)*2),(p_width,p_height/5))
player1_4 = pygame.Rect((30, height/2 - p_height/2 + (p_height/5)*3),(p_width,p_height/5))
player1_5 = pygame.Rect((30, height/2 - p_height/2 + (p_height/5)*4),(p_width,p_height/5))
player2_1 = pygame.Rect((width-30-p_width, height/2 - p_height/2),(p_width, p_height/5 ))
player2_2 = pygame.Rect((width-30-p_width, height/2 - p_height/2 + p_height/5 ),(p_width, p_height/5 ))
player2_3 = pygame.Rect((width-30-p_width,height/2 - p_height/2  + (p_height/5)*2),(p_width, p_height/5 ))
player2_4 = pygame.Rect((width-30-p_width,height/2 - p_height/2 + (p_height/5)*3 ),(p_width, p_height/5 ))
player2_5 = pygame.Rect((width-30-p_width,height/2 - p_height/2 + (p_height/5)*4 ),(p_width, p_height/5 ))
pong = pygame.Rect((width/2,height/2), (p_width, p_width))
topWall = pygame.Rect((0,0),(width, 30))
bottomWall = pygame.Rect((0,height - 30),(width, 30)) # coordinates upper left corner, width and height
invisible_wall_l = pygame.Rect((0,0), (20, height))
invisible_wall_r = pygame.Rect((width-20,0), (20, height))


object_array= [[player1_1, (0,0,0)],
                [player1_2, (0,0,0)],
                [player1_3, (0,0,0)],
                [player1_4, (0,0,0)],
                [player1_5, (0,0,0)],
                [player2_1, (0,0,0)],
                [player2_2, (0,0,0)],
                [player2_3, (0,0,0)],
                [player2_4, (0,0,0)],
                [player2_5, (0,0,0)],
                [pong, (0,0,0)],
                [topWall, (165, 165, 165)],
                [bottomWall, (165, 165, 165)]]
player1 = [player1_1, player1_2, player1_3, player1_4, player1_5]
player2 = [player2_1, player2_2, player2_3, player2_4, player2_5]

# starting screen
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
    pygame.draw.rect(screen, (0,0,255), invisible_wall_r)
    pygame.draw.rect(screen, (0,0,255), invisible_wall_l)
    pygame.display.flip()

# Run until the user asks to quit
running = True
# init states - states show if a button is being pressed for a longer time
stateP1 = "none"
stateP2 = "none"
pong_movement= move_x, move_y = 1,0
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

        # reset state
        if event.type == pygame.KEYUP:
            if (event.key == pygame.K_w) or (event.key == pygame.K_s):
                stateP1 = "none"
            elif (event.key == pygame.K_UP) or (event.key == pygame.K_DOWN):
                stateP2 = "none"

    # move pong, update movement vector
    update_v = pong_aux.move_pong(pong, move_x, move_y, player1, player2, bottomWall, topWall, invisible_wall_l,invisible_wall_r)
    move_x = update_v[0]
    move_y = update_v[1]
    if update_v[2] == True:
        pong_aux.pong_reset(pong, width, height)

    # update canvas
    pong_aux.draw_everything(screen, object_array)
    pygame.display.flip()


# Done! Time to quit.
print("i quit.")
pygame.quit()

