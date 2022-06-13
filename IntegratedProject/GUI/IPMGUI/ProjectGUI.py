import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
import IntegratedProject.Map.Area as area
from IntegratedProject.GUI.IPMGUI.IPPlot import IPPlot

root =tk.Tk()
projectScreen = tk.Canvas(root)
root.title("IPM Radio Power Density")

def open_file():
    """Open a file for editing."""
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    with open(filepath, mode="r", encoding="utf-8") as input_file:
        myArea = area.swath()
        return myArea
    root.title(f"Area Import - {filepath}")

def projectGUI():
    myArea = open_file()
    plotWidget = IPPlot(myArea)