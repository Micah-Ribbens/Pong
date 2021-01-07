import game_objects


class PhysicsEngine:
    def vertical_boundaries(self, Object):
        if Object.get_y_coordinate() <= 0:
            Object.change_is_below_top(False)
        else:
            Object.change_is_below_top(True)
        if Object.get_y_coordinate() >= (
                game_objects.screen_height - Object.get_height()):
            Object.change_is_above_bottom(False)
        else:
            Object.change_is_above_bottom(True)

    def ball_horizontal_boundaries(self, ball):
        if ball.get_x_coordinate() <= 0:
            ball.reset_ball_position()
            ball.reset_movement_speed()
        if ball.get_x_coordinate() >= game_objects.screen_width:
            ball.reset_ball_position()
            ball.reset_movement_speed()

    def is_in_player1s_goal(self, ball):
        return ball.get_x_coordinate() <= 0

    def is_in_player2s_goal(self, ball):
        return ball.get_x_coordinate() >= game_objects.screen_width

    def collisions(self, ball, paddle, paddleNumber):
        ball_x_coordinate = ball.get_x_coordinate()
        paddle_x_coordinate = paddle.get_x_coordinate()
        ball_y_coordinate = ball.get_y_coordinate()
        within_paddle_width = True
        # Screen goes from 0 to end
        # so paddle2 outside edge is its x_cor + length
        if paddleNumber == 1:
            within_paddle_width = (ball_x_coordinate >= paddle_x_coordinate and
                                   ball_x_coordinate <= paddle_x_coordinate +
                                   paddle.get_length())

        else:
            ball_x_coordinate += paddle.get_length()
            paddle_outside = paddle_x_coordinate + paddle.get_length()
            paddle_inside = paddle_x_coordinate
            within_paddle_width = (ball_x_coordinate <= paddle_outside and
                                   ball_x_coordinate >= paddle_inside)

        paddle_y_coordinate = paddle.get_y_coordinate()
        # The minus 5 and plus 5 makes the paddle have better "edges" bc
        # the hitbox extends a little higher than the actual length
        buffer = paddle.get_height() * .02
        paddle_top = paddle_y_coordinate + paddle.get_height() - buffer
        paddle_bottom = paddle_y_coordinate - buffer

        within_paddle_height = (ball_y_coordinate >= paddle_bottom and
                                ball_y_coordinate <= paddle_top)

        ball_was_hit = within_paddle_width and within_paddle_height

        if ball_was_hit and paddleNumber == 1:
            ball.change_x_coordinate(paddle_x_coordinate + paddle.get_length())
            ball.set_hit_paddle(True)

        if ball_was_hit and paddleNumber == 2:
            ball.change_x_coordinate(paddle_x_coordinate - paddle.get_length())
            ball.set_hit_paddle(True)

        else:
            ball.set_hit_paddle(False)
