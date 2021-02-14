import time

from src.Direction import Direction
from src.Food import Food
from src.Snake import Snake
from pynput.keyboard import Listener, Key
import os


# Clears the terminal console
def clear():
    # Windows
    if os.name == 'nt':
        _ = os.system("cls")
    # Linux
    else:
        _ = os.system("clear")


class SnakeGame:

    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.board = [[' '] * width for _ in range(height)]
        self.snake = Snake(height, width)
        self.Dir = Direction.IDLE
        self.food = Food(8, 20)
        self.speed = 0.3
        listener = Listener(on_press=self.on_press)
        listener.start()

    def run(self):
        clear()
        while not self.has_crashed():
            self.snake.move(self.Dir)
            self.update_board(self.snake.get_body())
            self.print()

            # Check if food is hit
            if self.hits_food():
                self.snake.extend()
                self.set_food()

            time.sleep(self.speed)
            clear()
        print("The Snake crashed...")


    def has_crashed(self) -> bool:
        if self.snake.length() != 1:
            body = self.snake.get_body()
            for i in range(1, len(self.snake.get_body())):
                if body[i] == self.snake.get_head():
                    return True
        return False

    def hits_food(self) -> bool:
        head = self.snake.get_head()
        # Possible because it compares the attributes
        if head == self.food:
            return True
        return False

    def set_food(self):
        interfering = True
        while interfering:
            interfering = False
            self.food.calc_position(self.height, self.width)
            for part in self.snake.get_body():
                if part == self.food:
                    interfering = True

        self.board[self.food.y][self.food.x] = 'x'

    def update_board(self, snake):
        self.reset()
        self.board[self.food.y][self.food.x] = 'x'
        self.board[snake[0].y % self.height][snake[0].x % self.width] = '●'
        for i in range(1, len(snake)):
            self.board[snake[i].y % self.height][snake[i].x % self.width] = '■'

    def on_press(self, key):

        if (key == Key.up) and self.Dir != Direction.DOWN:
            self.Dir = Direction.UP

        if (key == Key.down) and self.Dir != Direction.UP:
            self.Dir = Direction.DOWN

        if (key == Key.left) and self.Dir != Direction.RIGHT:
            self.Dir = Direction.LEFT

        if (key == Key.right) and self.Dir != Direction.LEFT:
            self.Dir = Direction.RIGHT

        print("key pressed: ", key)

    def print(self):
        for i in range(self.width + 2):
            print("#", end="")
        print("")
        for i in range(len(self.board)):
            print("#", end="")
            for j in range(len(self.board[i])):
                print(self.board[i][j], end="")
            print("#")
        for i in range(self.width + 2):
            print("#", end="")
        print("")

    def reset(self):
        #self.board = [[' '] * self.width for _ in range(self.height)]
        tail = self.snake.tail
        self.board[tail.y][tail.x] = ' '