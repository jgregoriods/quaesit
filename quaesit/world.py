import numpy as np
import rasterio as rio

from abc import ABCMeta, abstractmethod
from random import shuffle
from scipy.interpolate import interp2d
from statistics import mean


class World(metaclass=ABCMeta):
    def __init__(self, width, height, torus=True, tracking=None):
        self.width = width
        self.height = height
        self.grid = self.init_grid(width, height)
        self.torus = torus
        self.agents = {}
        self.tick = 0
        self.display_layer = None
        self.tracking = tracking

        if self.tracking:
            self.track = {agent: {param: [] for param in tracking[agent]}
                          for agent in tracking}

    def init_grid(self, width, height):
        grid = {}
        
        for i in range(width):
            for j in range(height):
                grid[(i, j)] = {'agents': []}
        
        return grid
    
    def add_layer(self, layer_name, file=None, value=0, display=False):
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
            for cell in self.grid:
                    self.grid[cell][layer_name] = value
        
        if display:
            self.display_layer = layer_name

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

    def save(self):
        for agent in self.tracking:
            for param in self.tracking[agent]:
                if param == 'count':
                    self.track[agent][param].append(
                        len([self.agents[_id] for _id in self.agents
                             if self.agents[_id].breed == agent]))
                elif param[:4] == 'avg_':
                    self.track[agent][param].append(
                        mean([getattr(self.agents[_id], param[4:])
                              for _id in self.agents
                              if self.agents[_id].breed == agent]))
                elif param[:4] == 'sum_':
                    self.track[agent][param].append(
                        sum([getattr(self.agents[_id], param[4:])
                             for _id in self.agents
                             if self.agents[_id].breed == agent]))

    @abstractmethod
    def setup(self):
        raise NotImplementedError

    def step(self):
        agent_ids = list(self.agents.keys())
        shuffle(agent_ids)
        for _id in agent_ids:
            if _id in self.agents:
                self.agents[_id].step()
        if self.tracking:
            self.save()
        self.tick += 1