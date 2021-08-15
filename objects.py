import pygame
import random
import time
import sys

class GameRound:
    """Round handler class"""
    def __init__(self):
        # windows setup
        self.screen_width = 720
        self.screen_height = 460

        # needed colors
        self.red = pygame.Color(255, 57, 57)
        self.green = pygame.Color(39, 174, 29)
        self.black = pygame.Color(0, 0, 0)
        self.white = pygame.Color(255, 255, 255)
        self.brown = pygame.Color(105, 78, 37)

        # set the number of frames per second
        self.fps = pygame.time.Clock()

        # score variable (the amount of food eaten)
        self.score = 0

    @staticmethod
    def chek_errors():
        check_errors = pygame.init()
        if check_errors[1] > 0:
            sys.exit()
        else:
            print('Ok')

    def set_window_properties(self):
        # TODO: Set the surface (the surface of which
        #  everything will be drawn) and set the title of the window
        pass

    def event_handler(self, event):
        # TODO: listen to events from keyboard
        pass

    def refresh_game_screen(self):
        # TODO: refreshing screen and set fps
        pass

    def display_score(self, choice=1):
        # TODO: displaying scores
        pass

    def game_over(self):
        # TODO: Function for displaying Game Over and results
        #  in case of game completion and exiting the game
        pass

class Snake:
    def __init__(self):
        # TODO: choose snake
        #  position and direction of movement.
        pass

    def draw_snake(self):
        # TODO: the snake should be drawn in a separate method
        pass

    def validate_direction_and_change(self):
        # TODO: Change the direction of movement of the snake only if
        #  it isn't directly opposite to the current one
        pass

    def change_head_position(self):
        # TODO: Customize the movement of the snake's head
        pass

    def snake_body_change(self):
        # TODO: The snake should grow after eating food
        pass

    def check_boundaries(self):
        # TODO: The snake shouldn't pass through the wall and itself
        pass


class Food:
    def __init__(self):
        # TODO: initialization of the food
        pass

    def draw_food(self):
        # TODO: draw the food
        pass