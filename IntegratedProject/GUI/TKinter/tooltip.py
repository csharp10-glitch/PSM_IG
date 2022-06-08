from tkinter import *
from tkinter.tix import *
root = Tk()
btn1 = Button(root, text="hello")
btn1.grid(row=0, column=0)
balloon = Balloon(root, bg="white", title="Help")
balloon.bind_widget(btn1, balloonmsg="Click to Exit")
root.mainloop()