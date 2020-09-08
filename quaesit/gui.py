import inspect
import matplotlib.pyplot as plt
import matplotlib.figure as mplfig
import matplotlib.backends.backend_tkagg as tkagg
import numpy as np
import tkinter as tk

from math import ceil


class GUI:
    def __init__(self, master, model, controls, plots=None, grid_keys=None):
        self.master = master
        self.model = model
        self.breeds = None
        self.running = True
        self.plots = plots or []
        self.plot_axes = []
        self.grid_keys = grid_keys

        nrow = ceil((1 + len(self.plots)) / 3)
        ncol = len(self.plots) + 1 if len(self.plots) < 2 else 3

        self.figure = mplfig.Figure(figsize=(5 * ncol, 5 * nrow),
                                    dpi=(75 // nrow))
        self.ax = self.figure.add_subplot(nrow, ncol, 1)
        self.ax.tick_params(axis='both', which='both', bottom=False,
                            labelbottom=False, left=False, labelleft=False)

        if self.plots:
            i = 2
            for plot in self.plots:
                self.plot_axes.append(self.figure.add_subplot(nrow, ncol, i))
                i += 1

        self.figure.subplots_adjust(left=0.05, bottom=0.05, right=0.95,
                                    top=0.95, wspace=0.1, hspace=0.1)

        self.canvas = tkagg.FigureCanvasTkAgg(self.figure, self.master)
        self.canvas.get_tk_widget().grid(row=2, column=2, columnspan=6 * ncol,
                                         rowspan=10 * nrow)
        
        self.toolbar_frame = tk.Frame(self.master)
        self.toolbar_frame.grid(row=10 * nrow + 2, column=2, columnspan=5)
        self.toolbar = tkagg.NavigationToolbar2Tk(self.canvas,
                                                  self.toolbar_frame)

        self.setup_button = tk.Button(master, text='Setup', width=10,
                                      command=self.setup)
        self.setup_button.grid(row=1, column=2)

        self.step_button = tk.Button(master, text='Step', width=10,
                                     command=self.step)
        self.step_button.grid(row=1, column=3)

        self.run_button = tk.Button(master, text='Run', width=10,
                                    command=self.run)
        self.run_button.grid(row=1, column=4)

        self.stop_button = tk.Button(master, text='Stop', width=10,
                                     command=self.stop)
        self.stop_button.grid(row=1, column=5)

        self.n_steps = tk.Entry(master, width=10)
        self.n_steps.grid(row=1, column=6)

        self.iterate_button = tk.Button(master, text='Iterate', width=10,
                                        command=self.iterate)
        self.iterate_button.grid(row=1, column=7)
          
        self.model_vars = {}

        for control in controls:
            if controls[control]['type'] == 'scale':
                self.model_vars[control] = tk.IntVar()
                label = controls[control]['label']
                min, max = controls[control]['range']

                new_slider = tk.Scale(self.master, label=label,
                                    from_=min, to=max,
                                    orient=tk.HORIZONTAL,
                                    variable=self.model_vars[control])
                new_slider.set(controls[control]['value'])

                new_slider.grid(row=len(self.model_vars) + 1, column=1)
                
            elif controls[control]['type'] == 'check':
                self.model_vars[control] = tk.BooleanVar()
                label = controls[control]['label']

                new_checkbox = tk.Checkbutton(self.master, text=label,
                                              variable=self.model_vars[control])
                new_checkbox.grid(row=len(self.model_vars) + 1, column=1)

    def plot_model(self):
        self.ax.cla()
        self.ax.set_xlim(0, self.model.width - 1)
        self.ax.set_ylim(0, self.model.height - 1)

        if self.model.display_layer:
            base = np.reshape([self.model.grid[(i, j)][self.model.display_layer]
                               for j in range(self.model.height)
                               for i in range(self.model.width)],
                              (self.model.height, self.model.width))
            
            if base.dtype.kind == 'U':
                base = np.vectorize(self.grid_keys.__getitem__)(base)

            self.ax.imshow(base, cmap='cividis')

        if self.model.agents:
            breeds = {self.model.agents[_id].breed
                      for _id in self.model.agents}
            for breed in breeds:

                agents = [self.model.agents[_id] for _id in self.model.agents
                          if self.model.agents[_id].breed == breed]

                points = [agent.coords for agent in agents]
                colors = [agent.color for agent in agents]

                self.ax.scatter(*zip(*points), c=colors, s=100,
                                marker=agents[0].icon)
        
        if self.plot_axes:
            i = 0
            for plot in self.plot_axes:
                plot.cla()
                labels = []
                for agent in self.plots[i]:
                    for param in self.plots[i][agent]:
                        if agent[:5] == 'grid_':
                            plot.plot(self.model.track_layers[agent][param])
                        else:
                            plot.plot(self.model.track_agents[agent][param])
                        labels.append(f'{agent} {param}')
                plot.legend(tuple(labels), loc='upper right')

                i += 1

        self.canvas.draw()

    def setup(self):
        params = {k: v.get() for k, v in self.model_vars.items()}

        tracking = None
        if self.plots:
            tracking = {}
            for plot in self.plots:
                for agent, param in plot.items():
                    tracking.setdefault(agent, [])
                    tracking[agent] += param
        
        self.running = True
        self.stop_button.configure(text='Stop')

        if inspect.isclass(self.model):
            self.model = self.model(tracking=tracking, **params)
        else:
            self.model = self.model.__class__(tracking=tracking, **params)

        self.model.setup()
        self.plot_model()
    
    def step(self):
        self.model.step()
        self.plot_model()
    
    def run(self):
        if self.running:
            self.model.step()
            self.plot_model()
            self.master.after(1, self.run)

    def stop(self):
        if self.running:
            self.running = False
            self.stop_button.configure(text='Resume')
        else:
            self.running = True
            self.stop_button.configure(text='Stop')
            self.run()

    def iterate(self):
        self.model.iterate(int(self.n_steps.get()))
        self.plot_model()
