from math import hypot, sin, cos, radians


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
        return Agent(self.world, self.coords)
    
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
