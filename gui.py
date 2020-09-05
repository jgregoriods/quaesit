import matplotlib.pyplot as plt
import matplotlib.figure as mplfig
import matplotlib.backends.backend_tkagg as tkagg
import numpy as np
import tkinter as tk


class GUI:
    def __init__(self, master, model):
        self.master = master
        self.model = model()
        self.running = True

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

        self.step_button = tk.Button(master, text='Step', width=10,
                                     command=self.step)
        self.step_button.grid(row=2, column=1)

        self.run_button = tk.Button(master, text='Run', width=10,
                                    command=self.run)
        self.run_button.grid(row=3, column=1)

        self.stop_button = tk.Button(master, text='Stop', width=10,
                                     command=self.stop)
        self.stop_button.grid(row=4, column=1)
    
        self.plot_model()

    def plot_model(self):
        self.ax.cla()
        
        base = np.reshape([self.model.grid[(i, j)]['ele']
                           for j in range(self.model.height)
                           for i in range(self.model.width)],
                           (self.model.height, self.model.width))
        
        self.ax.imshow(base)

        if self.model.agents:
            points = [self.model.agents[_id].coords
                      for _id in self.model.agents]
            self.ax.scatter(*zip(*points))
        
        self.canvas.draw()

    def setup(self):
        self.running = True
        self.model = self.model.__class__()
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