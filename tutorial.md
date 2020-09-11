# Tutorial

In this tutorial, loosely based on Netlogo's, we will create a simple model where agents move around, eat, reproduce and die. The model illustrates several of the capabilities included in the package.

## Creating the Agents

The agents in QuAESit inherit from the Agent class. The class has many in-built methods that facilitate common agent procedures in agent-based models. Let's define our class and call it "Turtle" (as a tribute to Netlogo).

```python
  from quaesit import Agent
  
  
  class Turtle(Agent):
    def __init__(self, energy, world, coords=None):
      super().__init__(world=world, coords=coords)
      self.energy = energy
```
We must pass, as arguments, at least a World object (we will define that later) and a tuple of x,y coordinates. When coordinates are not specified, random coordinates are assigned to the agent. Our turtles will also have a property called "energy".

Every agent must have a method called "step", which calls the methods to be executed at each step of the model.

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
  

def 
```
