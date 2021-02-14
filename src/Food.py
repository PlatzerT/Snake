import random

from src.Position import Position


class Food(Position):
    def __init__(self, y, x):
        super().__init__(y, x)

    def calc_position(self, y_bounds, x_bounds):
        self.y = random.randint(0, y_bounds-1)
        self.x = random.randint(0, x_bounds-1)

    def __str__(self):
        return "Food[" + str(self.y) + ", " + str(self.x) + "]"