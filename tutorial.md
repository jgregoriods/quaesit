# Tutorial

In this tutorial, loosely based on Netlogo's, we will create a simple model where agents move around, eat, reproduce and die. The model illustrates several of the capabilities included in the package.

## Creating the Agents

The agents in QuAESit inherit from the Agent class. The class has many in-built methods that facilitate common agent procedures in agent-based models. Let's define our class and call it Turtle (as a tribute to Netlogo).

```python
  from quaesit import Agent
  
  
  class Turtle(Agent):
    def __init__(self, energy, world, coords=None):
      super().__init__(world, coords)
      self.energy = energy
```
We must pass, as arguments, at least a World object (we will define that later) and a tuple of x,y coordinates. When coordinates are not specified, random coordinates are assigned to the agent. Our turtles will also have a property called <code>energy</code>.
Every agent is also given a unique id, a random color and a dot icon for display in the GUI. You can override those attributes, e.g. specifying a different <code>self.color</code> and <code>self.icon</code> following matplotlib conventions. Another property that an agent has by default is <code>breed</code> (the same terminology of Netlogo). It is automatically generated (in lowercase) from the class name.

Every agent must have a method called <code>step()</code>, which calls the methods to be executed at each step of the model.

```python
  def step(self):
    self.move()
    self.eat()
    self.reproduce()
    self.check_death()
```
In our case, let's make the agents move randomly, eat food (if there is any available), check if they have enough energy to reproduce and, in case they are out of energy, die. Let's now define each of those methods:

```python
  def move(self):
    self.random_walk()
    self.energy -= 1

  def eat(self):
    pass

  def reproduce(self):
    if self.energy > 50:
      self.energy //= 2
      self.hatch()

  def check_death(self):
    if self.energy <= 0:
      self.die()
```
We will go back to the <code>eat()</code> method later, after understanding how the grid system works.
The code above should be self-explanatory. The Agent class has in-built methods for moving and turning. They are <code>turn_right()</code>, <code>turn_left()</code> and <code>forward()</code>. The <code>random_walk()</code> method combines them, making the agent move a step in a random direction. Our turtles also loose one unit of energy every time they move.
For reproducing, the turtle first checks whether it has surplus energy. If so, an agent is created and initialized with the same parameters as the "parent". The Agent method <code>hatch()</code> does just that.
When the turtles are out of energy, they die by calling the Agent <code>die()</code> method, which deletes the object and references to it in the model.

## Creating the World

Now, let's design the environment in which the turtles live. The model inherits from the World class, where the spatial grid and rules of the model are defined.

```python
from quaesit import World
from random import randint

from agents.turtle import Turtle


class Tutorial(World):
  def __init__(self, population, width=50, height=50, tracking=None):
    super().__init__(width, height, tracking)
    self.population = population
```
In the code above, we initialize the grid with 50x50 cells. The parameter tracking will be better explained later. Essentially, it specifies which properties of the agents or the grid will be saved at each step. The model's world, by default, is toroidal - it wraps vertically and horizontally. If you wish otherwise, you can specify <code>torus=False</code>. We are giving the world an extra property: the initial population of turtles to be created.
Notice that we import the Turtle module from a subfolder. Although you can organize your files in the manner you find most convenient, here I suggest the following structure:
```
tutorial
├── agents
│   └── turtle.py
├── world
│   └── tutorial.py
└── app.py
```
Every world must have a <code>setup()</code> method, which calls all actions to be performed before the model starts to run. In our case, we will create a number of turtles equal to <code>self.population</code> and initialize a layer in the grid with food for the agents.
```python
  def setup(self):
    for i in range(self.population):
      new_turtle = Turtle(world=self, energy=randint(1, 10))
      
    self.add_layer('food', value=1, display=True)
```
When each Turtle object is created, we are passing it <code>self</code>, i.e., the World object as one of the arguments (see above). We also give each turtle a random energy value to start with - between 1 and 10.
Every world is initialized with a grid whose dimensions are defined by the width and height arguments. The grid is structured as a dictionary where tuples of x,y coordinates are the keys and the values are, on their turn, dictionaries with each layer name as a key. Minimally, the grid is initialized with a layer called "agents" where the agent objects occupying each cell are stored in a list. If we inspected a given cell at this stage, we would see something like <code>{(0, 0): {'agents: []}}</code>. The method <code>add_layer()</code> facilitates adding extra layers to the model. In our case, we specify the layer's name as "food" and initialize every cell with a value of 1. If <code>display=True</code>, this is the layer that will be drawn in the GUI when we visualize the model.
Besides uniform values, the <code>add_layer()</code> method also accepts raster files and numpy arrays to initialize a layer. They must be specified the arguments <code>file</code> and <code>object</code>, respectively. If the file or array provided does not fit the number of cells specified in the model's width and height, they will be resampled.
Now that we understand how the grid works, we can go back to the turtle's <code>eat()</code> method.
```python
  def eat(self):
    if self.cell_here('food'):
      self.energy += 10
      self.world.grid[self.coords]['food'] = 0
```
