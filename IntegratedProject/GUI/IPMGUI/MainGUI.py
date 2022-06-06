import tkinter as tk
import MenuBar as mb
import IPPlot as iplt
from IntegratedProject.GUI.IPMGUI import utils

def textEntry():
    return txt_edit

root = tk.Tk()
root.title("IPM Radio Power Density")
txt_edit = tk.Text(root)

menubar = mb.MenuBar(root)
thePlot, button = iplt.IPPlot(root)

# thePlot.grid(row=0, column=0)
# button.grid(row=0, column=1)

root.config(menu=menubar)
# root.config(canvas=thePlot)
root.config(button=button)
root.mainloop()