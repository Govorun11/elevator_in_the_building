from random import randint
import application

MAX_FLOOR_NUMBER: int = randint(5, 6)
UP: int = 1
DOWN: int = 0

if __name__ == '__main__':
    app = application.Application()
    app.run()
