# Tutorial

In this tutorial, loosely based on Netlogo's, we will create a simple model where agents move around, eat, reproduce and die. The model illustrates several of the capabilities included in the package.

## Creating the Agents

The agents in QuAESit inherit from the Agent class. The class has many in-built methods that facilitate common agent procedures in agent-based models. Let's define our class and call it "Turtle" (as a tribute to Netlogo).

```python
  from quaesit import Agent
  
  class Turtle(Agent):
    def __init__(self, world, coords=None):
      super().__init__(world=world, coords=coords)
```
