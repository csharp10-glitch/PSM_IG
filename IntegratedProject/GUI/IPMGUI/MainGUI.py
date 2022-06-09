import tkinter as tk
import tkinter.tix as tix
import MenuBar as mb
import IPPlot as iplt
from idlelib.tooltip import Hovertip
from IntegratedProject.GUI.IPMGUI import utils

def textEntry():
    return txt_edit

root = tk.Tk()
projectScreen = tk.Canvas(root)
root.title("IPM Radio Power Density")
txt_edit = tk.Text(root)

root.rowconfigure([0], minsize=50, weight=1)
root.columnconfigure([0,1], minsize=200, weight=1)

projectScreen.rowconfigure([0,8], minsize=50, weight=1)
projectScreen.columnconfigure([0,1], minsize=50, weight=1)

menubar = mb.MenuBar(root)
thePlot= iplt.IPPlot(root)

thePlot.grid(row=0, column=0)
projectScreen.grid(row=0, column=1)

# button = tk.Button(projectScreen).grid(row=1, column=1)
button = iplt.updateButton(projectScreen,1,1)

lbl = tk.Label(projectScreen, text="Transmitter")
variable = tk.StringVar(projectScreen)
variable.set("tx 1") # default value
w = tk.OptionMenu(projectScreen, variable, "tx 1", "tx 2", "tx 3")
txEntry = tk.Entry(projectScreen)
b1 = tk.Button(projectScreen, text="Broad")

lbl.grid(row=0, column=0)
w.grid(row=0, column=1)
b1.grid(row=1, column=0)
lbl2 = tk.Label(projectScreen, text="Power: ").grid(row=2, column=0)
txEntry.grid(row=2, column = 1)
lbl3 = tk.Label(projectScreen, text="Freq.: ").grid(row=3, column=0)
txEntry3 = tk.Entry(projectScreen).grid(row=3, column=1)
lbl4 = tk.Label(projectScreen, text="Altitude.: ").grid(row=4, column=0)
txEntry4 = tk.Entry(projectScreen).grid(row=4, column=1)
# button.grid(row=1, column=1)



# balloon = Balloon(projectScreen, bg="white", title="Help")
# balloon = tix.Balloon(projectScreen)
# balloon.bind_widget(b1, balloonmsg="Click to Exit")

root.config(menu=menubar)
# root.config(canvas=thePlot)
root.config(button=button)
root.mainloop()