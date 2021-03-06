import tkinter as tk
import IntegratedProject.GUI.IPMGUI.FileBar as fb

def donothing():
    x = 0

def MenuBar(root):
    menubar = tk.Menu(root)
    filemenu = tk.Menu(menubar, tearoff=0)
    filemenu.add_command(label="New", command=donothing)
    # filemenu.add_command(label="Open", command=fb.open_file(root))
    # filemenu.add_command(label="Save", command=fb.save_file(root))
    filemenu.add_command(label="Open", command=donothing)
    filemenu.add_command(label="Save", command=donothing)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=root.quit)
    menubar.add_cascade(label="File", menu=filemenu)
    helpmenu = tk.Menu(menubar, tearoff=0)
    helpmenu.add_command(label="Help Index", command=donothing)
    helpmenu.add_command(label="About...", command=donothing)
    menubar.add_cascade(label="Help", menu=helpmenu)
    return menubar