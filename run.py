import tkinter as tk

from gui import GUI
from swm import SWM

controls = {
    'n_sheep': {'label': 'Init sheep', 'range': (1, 50)},
    'n_wolves': {'label': 'Init wolves', 'range': (5, 30)}
}

root = tk.Tk()
app = GUI(root, SWM, controls=controls)
root.mainloop()