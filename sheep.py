from icons import get_icon
from agent import Agent
from random import randint


class Sheep(Agent):
    def __init__(self, world, coords=None):
        super().__init__(world, coords)
        self.color = 'white'
        self.energy = 10
        self.icon = get_icon('cat')

    def eat_grass(self):
        if self.cell_here()['grass'] == 10:
            self.cell_here()['grass'] = 0
            self.energy += 10

    def move(self):
        self.random_walk()
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