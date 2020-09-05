from agent import Agent
from random import randint


class Village(Agent):
    def __init__(self, world, coords=None):
        super().__init__(world, coords)

    def migrate(self):
        self.turn_left(randint(0, 360))
        self.turn_right(randint(0, 360))
        self.forward()

    def check_water(self):
        while self.cell_here()['ele'] < 0:
            self.turn_left(randint(0, 360))
            self.turn_right(randint(0, 360))
            self.forward()

    def step(self):
        self.migrate()
        self.check_water()