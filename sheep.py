from agent import Agent
from random import randint


class Sheep(Agent):
    def __init__(self, world, coords=None):
        super().__init__(world, coords)
        self.color = 'white'
        self.energy = 10
        self.breed = 'sheep'

    def eat_grass(self):
        if self.cell_here()['grass']:
            self.cell_here()['grass'] = 0
            self.energy += 10

    def move(self):
        self.turn_left(randint(0, 360))
        self.turn_right(randint(0, 360))
        self.forward()
        self.energy -= 1

    def reproduce(self):
        if self.energy >= 100:
            self.energy //= 2
            self.hatch()

    def check_death(self):
        if self.energy <= 0:
            self.die()

    def step(self):
        self.eat_grass()
        self.move()
        self.reproduce()
        self.check_death()