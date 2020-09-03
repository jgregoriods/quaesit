from world import World
from village import Village


class MySim(World):
    def __init__(self, width=100, height=100, torus=True):
        super().__init__(width, height, torus)
    
    def setup(self):
        for i in range(25):
            v = Village(self)
    