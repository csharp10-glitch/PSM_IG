import tkinter as tk

class IPTk(tk.Tk):
    def __init__(self):
        self.text = tk.Text(self)
    
    def textEntry(self):
        return self.text

