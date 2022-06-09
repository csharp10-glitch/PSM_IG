import numpy as np
import tkinter as tk
import matplotlib
# matplotlib.use('TkAgg')
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
    return plot_widget

def IPPlot(root, area, scatter, row=0, column=0):
    plt.imshow(area)
    plt.scatter(scatter[0], scatter[1], 1, scatter[2], alpha=0.0)
    # plt.show()
    canvas = FigureCanvasTkAgg(fig, master=root)
    plot_widget = canvas.get_tk_widget()
    plot_widget.grid(row=row, column=column)
    return plot_widget

def updateButton(root, row=0, column=0):
    updateButton = tk.Button(root, text="Update", name = "update", command=update).grid(row=row, column=column)
    return updateButton

def update():
    s = np.cos(np.pi*t)
    plt.plot(t,s)
    fig.canvas.draw()


