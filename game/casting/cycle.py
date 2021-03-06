import constants
from game.casting.actor import Actor
from game.shared.point import Point


class Cycle(Actor):
    """
    A long limbless reptile.

    The responsibility of Cycle is to move itself.

    Attributes:
        _points (int): The number of points the food is worth.
    """

    def __init__(self, player):
        super().__init__()
        self._segments = []
        self._player = player
        self._prepare_body(self._player)
        self._is_dead = False

    def get_player(self):
        return self._player

    def get_segments(self):
        return self._segments

    def get_is_dead(self):
        return self._is_dead

    def set_is_dead(self, is_dead):
        self._is_dead = is_dead

    def move_next(self):
        for segment in self._segments:
            segment.move_next()
        for i in range(len(self._segments) - 1, 0, -1):
            trailing = self._segments[i]
            previous = self._segments[i - 1]
            velocity = previous.get_velocity()
            trailing.set_velocity(velocity)

    def get_head(self):
        return self._segments[0]

    def grow_tail(self, number_of_segments):
        for i in range(number_of_segments):
            tail = self._segments[-1]
            velocity = tail.get_velocity()
            offset = velocity.reverse()
            position = tail.get_position().add(offset)

            segment = Actor()

            if self._player == "first":
                segment.set_position(position)
                segment.set_velocity(velocity)
                segment.set_text("#")
                segment.set_color(constants.GREEN)
            else:
                segment.set_position(position)
                segment.set_velocity(velocity)
                segment.set_text("%")
                segment.set_color(constants.RED)

            self._segments.append(segment)

    def turn_head(self, velocity):
        self._segments[0].set_velocity(velocity)

    def _reset_body(self):
        self._is_dead = False
        self._segments.clear()
        self._prepare_body(self._player)
        
    def _clear_cycles(self):
        self._is_dead = False
        self._segments.clear()
        self._prepare_empty(self._player)
        
    def _prepare_empty(self, player):
       
        if player == "first":
            for i in range(constants.CYCLE_LENGTH):
                segment = Actor()
                self._segments.append(segment)
        else:
            for i in range(constants.CYCLE_LENGTH):
                segment = Actor()
                self._segments.append(segment)        

    def _prepare_body(self, player):

        if player == "first":
            x = int(constants.MAX_X / 4)
            y = int(constants.MAX_Y / 2)
            for i in range(constants.CYCLE_LENGTH):
                position = Point(x, y + i * constants.CELL_SIZE)
                velocity = Point(0, -1 * constants.CELL_SIZE)
                text = "*"
                color = constants.RED if i == 0 else constants.GREEN
                segment = Actor()
                segment.set_position(position)
                segment.set_velocity(velocity)
                segment.set_text(text)
                segment.set_color(color)
                self._segments.append(segment)
        else:
            x = int(constants.MAX_X / 4)*3
            y = int(constants.MAX_Y / 2)
            for i in range(constants.CYCLE_LENGTH):
                position = Point(x, y - i * constants.CELL_SIZE)
                velocity = Point(0, 1 * constants.CELL_SIZE)
                text = "@"
                color = constants.GREEN if i == 0 else constants.RED
                segment = Actor()
                segment.set_position(position)
                segment.set_velocity(velocity)
                segment.set_text(text)
                segment.set_color(color)
                self._segments.append(segment)
