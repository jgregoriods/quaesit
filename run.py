import tkinter as tk

from gui import GUI
from mysim import MySim

root = tk.Tk()
app = GUI(root, MySim)
root.mainloop()