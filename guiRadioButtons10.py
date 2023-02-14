from tkinter import *

root = Tk()
root.title("Radio Buttons")


toppings = [
    ("Pepperoni", "Pepperoni"),
    ("Cheese", "Cheese"),
    ("Mushroom", "Mushroom"),
    ("Onion", "Onion"),
]

pizza = StringVar()
#pizza.set("Select a topping: ")

for text, topping in toppings:
    rbutton1 = Radiobutton(root, text = text, variable = pizza, value = topping)
    rbutton1.pack(anchor = W)

def clicked(value):
    label = Label(root, text = value)
    label.pack()

confirm_button = Button(root, text = "Confirm", command = lambda: clicked(pizza.get()))
confirm_button.pack()

#label = Label(root, text = pizza.get())
#label.pack()


"""
r = IntVar()
r.set(0)

rbutton1 = Radiobutton(root, text = "Option 1", variable = r, value = 1, command = lambda: clicked(r.get()))
rbutton1.pack()

rbutton2 = Radiobutton(root, text = "Option 2", variable = r, value = 2, command = lambda: clicked(r.get()))
rbutton2.pack()
"""









"""
# a.set("2") -> sets output to "2"

global frame

def clicked(value):
    label = Label(frame, text = value)
    label.pack()

# This shows how sharing one variable allows for one choice
def side1():
    global frame
    frame = LabelFrame(root, padx = 100, pady = 100)
    frame.grid(row = 0, column = 1, padx = 50, pady = 50)

    # The variable 'a' takes an integer value from clicking the button -> a.get() to get the value of rbutton1
    a = IntVar()
    rbutton1 = Radiobutton(frame, text = "Option 1", variable = a, value = 1, command = lambda: clicked(a.get))
    rbutton1.pack()

    rbutton2 = Radiobutton(frame, text = "Option 2", variable = a, value = 2, command = lambda: clicked(a.get))
    rbutton2.pack()

    label = Label(frame, text = a.get())
    label.pack()

# This shows how having multiple variables allows for multiple choices
def side2():
    frame = LabelFrame(root, padx = 100, pady = 100)
    frame.grid(row = 0, column = 2, padx = 50, pady = 50)

    a = IntVar()
    rbutton1 = Radiobutton(frame, text = "Option 1", variable = a, value = 1)
    rbutton1.pack()

    b = IntVar()
    rbutton2 = Radiobutton(frame, text = "Option 2", variable = b, value = 2)
    rbutton2.pack()


side1()
side2()

"""
root.mainloop()