import pygame

def setstate(object, state):
    """changes the state of an object, states are used to tell us if we keep pressing something"""
    object = state


def move_player(rect, x_direction, y_direction, top_wall, bottom_wall):
    """moves a Rect object by 1 unit in the specified direction -
    up if y_direction == -1 , down if y_direction == 1
    left if  x_dir == -1 , right if x_dir == 1
    if needed, a unit modifier can be added easily"""
    if (rect.colliderect(top_wall) == 0) and (y_direction == -1):        # upwards movement possible?
        rect.move_ip(x_direction, y_direction)
    elif (rect.colliderect(bottom_wall) == 0) and (y_direction == 1):    # downwards movement possible?
        rect.move_ip(x_direction, y_direction)


def draw_everything(screen, object_array):
    """the object array contains elements that should be drawn and their colour
    A[i][j] = object, colour describes one element"""
    screen.fill((255, 255, 255))  # Fill the background with white
    for game_object in object_array:
        pygame.draw.rect(screen, game_object[1], game_object[0])


