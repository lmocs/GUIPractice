from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Bulldog Viewer App")

dogo0 = ImageTk.PhotoImage(Image.open("/Users/loganmoreno/Desktop/Python/Images/Bulldog0.jpeg"))

dogo1 = ImageTk.PhotoImage(Image.open("/Users/loganmoreno/Desktop/Python/Images/Bulldog1.jpeg"))

dogo2 = ImageTk.PhotoImage(Image.open("/Users/loganmoreno/Desktop/Python/Images/Bulldog2.jpeg"))

img_list = [dogo0, dogo1, dogo2]

# Button Functions
def back(image_number):
    global my_label
    global forward_button
    global rewind_button

    my_label.grid_forget()

    my_label = Label(root, image = img_list[image_number - 1])

    forward_button = Button(root, text = "Next", padx = 20, pady = 20, command = lambda: next(image_number + 1))
    rewind_button = Button(root, text = "Back", padx = 20, pady = 20, command = lambda: back(image_number - 1))

    # This If-Statement disbles the "Next" button when images run out
    if image_number == 1:
        rewind_button = Button(root, text = "Back", padx = 20, pady = 20, state = DISABLED)

    # Status Label Updater           bd = border  relief = makes label sunken  anchor = E (leans label to the right)
    status = Label(root, text = "Image " + str(image_number) + " of " + str(len(img_list)), bd = 1, relief = SUNKEN)
    # sticky stretches the label from west to east 
    status.grid(row = 3, column = 1, sticky = W+E)

    forward_button.grid(row = 1, column = 2)
    rewind_button.grid(row = 1, column = 0)
    my_label.grid(row = 0, column = 0, columnspan = 3)

def quit():
    root.quit()

def next(image_number):
    global my_label
    global forward_button
    global rewind_button

    my_label.grid_forget()

    my_label = Label(root, image = img_list[image_number - 1])

    forward_button = Button(root, text = "Next", padx = 20, pady = 20, command = lambda: next(image_number + 1))
    rewind_button = Button(root, text = "Back", padx = 20, pady = 20, command = lambda: back(image_number - 1))

    # This If-Statement disbles the "Next" button when images run out
    if image_number == len(img_list):
        forward_button = Button(root, text = "Next", padx = 20, pady = 20, state = DISABLED)

    # Status Label Updater           bd = border  relief = makes label sunken  anchor = E (leans label to the right)
    status = Label(root, text = "Image " + str(image_number) + " of " + str(len(img_list)), bd = 1, relief = SUNKEN)
    # sticky stretches the label from west to east 
    status.grid(row = 3, column = 1, sticky = W+E)

    forward_button.grid(row = 1, column = 2)
    rewind_button.grid(row = 1, column = 0)
    my_label.grid(row = 0, column = 0, columnspan = 3)



# Initial Image
my_label = Label(root, image = dogo0)
my_label.grid(row = 0, column = 0, columnspan = 3)

# Status Label
status = Label(root, text = "Image 1 of " + str(len(img_list)), bd = 1, relief = SUNKEN) 
status.grid(row = 3, column = 1, sticky = W+E)

# Backwards, Exit, and Forward Buttons
rewind_button = Button(root, text = "Back", padx = 20, pady = 20, command = back, state = DISABLED)
quit_button = Button(root, text = "Exit", padx = 20, pady = 20, command = quit)
forward_button = Button(root, text = "Next", padx = 20, pady = 20, command = lambda: next(2))

rewind_button.grid(row = 1, column = 0)
quit_button.grid(row = 1, column = 1)
forward_button.grid(row = 1, column = 2)





root.mainloop()