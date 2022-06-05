import random
import tkinter as tk

def roll():
    lbl_result["text"] = str(random.randint(1, 6))

window = tk.Tk()
window.columnconfigure(0, minsize=150)
window.rowconfigure([0, 1], minsize=50)

btn_roll = tk.Button(text="Roll", command=roll)
lbl_result = tk.Label()

btn_roll.grid(row=0, column=0, sticky="nsew")
lbl_result.grid(row=1, column=0)

window.mainloop()



# window = tk.Tk()
#
# def increase():
#     value = int(lbl_value["text"])
#     lbl_value["text"] = f"{value + 1}"
#
# def decrease():
#     value = int(lbl_value["text"])
#     lbl_value["text"] = f"{value - 1}"
#
# window.rowconfigure(0, minsize=50, weight=1)
# window.columnconfigure([0, 1, 2], minsize=50, weight=1)
#
# btn_decrease = tk.Button(master=window, text="-", command=decrease)
# btn_decrease.grid(row=0, column=0, sticky="nsew")
#
# lbl_value = tk.Label(master=window, text="0")
# lbl_value.grid(row=0, column=1)
#
# btn_increase = tk.Button(master=window, text="+", command=increase)
# btn_increase.grid(row=0, column=2, sticky="nsew")
#
# window.mainloop()




# # Create an event handler
# def handle_keypress(event):
#     """Print the character associated to the key pressed"""
#     print(event.char)
#
# def handle_click(event):
#     print("The button was clicked!")
#
# button = tk.Button(text="Click me!")
# button.bind("<Button-1>", handle_click)
#
# # Create a window object
# name = "Hello, Tkinter"
# greeting = tk.Label(text = name)
# greeting.pack()
# button.pack()
# window.bind("<Key>", handle_keypress)
#
# # Run the event loop
# window.mainloop()


# border_effects = {
#     "flat": tk.FLAT,
#     "sunken": tk.SUNKEN,
#     "raised": tk.RAISED,
#     "groove": tk.GROOVE,
#     "ridge": tk.RIDGE,
# }
#
# window = tk.Tk()
#
# for relief_name, relief in border_effects.items():
#     frame = tk.Frame(master=window, relief=relief, borderwidth=5)
#     frame.pack(side=tk.LEFT)
#     label = tk.Label(master=frame, text=relief_name)
#     label.pack()
#
# window.mainloop()

# window = tk.Tk()
# name = "Hello, Tkinter"
# greeting = tk.Label(text = name)
# greeting.pack()
#
# button = tk.Button(
#     text="Click me!",
#     width=25,
#     height=5,
#     bg="blue",
#     fg="yellow",
# )
# button.pack()
#
# entry = tk.Entry(fg="yellow", bg="blue", width=50)
# entry.pack()
#
# name = entry.get()
#
# window.mainloop()

