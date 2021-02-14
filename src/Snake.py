import copy

from src.SnakePart import SnakePart


class Snake:
    def __init__(self, boardHeight, boardWidth):
        self.body = []
        self.boardHeight = boardHeight
        self.boardWidth = boardWidth
        self.body.append(SnakePart(int(boardHeight/2), int(boardWidth/2)))
        self.tail = self.get_head()

    def extend(self):
        self.body.append(self.tail)

    def get_head(self):
        return self.body[0]

    def get_tail(self):
        return self.body[-1]

    def release_tail(self):
        if len(self.body) > 1:
            self.body.pop()

    def move(self, dir):
        # Saves last tail position --> extend it easily
        self.tail = copy.deepcopy(self.get_tail())
        head_copy = copy.deepcopy(self.body[0])
        if len(self.body) > 1:
            last = head_copy
            for i in range(1, len(self.body)):
                current = copy.deepcopy(self.body[i])
                self.body[i] = last
                last = current
        self.body[0].y += dir.value[0]
        self.body[0].x += dir.value[1]

        self.normalize()

    def normalize(self):
        for i in range(len(self.body)):
            self.body[i].y %= self.boardHeight
            self.body[i].x %= self.boardWidth

    def get_body(self):
        return self.body

    def length(self):
        return len(self.body)
