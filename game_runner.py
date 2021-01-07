import pygame
import pygame.freetype
from game_objects import (
    Ball
)
from players import (
    Player
)
import game_objects

from physics_engine import PhysicsEngine
# So it can be accessible to the outside
pygame.init()


class ScoreKeeper:
    player1_score = 0
    player2_score = 0
    font = pygame.font.Font('freesansbold.ttf', 32)

    def increment_score_if_someone_scored(self, ball, physics_engine):
        if physics_engine.is_in_player1s_goal(ball):
            self.player1_score += 1

        if physics_engine.is_in_player2s_goal(ball):
            self.player2_score += 1

    def show_score(self, ball, physics_engine):
        self.increment_score_if_someone_scored(ball, physics_engine)
        message = f"Player 1: {self.player1_score} Player 2: {self.player2_score}"
        black = (0, 0, 0)
        white = (255, 255, 255)
        text = self.font.render(message, True, white, black)
        text_rect = text.get_rect()
        text_rect.center = (game_objects.screen_width / 2,
                            0 + game_objects.screen_height * .04)

        game_objects.win.blit(text, text_rect)


def run():
    # Up is down. Down is up.
    # No spaces between functions in a class
    background = (0, 0, 0)
    physics_engine = PhysicsEngine()
    score_keeper = ScoreKeeper()
    ball = Ball()
    player1 = Player()
    player2 = Player()
    player2.set_character_coordinates(game_objects.screen_width - 50,
                                      game_objects.screen_height - 300)
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        game_objects.win.fill(background)

        player1.draw()
        player2.draw()

        player1.movements(pygame.K_w, pygame.K_s)
        player2.movements(pygame.K_UP, pygame.K_DOWN)
        physics_engine.vertical_boundaries(player1)
        physics_engine.vertical_boundaries(player2)
        physics_engine.vertical_boundaries(ball)
        physics_engine.collisions(ball, player1, 1)
        physics_engine.collisions(ball, player2, 2)
        physics_engine.ball_horizontal_boundaries(ball)

        ball.draw()
        ball.movement()

        score_keeper.show_score(ball, physics_engine)

        pygame.display.update()
