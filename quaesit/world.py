import numpy as np
import rasterio as rio

from abc import ABCMeta, abstractmethod
from random import shuffle, randint, choice
from scipy.interpolate import interp2d
from statistics import mean
from tqdm import tqdm
from typing import Dict, Tuple


class World(metaclass=ABCMeta):
    def __init__(self, width: int, height: int, torus: bool = True,
                 tracking: Dict = None):
        self.width = width
        self.height = height
        self.grid = self.init_grid()
        self.torus = torus
        self.agents = {}
        self.tick = 0
        self.display_layer = None
        self.tracking = tracking
        self.globals = {}

        if self.tracking:
            self.track = {agent: {param: [] for param in tracking[agent]}
                          for agent in tracking}

    def init_grid(self) -> Dict:
        grid = {}

        for i in range(self.width):
            for j in range(self.height):
                grid[(i, j)] = {'agents': []}

        return grid

    def add_layer(self, layer_name: str, file: str = None, array=None,
                  value: int = 0, display: bool = False):
        if file is not None:
            with rio.open(file) as layer:
                array = layer.read(1)
                self.interp_to_grid(array, layer_name)

        elif array is not None:
            self.interp_to_grid(array, layer_name)

        else:
            for cell in self.grid:
                self.grid[cell][layer_name] = value

        if display:
            self.display_layer = layer_name

    def interp_to_grid(self, array, layer_name):
        height, width = array.shape
        xrange = lambda x: np.linspace(0, 1, x)
        f = interp2d(xrange(width), xrange(height), array, kind='linear')
        new_arr = f(xrange(self.width), xrange(self.height))

        for i in range(self.width):
            for j in range(self.height):
                self.grid[(i, j)][layer_name] = new_arr[self.height - 1 - j, i]

    def to_torus(self, coords: Tuple) -> Tuple:
        x, y = coords
        return (x % self.width, y % self.height)

    def add_agent(self, agent):
        self.agents[agent._id] = agent
        self.place_on_grid(agent)

    def remove_from_grid(self, agent):
        self.grid[agent.coords]['agents'].remove(agent)

    def place_on_grid(self, agent):
        self.grid[agent.coords]['agents'].append(agent)

    def random_cell(self):
        return (randint(0, self.width - 1), randint(0, self.height - 1))

    def random_empty_cell(self):
        empty_cells = [cell for cell in self.grid if not self.grid[cell]['agents']]
        return choice(empty_cells)

    def run(self, n_ticks: int):
        for i in range(n_ticks):
            self.step()

    def save(self):
        for agent in self.tracking:
            if agent == 'global':
                for param in self.tracking[agent]:
                    self.track['global'][param].append(
                        self.globals[param])

            elif agent[:5] == 'grid_':
                layer = np.reshape([self.grid[(i, j)][agent[5:]]
                                    for j in range(self.height)
                                    for i in range(self.width)],
                                   (self.height, self.width))

                for param in self.tracking[agent]:
                    if param[:6] == 'count_':
                        val = param[6:]
                        if val.isdigit():
                            val = int(val)
                        self.track[agent][param].append(
                            np.count_nonzero(layer == val))

                    elif param == 'avg':
                        self.track[agent][param].append(
                            np.average(layer))

                    elif param == 'sum':
                        self.track[agent][param].append(
                            np.sum(layer))

                    elif param == 'min':
                        self.track[agent][param].append(
                            np.min(layer))

                    elif param == 'max':
                        self.track[agent][param].append(
                            np.max(layer))

            else:
                for param in self.tracking[agent]:
                    if param == 'count':
                        self.track[agent][param].append(
                            len([self.agents[_id] for _id in self.agents
                                if self.agents[_id].breed == agent]))

                    elif param[:4] == 'avg_':
                        self.track[agent][param].append(
                            mean([getattr(self.agents[_id], param[4:])
                                  for _id in self.agents
                                  if self.agents[_id].breed == agent] or [0]))

                    elif param[:4] == 'sum_':
                        self.track[agent][param].append(
                            sum([getattr(self.agents[_id], param[4:])
                                 for _id in self.agents
                                 if self.agents[_id].breed == agent]))

                    elif param[:4] == 'min_':
                        self.track[agent][param].append(
                            min([getattr(self.agents[_id], param[4:])
                                for _id in self.agents
                                if self.agents[_id].breed == agent] or [0]))

                    elif param[:4] == 'max_':
                        self.track[agent][param].append(
                            max([getattr(self.agents[_id], param[4:])
                                for _id in self.agents
                                if self.agents[_id].breed == agent] or [0]))

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

    def iterate(self, n_steps: int):
        for i in tqdm(range(n_steps)):
            self.step()
