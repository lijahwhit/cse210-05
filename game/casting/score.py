from game.casting.actor import Actor
from game.shared.point import Point
import constants

class Score(Actor):
    """
    A record of points made or lost. 

    The responsibility of Score is to keep track of the points the player has earned by eating food.
    It contains methods for adding and getting points. Client should use get_text() to get a string 
    representation of the points earned.

    Attributes:
        _points (int): The points earned in the game.
        _player (string): Which player this score belongs to "first" or "second"
    """

    def __init__(self, player):
        super().__init__()
        self._points = 0
        self._player = player
        self.add_points(0)
        self.init_position(self._player)

    def get_player(self):
        return self._player

    def init_position(self, player):
        """Sets score display to corners of screen based on player variable

        Args:
            player (string): Which player this score belongs to
        """
        if self._player == "first":
            self.set_position(
                Point(2 * constants.CELL_SIZE, constants.CELL_SIZE))

        if self._player == "second":
            self.set_position(
                Point(constants.MAX_X - 8 * constants.CELL_SIZE, constants.CELL_SIZE))

    def add_points(self, points):
        """Adds the given points to the score's total points.

        Args:
            points (int): The points to add.
        """
        self._points += points
<<<<<<< HEAD

        if self._player == "first":
            self.set_text(f"Green Score: {self._points}")
        if self._player == "second":
            self.set_text(f"Red Score: {self._points}")
=======
        self.set_text(f"Score: {self._points}")
        
  class Game:
    def __init__(self):
        game.init()
        game.display.set_caption("Codebasics Snake And food")

        self.surface = game.display.set_mode((1000, 800))
        self.actor = Actor(self.surface)
        self.snake.draw()
        self.food = Food(self.surface)
        self.food.draw()

    def reset(self):
        self.actor = Actor(self.surface)
        self.food = food(self.surface)


    def is_collision(self, x1, y1, x2, y2):
        if x1 >= x2 and x1 < x2 + SIZE:
            if y1 >= y2 and y1 < y2 + SIZE:
                return True
        return False


    def play(self):
        self.render_background()
        self.snake.walk()
        self.apple.draw()
        self.display_score()
        game.display.flip()

        # snake eating apple scenario
        for i in range(self.snake.length):
            if self.is_collision(self.snake.x[i], self.snake.y[i], self.apple.x, self.apple.y):
                self.play_sound("ding")
                self.snake.increase_length()
                self.apple.move()

        # snake colliding with itself
        for i in range(3, self.snake.length):
            if self.is_collision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                raise "Collision Occurred"

        # snake colliding with the boundries of the window
        if not (0 <= self.snake.x[0] <= 1000 and 0 <= self.snake.y[0] <= 800):
            raise "Hit the boundry error"

    def display_score(self):
        font = game.font.SysFont('arial',30)
        score = font.render(f"Score: {self.snake.length}",True,(200,200,200))
        self.surface.blit(score,(850,10))

    def show_game_over(self):
        self.render_background()
        font = game.font.SysFont('arial', 30)
        line1 = font.render(f"Game is over! Your score is {self.snake.length}", True, (255, 255, 255))
        self.surface.blit(line1, (200, 300))
        line2 = font.render("To play again press Enter. To exit press Escape!", True, (255, 255, 255))
        self.surface.blit(line2, (200, 350))
        game.display.flip()

    def run(self):
        running = True
        pause = False

        while running:
            for event in game.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

                    if event.key == K_RETURN:
                        pause = False

                    if not pause:
                        if event.key == K_LEFT:
                            self.snake.move_left()

                        if event.key == K_RIGHT:
                            self.snake.move_right()

                        if event.key == K_UP:
                            self.snake.move_up()

                        if event.key == K_DOWN:
                            self.snake.move_down()

                elif event.type == QUIT:
                    running = False
            try:

                if not pause:
                    self.play()

            except Exception as e:
                self.show_game_over()
                pause = True
                self.reset()

            time.sleep(.1)

if __name__ == '__main__':
    game = Game()
    game.run()
>>>>>>> 86fd0133b02d86c91c2f56a4cdf30919a49e5ba2
