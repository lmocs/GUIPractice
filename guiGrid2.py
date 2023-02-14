from tkinter import *

# Root Widget (the box window)
root = Tk()

# Label Widget 
myLabel1 = Label(root, text = "Party Time!")
myLabel2 = Label(root, text = "Swag!")

# "Grid" myLabel into Root Widget
# Grid is relative to other rows and columns
myLabel1.grid(row = 0, column = 0)
myLabel2.grid(row = 1, column = 0)

# Event Loop to run GUI
root.mainloop()

