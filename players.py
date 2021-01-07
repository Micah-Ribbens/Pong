from game_objects import Paddle
from physics_engine import PhysicsEngine
import pygame
import game_objects
from abc import abstractmethod


class Player(Paddle):
    movement = game_objects.screen_height * .0015

    def __init__(self):
        super().__init__()

    def movements(self, move_up_command, move_down_command):
        controlls = pygame.key.get_pressed()
        if controlls[move_up_command] and self.is_below_top:
            self.y_coordinate -= self.movement
        if controlls[move_down_command] and self.is_above_bottom:
            self.y_coordinate += self.movement 

