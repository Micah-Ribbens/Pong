import pygame
# So it is accessible to the outside
screen_width = 800
screen_height = 500
name_of_game = "Pong 2.0"
win = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption(f'{name_of_game}')


class Paddle:
    character_color = (250, 0, 0)
    x_coordinate = 20
    y_coordinate = 50
    length = screen_width * .03
    height = screen_height * .3
    is_below_top = True
    is_above_bottom = True

    def draw(self):
        pygame.draw.rect(win, (self.character_color), (self.x_coordinate,
                         self.y_coordinate, self.length, self.height))

    def get_height(self):
        return self.height

    def get_x_coordinate(self):
        return self.x_coordinate

    def get_y_coordinate(self):
        return self.y_coordinate

    def get_length(self):
        return self.length

    def set_character_coordinates(self, x_coordinate, y_coordinate):
        self.y_coordinate = y_coordinate
        self.x_coordinate = x_coordinate

    def change_is_below_top(self, true_or_false):
        self.is_below_top = true_or_false

    def change_is_above_bottom(self, true_or_false):
        self.is_above_bottom = true_or_false


class Ball:
    color = (0, 0, 250)
    x_coordinate = screen_width * .5
    y_coordinate = screen_height * .5
    length = screen_height * .05
    height = screen_height * .05
    is_below_top = True
    is_above_bottom = True
    base_speed = screen_width * .0004
    movement_speed = base_speed
    moving_up = False
    moving_down = True
    moving_right = False
    moving_left = True
    has_hit_paddle = False
    # -1 is up 1 is down
    direction = 1

    def draw(self):
        pygame.draw.rect(win, (self.color), (self.x_coordinate,
                         self.y_coordinate, self.length, self.height))

    def get_height(self):
        return self.height

    def get_length(self):
        return self.length

    def get_x_coordinate(self):
        return self.x_coordinate

    def get_y_coordinate(self):
        return self.y_coordinate

    def change_x_coordinate(self, x_coordinate):
        self.x_coordinate = x_coordinate

    def change_y_coordinate(self, y_coordinate):
        self.y_coordinate = y_coordinate

    def change_is_below_top(self, true_or_false):
        self.is_below_top = true_or_false

    def change_is_above_bottom(self, true_or_false):
        self.is_above_bottom = true_or_false

    def movement(self):
        if not self.is_above_bottom:
            self.moving_up = True
            self.moving_down = False
            self.increase_movement_speed()
        if not self.is_below_top:
            self.moving_up = False
            self.moving_down = True
            self.increase_movement_speed()
        if self.moving_up:
            self.y_coordinate -= self.movement_speed
        if self.moving_down:
            self.y_coordinate += self.movement_speed
        if self.moving_right:
            self.x_coordinate += self.movement_speed
        if self.moving_left:
            self.x_coordinate -= self.movement_speed

    def increase_movement_speed(self):
        if not self.movement_speed >= 3:
            self.movement_speed *= 1.03

    def set_hit_paddle(self, true_or_false):
        self.has_hit_paddle = true_or_false
        # Changes left to right
        if true_or_false:
            self.moving_right = not self.moving_right
            self.moving_left = not self.moving_left

    def reset_movement_speed(self):
        self.movement_speed = self.base_speed

    def reset_ball_position(self):
        self.x_coordinate = screen_width * .5
        self.y_coordinate = screen_height * .5
