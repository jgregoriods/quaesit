from agent import Agent
from random import randint


class Wolf(Agent):
    def __init__(self, world, coords=None):
        super().__init__(world, coords)
        self.color = 'black'
        self.energy = 10
        self.breed = 'wolf'

    def eat_sheep(self):
        sheep_here = [agent for agent in self.agents_here()
                      if agent.breed == 'sheep']
        if sheep_here:
            sheep_here[0].die()
            self.energy += 100

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
        self.eat_sheep()
        self.move()
        self.reproduce()
        self.check_death()