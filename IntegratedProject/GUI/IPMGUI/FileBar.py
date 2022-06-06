import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename


def open_file(window):
    """Open a file for editing."""
    tBox = tk.Text()
    children_widgets = window.winfo_children()
    for child_widget in children_widgets:
        if child_widget.winfo_class() == 'text':
            tBox = child_widget.get()
    txt_edit = tBox
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete("1.0", tk.END)
    with open(filepath, mode="r", encoding="utf-8") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
    window.title(f"Simple Text Editor - {filepath}")

def save_file(window):
    """Save the current file as a new file."""
    txt_edit = window.txt_edit.get("1.0", tk.END)
    filepath = asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, mode="w", encoding="utf-8") as output_file:
        text = txt_edit.get("1.0", tk.END)
        output_file.write(text)
    window.title(f"Simple Text Editor - {filepath}")