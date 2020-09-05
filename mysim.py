from world import World
from village import Village


class MySim(World):
    def __init__(self, width=25, height=15, torus=True):
        super().__init__(width, height, torus)
    
    def setup(self):
        for i in range(25):
            v = Village(self)
