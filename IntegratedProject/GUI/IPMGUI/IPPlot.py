import numpy as np
import tkinter as tk
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

t = np.arange(0.0,3.0,0.01)
fig = plt.figure(1)

def IPPlot(root):
    plt.ion()
    s = np.sin(np.pi*t)
    plt.plot(t,s)
    canvas = FigureCanvasTkAgg(fig, master=root)
    plot_widget = canvas.get_tk_widget()
    plot_widget.grid(row=0, column=0)
    updateButton = tk.Button(root, text="Update", command=update).grid(row=1, column=0)
    return plot_widget, updateButton

def update():
    s = np.cos(np.pi*t)
    plt.plot(t,s)
    fig.canvas.draw()


