# Classes with Tkinter

from tkinter import *

root = Tk()
root.title("Classes")
root.geometry("400x400")

class Store:

    def __init__(self, main, name):

        self.name = name

        self.frame = LabelFrame(main)
        self.frame.pack()

        self.button = Button(main, text = "Click me!", command = self.clicked)
        self.button.pack()

    def clicked(self):
        Label(self.frame, text = "You clicked me!").pack()


one = Store(root, "Walmart")
root.mainloop()