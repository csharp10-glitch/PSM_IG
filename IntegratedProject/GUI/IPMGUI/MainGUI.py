import tkinter as tk
import MenuBar as mb
import IPPlot as iplt
from IntegratedProject.GUI.IPMGUI import utils

def textEntry():
    return txt_edit

root = tk.Tk()
projectScreen = tk.Canvas(root)
root.title("IPM Radio Power Density")
txt_edit = tk.Text(root)

root.rowconfigure([0], minsize=50, weight=1)
root.columnconfigure([0,1], minsize=200, weight=1)

projectScreen.rowconfigure([0,1], minsize=50, weight=1)
projectScreen.columnconfigure([0,1], minsize=50, weight=1)

button = iplt.updateButton(projectScreen)
projectScreen.grid(row=0, column=1)
b1 = tk.Button(projectScreen, text="dost").grid(row=1, column=0)
# b1.pack()

menubar = mb.MenuBar(root)
thePlot= iplt.IPPlot(root)

thePlot.grid(row=0, column=0)
# button.grid(row=0, column=1)

root.config(menu=menubar)
# root.config(canvas=thePlot)
root.config(button=button)
root.mainloop()