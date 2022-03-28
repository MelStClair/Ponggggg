import pygame

def iquit():        # bruteforce shut down
    pygame.quit()


def start_screen(screen, object_array, invisible_wall_r, invisible_wall_l):
    print("press SPACE to begin")
    startingScreen = True
    while startingScreen:
        startscreenEvent = pygame.event.wait()
        if startscreenEvent.type == pygame.QUIT:
            iquit()
        if startscreenEvent.type == pygame.KEYDOWN:
            if startscreenEvent.key == pygame.K_SPACE:
                print("starting game, get ready")
                startingScreen = False

        draw_everything(screen, object_array)
        pygame.draw.rect(screen, (0, 0, 255), invisible_wall_r)
        pygame.draw.rect(screen, (0, 0, 255), invisible_wall_l)
        pygame.display.flip()


def setstate(object, state):
    """changes the state of an object, states are used to tell us if we keep pressing something"""
    object = state


def init_everything():
    print("is there some way to put all of the init sdtuff here but still return everything thats necessary?")


def pong_reset(pong, width, height):
    pong.update((width/2, height/2), (pong.width, pong.height))
    print("YOU ARE A FAILURE, RESETTING NOW")
    for i in range(0,1000000):
        continue

def move_player(player_array, x_direction, y_direction, top_wall, bottom_wall):
    """moves a Rect object by 1 unit in the specified direction -
    up if y_direction == -1 , down if y_direction == 1
    left if  x_dir == -1 , right if x_dir == 1
    if needed, a unit modifier can be added easily"""
    if (player_array[0].colliderect(top_wall) == 0) and (y_direction == -1): # upwards movement possible?
        for rect in player_array:
            rect.move_ip(x_direction, y_direction)
    elif (player_array[4].colliderect(bottom_wall) == 0) and (y_direction == 1):    # downwards movement possible?
        for rect in player_array:
            rect.move_ip(x_direction, y_direction)

def move_pong(pong, move_x, move_y, player1, player2, bottom_wall, top_wall, invisible_wall_l, invisible_wall_r):
    # if no collision then move normally
    # idea: add direction based on state of player that sent it
    # if collision then change direction
    for i in range(0,4):
        if (pong.colliderect(player1[i]) == 1) or (pong.colliderect(player2[i]) == 1):
            move_x *= -1
            if i == 0:
                move_y = move_y + 2
            if i == 1:
                move_y = move_y + 1
            if i == 2:
                move_y = 0
            if i == 3:
                move_y = move_y + 1
            if i == 4:
                move_y = move_y + 2
            pong.move_ip(move_x, move_y)

    if (pong.colliderect(bottom_wall) == 1) or (pong.colliderect(top_wall) == 1):
        move_y *= -1

    pong.move_ip(move_x, move_y)

    if pong.colliderect(invisible_wall_l) == 1: # or (pong.colliderect(invisible_wall_l) == 1):
        print("left out ")
        return [move_x, move_y, True]

    if pong.colliderect(invisible_wall_r) == 1: # or (pong.colliderect(invisible_wall_l) == 1):
        print("right out ")
        return [move_x, move_y, True]


    return [move_x, move_y, False]


def draw_everything(screen, object_array):
    """the object array contains elements that should be drawn and their colour
    A[i][j] = object, colour describes one element"""
    screen.fill((255, 255, 255))  # Fill the background with white
    for game_object in object_array:
        pygame.draw.rect(screen, game_object[1], game_object[0])


