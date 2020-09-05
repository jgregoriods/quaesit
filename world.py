import numpy as np
import rasterio as rio

from abc import ABCMeta, abstractmethod
from random import shuffle
from scipy.interpolate import interp2d


class World(metaclass=ABCMeta):
    def __init__(self, width, height, torus=True):
        self.width = width
        self.height = height
        self.grid = self.init_grid(width, height)
        self.torus = torus
        self.agents = {}
        self.tick = 0

        self.setup()

    def init_grid(self, width, height):
        grid = {}
        
        for i in range(width):
            for j in range(height):
                grid[(i, j)] = {'agents': []}
        
        return grid
    
    def add_layer(self, layer_name, file=None, value=0):
        if file is not None:
            with rio.open(file) as layer:
                l_arr = layer.read(1)

            height, width = l_arr.shape
            xrange = lambda x: np.linspace(0, 1, x)
            f = interp2d(xrange(width), xrange(height), l_arr, kind='linear')
            new_arr = f(xrange(self.width), xrange(self.height))

            for i in range(self.width):
                for j in range(self.height):
                    self.grid[(i, j)][layer_name] = new_arr[j, i]

        else:
            for i in range(self.width):
                for j in range(self.height):
                    self.grid[(i, j)][layer_name] = value

    def to_torus(self, coords):
        x, y = coords
        return (x % self.width, y % self.height)

    def add_agent(self, agent):
        self.agents[agent._id] = agent
        self.place_on_grid(agent)

    def remove_from_grid(self, agent):
        self.grid[agent.coords]['agents'].remove(agent)
    
    def place_on_grid(self, agent):
        self.grid[agent.coords]['agents'].append(agent)

    def run(self, n_ticks):
        for i in range(n_ticks):
            self.step()

    @abstractmethod
    def setup(self):
        raise NotImplementedError

    def step(self):
        agent_ids = list(self.agents.keys())
        shuffle(agent_ids)
        for _id in agent_ids:
            self.agents[_id].step()
        self.tick += 1
