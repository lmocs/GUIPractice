from tkinter import *

root = Tk()

# Create a function to make a Button Event (Line 21)
def myClick():
    myLabel4 = Label(root, text = "That tickled uwu! ")
    myLabel4.grid(row = 4, column = 0)

# Create Button Widget

myButton1 = Button(root, text = "Click me! ")
myButton2 = Button(root, text = "You can't click me!", state = DISABLED)
myButton3 = Button(root, text = "I'm a bigger button!", padx = 50, pady = 50)

# "Grid" Button Widget in root
myButton1.grid(row = 0, column = 0)
myButton2.grid(row = 1, column = 0)
myButton3.grid(row = 2, column = 0)

# Button w/ Event                      # When calling myClick, no parenthesis
myButton4 = Button(root, text = "uwu", padx = 30, command = myClick)
myButton4.grid(row = 3, column = 0)

# Button w/ Foreground and Background Color              I don't know why bg no work
myButton5 = Button(root, text = "Look, I'm red!", fg = "red", bg = "black")
myButton5.grid(row = 4, column = 0)


root.mainloop()