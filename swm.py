from world import World
from sheep import Sheep
from wolf import Wolf


class SWM(World):
    def __init__(self, width=50, height=50, torus=True):
        super().__init__(width, height, torus)
    
    def setup(self):
        # Setup patches
        self.add_layer('grass', value=1, display=True)

        # Setup agents
        for i in range(100):
            s = Sheep(self)
        for i in range(20):
            w = Wolf(self)