import math
from tkinter import *

root = Tk()
root.title("Addition Calculator")

# This creates the Entry field
e = Entry(root, width = 35, borderwidth = 5)

# This places the Entry Field, columnspan stretches to 3 columns, padx/y is the size
e.grid(row = 0, column = 0, columnspan = 3, padx = 10, pady = 10)

# Number Click Event
def num_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def add_click():
    first_num = e.get()
    # This declares a global variable that can be used in all functions
    global f_num
    global math
    math = "addition"
    f_num = int(first_num)
    e.delete(0, END)

def sub_click():
    first_num = e.get()
    # This declares a global variable that can be used in all functions
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_num)
    e.delete(0, END)

def mult_click():
    first_num = e.get()
    # This declares a global variable that can be used in all functions
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_num)
    e.delete(0, END)

def div_click():
    first_num = e.get()
    # This declares a global variable that can be used in all functions
    global f_num
    global math
    math = "division"
    f_num = int(first_num)
    e.delete(0, END)

def equals_click():
    second_num = int(e.get())
    e.delete(0, END)
    if math == "addition":
        e.insert(0, f_num + second_num)
    elif math == "subtraction":
        e.insert(0, f_num - second_num)
    elif math == "multiplication":
        e.insert(0, f_num * second_num)
    elif math == "division":
        e.insert(0, f_num / second_num)

def clear_click():
    e.delete(0, END)


# Create 9 buttons                                    # Lambda allows us to pass parameters
button1 = Button(root, text = "1", padx = 40, pady = 20, command = lambda: num_click(1))
button2 = Button(root, text = "2", padx = 40, pady = 20, command = lambda: num_click(2))
button3 = Button(root, text = "3", padx = 40, pady = 20, command = lambda: num_click(3))
button4 = Button(root, text = "4", padx = 40, pady = 20, command = lambda: num_click(4))
button5 = Button(root, text = "5", padx = 40, pady = 20, command = lambda: num_click(5))
button6 = Button(root, text = "6", padx = 40, pady = 20, command = lambda: num_click(6))
button7 = Button(root, text = "7", padx = 40, pady = 20, command = lambda: num_click(7))
button8 = Button(root, text = "8", padx = 40, pady = 20, command = lambda: num_click(8))
button9 = Button(root, text = "9", padx = 40, pady = 20, command = lambda: num_click(9))
button0 = Button(root, text = "0", padx = 40, pady = 20, command = lambda: num_click(0))

# Create Calculator Buttons
button_add = Button(root, text = "+", padx = 39, pady = 20, command = add_click)
button_subtract = Button(root, text = "-", padx = 40, pady = 20, command = sub_click)
button_multiply = Button(root, text = "*", padx = 42, pady = 20, command = mult_click)
button_divide = Button(root, text = "/", padx = 43, pady = 20, command = div_click)
button_equals = Button(root, text = "=", padx = 104, pady = 20, command = equals_click)
button_clear = Button(root, text = "Clear", padx = 91, pady = 20, command = clear_click)


# This places the buttons on the GUI grid
button1.grid(row = 4, column = 0)
button2.grid(row = 4, column = 1)
button3.grid(row = 4, column = 2)

button4.grid(row = 3, column = 0)
button5.grid(row = 3, column = 1)
button6.grid(row = 3, column = 2)

button7.grid(row = 2, column = 0)
button8.grid(row = 2, column = 1)
button9.grid(row = 2, column = 2)

button0.grid(row = 5, column = 0)
button_clear.grid(row = 5, column = 1, columnspan = 2)

button_add.grid(row = 6, column = 0)
button_equals.grid(row = 6, column = 1, columnspan = 2)

button_subtract.grid(row = 7, column = 0)
button_multiply.grid(row = 7, column = 1)
button_divide.grid(row = 7, column = 2)

# Runs the GUI
root.mainloop()