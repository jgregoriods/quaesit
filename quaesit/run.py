import tkinter as tk

from gui import GUI
from swm import SWM

controls = {
    'n_sheep': {'label': 'Init sheep', 'range': (1, 100)},
    'n_wolves': {'label': 'Init wolves', 'range': (5, 100)},
    'regrowth_time': {'label': 'Grass time', 'range': (10, 50)}
}

plots = [{'sheep': ['count'], 'wolf': ['count']},
         {'sheep': ['energy'], 'wolf': ['energy']}]

root = tk.Tk()
app = GUI(root, SWM, controls=controls, plots=plots)
root.mainloop()
