from random import shuffle


class World:
    def __init__(self, width, height, torus=True):
        self.width = width
        self.height = height
        self.grid = self.init_grid(width, height)
        self.torus = torus
        self.agents = {}
        self.tick = 0

    def init_grid(self, width, height):
        grid = {}
        
        for i in range(width):
            for j in range(height):
                grid[(i, j)] = {'agents': [],
                                'color': 'white'}
        
        return grid
    
    def add_layer(self, layer):
        pass
    
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

    def step(self):
        agent_ids = list(self.agents.keys())
        shuffle(agent_ids)
        for _id in agent_ids:
            self.agents[_id].step()
        self.tick += 1
