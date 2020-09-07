from world import World
from sheep import Sheep
from wolf import Wolf


class SWM(World):
    def __init__(self, n_sheep, n_wolves, width=20, height=20, torus=True, tracking=None):
                 #tracking={'sheep': ['count', 'energy'], 'wolf': ['count', 'energy']}):
        super().__init__(width, height, torus)#, tracking)
        self.n_sheep = n_sheep
        self.n_wolves = n_wolves

    def setup(self):
        # Setup patches
        self.add_layer('grass', value=10, display=True)

        # Setup agents
        for i in range(self.n_sheep):
            s = Sheep(self)
        for i in range(self.n_wolves):
            w = Wolf(self)
    
    def regrow_grass(self):
        for cell in self.grid:
            if self.grid[cell]['grass'] < 10:
                self.grid[cell]['grass'] += 1

    def step(self):
        self.regrow_grass()
        super().step()