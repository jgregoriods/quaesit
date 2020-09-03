from math import hypot, sin, asin, cos, radians, degrees
import inspect


class Agent:
    _id = 0

    def __init__(self, world, coords):
        self._id = Agent._id
        Agent._id += 1

        self.world = world
        self.coords = coords
        self.direction = 90

        self.world.add_agent(self)

    def die(self):
        del self.world.agents[self._id]
        self.world.grid[self.coords]['agents'].remove(self)
        del self

    def hatch(self):
        sig = inspect.signature(self.__init__)
        filter_keys = [param.name for param in sig.parameters.values()
                       if param.kind == param.POSITIONAL_OR_KEYWORD]
        filtered_dict = {filter_key: self.__dict__[filter_key]
                         for filter_key in filter_keys}
        return self.__class__(**filtered_dict)
    
    def move_to(self, coords):
        self.world.remove_from_grid(self)
        self.coords = coords
        self.world.place_on_grid(self)

    def cell_here(self):
        return self.world.grid[self.coords]
    
    def get_distance(self, coords):
        x, y = coords
        return round(hypot((x - self.coords[0]), (y - self.coords[1])))

    def cells_in_radius(self, radius):
        if self.world.torus:
            neighborhood = {self.world.to_torus((x, y)):
                            self.world.grid[self.world.to_torus((x, y))]
                            for x in range(self.coords[0] - radius,
                                        self.coords[0] + radius + 1)
                            for y in range(self.coords[1] - radius,
                                        self.coords[1] + radius + 1)
                            if self.get_distance((x, y)) <= radius}
        else:
            neighborhood = {(x, y): self.world.grid[(x, y)]
                            for x in range(self.coords[0] - radius,
                                        self.coords[0] + radius + 1)
                            for y in range(self.coords[1] - radius,
                                        self.coords[1] + radius + 1)
                            if (self.get_distance((x, y)) <= radius and
                                (x, y) in self.world.grid)}

        return neighborhood
    
    def agents_in_radius(self, radius):
        neighborhood = self.cells_in_radius(radius)
        neighbors = [agent for coords in neighborhood
                     for agent in self.world.grid[coords]['agents']
                     if agent is not self]
        return neighbors

    def agents_here(self):
        return [agent for agent in self.world.grid[self.coords]['agents']
                if agent is not self]

    def turn_right(self, angle=90):
        self.direction = round((self.direction - angle) % 360)
    
    def turn_left(self, angle=90):
        self.direction = round((self.direction + angle) % 360)
    
    def forward(self, n_steps=1):
        x = round(self.coords[0] + cos(radians(self.direction)) * n_steps)
        y = round(self.coords[1] + sin(radians(self.direction)) * n_steps)
    
        if self.world.torus:
            self.move_to(self.world.to_torus((x, y)))
        elif (x, y) in self.world.grid:
            self.move_to((x, y))

    def face_towards(self, coords):
        xdif = coords[0] - self.coords[0]
        ydif = coords[1] - self.coords[1]
        dist = hypot(xdif, ydif)
        angle = degrees(asin(ydif / dist))

        if xdif < 0:
            self.direction = round(180 - angle)
        else:
            self.direction = round((360 + angle) % 360)


class Village(Agent):
    def __init__(self, world, coords, size):
        super().__init__(world, coords)
        self.size = size
