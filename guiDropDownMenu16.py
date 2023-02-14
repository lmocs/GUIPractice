# Drop Down Box / Options Menu

from tkinter import *

root = Tk()
root.title("Drop Down Menu")
root.geometry("1920x1080")

# This function is for the button on line 22
def select():
    # Don't forget .get() !
    display = Label(root, text = var.get())
    display.pack()

# This is a Python list of the days
options = [
    "Monday", 
    "Tuesday", 
    "Wednesday", 
    "Thursday", 
    "Friday"
]
# First declare a variable for the menu
var = StringVar()
var.set(options[0])

# Next make an OptionMenu
# Format: var_name = OptionMenu(root, var, *list)

# Can be made like this:
# drop = OptionMenu(root, var, "Monday", "Tuesday", "Wednesday", "Thursday", "Friday")

# Changed to a list, but needs a star in front of the list variable !!!
drop = OptionMenu(root, var, *options)
drop.pack()

# This button allows us to see what the value is when selecting an option
confirm = Button(root, text = "Confirm", command = select)
confirm.pack()

root.mainloop()