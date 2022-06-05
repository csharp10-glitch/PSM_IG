import tkinter as tk
import MenuBar as mb
import IPPlot as iplt

root = tk.Tk()

menubar = mb.MenuBar(root)

root.config(menu=menubar)
root.mainloop()