from tkinter import *

root = Tk()

# This creates the entry box in the GUI
e = Entry(root, width = 25, borderwidth = 5, fg = "black", bg = "white")
e.pack()

# This puts text within the Entry
e.insert(0, "Enter your name here: ")

# This function is the click event that displays text after pressing a button
# e.get() "gets" data
def click():
    display_name = "Your name is " + e.get() + "!"
    lab1 = Label(root, text = display_name)
    lab1.pack()

button1 = Button(root, text = "Click to submit", command = click)
button1.pack()


root.mainloop()