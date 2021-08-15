import pygame
import random
import time
import sys

class GameRound:
    """Round handler class"""
    def __init__(self):
        # TODO: gamescreen initial method
        #  screen size, colors, frames controller,
        #  scores
        pass

    def chek_errors(self):
        # TODO: error handling for pygame initialization
        pass

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