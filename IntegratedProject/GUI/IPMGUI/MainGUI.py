import tkinter as tk
import MenuBar as mb
import IPPlot as iplt

root = tk.Tk()

menubar = mb.MenuBar(root)
thePlot, button = iplt.IPPlot(root)

root.config(menu=menubar)
# root.config(canvas=thePlot)
root.config(button=button)
root.mainloop()