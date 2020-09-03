import matplotlib.pyplot as plt
import matplotlib.figure as mplfig
import matplotlib.backends.backend_tkagg as tkagg
import numpy as np
import tkinter as tk


class GUI:
    def __init__(self, master, model):
        self.master = master
        self.model = model
        self.world = self.model()

        self.figure = mplfig.Figure(figsize=(7, 7), dpi=100)
        self.ax = self.figure.add_subplot(111)
        self.ax.tick_params(axis='both', which='both', bottom=False,
                            labelbottom=False, left=False, labelleft=False)
        self.figure.subplots_adjust(left=0, bottom=0.02, right=1, top=0.98,
                                    wspace=0, hspace=0)
        self.canvas = tkagg.FigureCanvasTkAgg(self.figure, self.master)
        self.canvas.get_tk_widget().grid(row=1, column=4, columnspan=1,
                                         rowspan=10)
        
        self.toolbar_frame = tk.Frame(self.master)
        self.toolbar_frame.grid(row=12, column=4, columnspan=1)
        self.toolbar = tkagg.NavigationToolbar2Tk(self.canvas,
                                                  self.toolbar_frame)

        self.setup_button = tk.Button(master, text='Setup', width=10,
                                      command=self.setup)
        self.setup_button.grid(row=1, column=1)
    
    def plot_model(self):
        if self.world.agents:
            points = [self.world.agents[_id].coords for _id in self.world.agents]
            self.ax.cla()
            self.ax.scatter(*zip(*points))
            self.canvas.draw()

    def setup(self):
        self.world = self.model()
        self.plot_model()
