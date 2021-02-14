from src.Position import Position


class SnakePart(Position):
    def __init__(self, y, x):
        super().__init__(y, x)

    def __str__(self):
        return "SnakePart[" + str(self.y) + ", " + str(self.x) + "]"
