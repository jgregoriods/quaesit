Help on module agent:

NAME
    agent

CLASSES
    builtins.object
        Agent
    
    class Agent(builtins.object)
     |  Agent(world, coords: Tuple = None)
     |  
     |  Class to represent an agent in an agent-based model.
     |  
     |  Methods defined here:
     |  
     |  __init__(self, world, coords: Tuple = None)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  agents_here(self) -> List
     |      Returns all agents located on the same cell as oneself.
     |  
     |  agents_in_radius(self, radius: int)
     |      Returns all agents within a distance of oneself.
     |  
     |  cell_here(self, layer=None)
     |      Returns the value of a layer in the model's grid for the cell
     |      where the agent is. If no layer is specified, the values of all
     |      layers are returned.
     |  
     |  cells_in_radius(self, radius: int) -> Dict
     |      Returns all cells and respective attributes within a distance
     |      of the agent.
     |  
     |  die(self)
     |      Remove the agent from the world.
     |  
     |  empty_cells_in_radius(self, radius: int) -> Dict
     |      Returns all empty cells (with no agents on them) and respective
     |      attributes within a distance of the agent.
     |  
     |  face_towards(self, coords: Tuple)
     |      Turns the agent's direction towards a given pair of coordinates.
     |  
     |  forward(self, n_steps: int = 1)
     |      Moves the agent a number of cells forward in the direction it
     |      is currently facing.
     |  
     |  get_distance(self, coords: Tuple) -> int
     |      Returns the distance (in cells) from the agent to a pair of
     |      coordinates.
     |  
     |  hatch(self)
     |      Creates an agent and initializes it with the same parameters as
     |      oneself.
     |  
     |  move_to(self, coords: Tuple)
     |      Places the agent in a different cell of the world grid.
     |  
     |  nearest_agent(self, agents: List = None)
     |      Given a list of agents, returns the agent that is nearest to
     |      oneself. If no list is provided, all agents are evaluated.
     |  
     |  nearest_cell(self, cells: Union[List, Dict]) -> Tuple
     |      Given a list or dictionary of cells, returns the coordinates of
     |      the cell that is nearest to the agent.
     |  
     |  random_walk(self, n_steps: int = 1)
     |      Moves the agent one cell forward in a random direction for a
     |      number of times.
     |  
     |  step(self)
     |      Methods to be performed by the agent at each step of the
     |      simulation.
     |  
     |  turn_left(self, angle: int = 90)
     |      Rotates the agent's direction a number of degrees to the left.
     |  
     |  turn_right(self, angle: int = 90)
     |      Rotates the agent's direction a number of degrees to the right.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  __abstractmethods__ = frozenset({'step'})
     |  
     |  colors = ['blue', 'brown', 'cyan', 'gray', 'green', 'magenta', 'orange...

FUNCTIONS
    asin(x, /)
        Return the arc sine (measured in radians) of x.
    
    cos(x, /)
        Return the cosine of x (measured in radians).
    
    degrees(x, /)
        Convert angle x from radians to degrees.
    
    hypot(x, y, /)
        Return the Euclidean distance, sqrt(x*x + y*y).
    
    radians(x, /)
        Convert angle x from degrees to radians.
    
    sin(x, /)
        Return the sine of x (measured in radians).

DATA
    Dict = typing.Dict
    List = typing.List
    Tuple = typing.Tuple
    Union = typing.Union

FILE
    /Users/jonasgregorio/quaesit/quaesit/agent.py


