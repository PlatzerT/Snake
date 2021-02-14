class Position:
    def __init__(self, y, x):
        self.y = y
        self.x = x

    def __eq__(self, o: object) -> bool:
        if isinstance(o, Position):
            if o.x == self.x and o.y == self.y:
                return True
        return False

