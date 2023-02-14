from tkinter import *

# Root Widget (the box window)
root = Tk()

# Label Widget 
myLabel = Label(root, text = "Hello")

# "Pack" myLabel into Root Widget
myLabel.pack()

# Event Loop to run GUI
root.mainloop()