import inspect
import matplotlib.pyplot as plt
import matplotlib.figure as mplfig
import matplotlib.backends.backend_tkagg as tkagg
import numpy as np
import tkinter as tk


class GUI:
    def __init__(self, master, model, controls, plots=None):
        self.master = master
        self.model = model
        self.running = True
        self.plots = plots or []
        self.plot_axes = []

        ncol = 1 + len(self.plots)

        self.figure = mplfig.Figure(figsize=(5 * ncol, 5), dpi=150)
        self.ax = self.figure.add_subplot(1, ncol, 1)
        self.ax.tick_params(axis='both', which='both', bottom=False,
                            labelbottom=False, left=False, labelleft=False)

        if self.plots:
            i = 2
            for plot in self.plots:
                self.plot_axes.append(self.figure.add_subplot(1, ncol, i))
                i += 1

        self.figure.subplots_adjust(left=0, bottom=0.02, right=1, top=0.98,
                                    wspace=0.1, hspace=0)

        self.canvas = tkagg.FigureCanvasTkAgg(self.figure, self.master)
        self.canvas.get_tk_widget().grid(row=2, column=2, columnspan=4,
                                         rowspan=10)
        
        self.toolbar_frame = tk.Frame(self.master)
        self.toolbar_frame.grid(row=12, column=2, columnspan=5)
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
          
        self.model_vars = {}

        for control in controls:
            self.model_vars[control] = tk.IntVar()
            label = controls[control]['label']
            min, max = controls[control]['range']

            new_slider = tk.Scale(self.master, label=label,
                                  from_=min, to=max,
                                  orient=tk.HORIZONTAL,
                                  variable=self.model_vars[control])

            new_slider.grid(row=len(self.model_vars) + 1, column=1)

    def plot_model(self):
        self.ax.cla()

        if self.model.display_layer:
            base = np.reshape([self.model.grid[(i, j)][self.model.display_layer]
                              for j in range(self.model.height)
                              for i in range(self.model.width)],
                              (self.model.height, self.model.width))
            
            self.ax.imshow(base)

        if self.model.agents:
            points = [self.model.agents[_id].coords
                      for _id in self.model.agents]
            colors = [self.model.agents[_id].color
                      for _id in self.model.agents]
            self.ax.scatter(*zip(*points), c=colors)
        
        if self.plot_axes:
            i = 0
            for plot in self.plot_axes:
                plot.cla()
                for param in self.plots[i]:
                    plot.plot(self.model.track[param])
                i += 1

        self.canvas.draw()

    def setup(self):
        params = {k: v.get() for k, v in self.model_vars.items()}
        self.running = True
        self.stop_button.configure(text='Stop')

        if inspect.isclass(self.model):
            self.model = self.model(**params)
        else:
            self.model = self.model.__class__(**params)

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
