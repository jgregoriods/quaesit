import tkinter as tk

from gui import GUI
from swm import SWM

root = tk.Tk()
app = GUI(root, SWM)
root.mainloop()