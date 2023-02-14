from tkinter import *

root = Tk()
root.title("Checkboxes")
root.geometry("1920x1080")

def first():
    var = IntVar()

    c = Checkbutton(root, text = "Check me!", variable = var).pack()

    # Need to make a button that runs this function to update the value every time
    def mark():
        display = Label(root, text = var.get()).pack()

    confirm = Button(root, text = "Confirm", command = mark).pack()

def second():
    var = StringVar()

    # Need to include onvalue and offvalue now because 'var' is no longer an integer value
    c = Checkbutton(root, text = "Check me!", variable = var, onvalue = "On", offvalue = "Off")
    # This deselects the button when it is first run
    c.deselect()
    c.pack()

    def mark():
        display = Label(root, text = var.get()).pack()

    confirm = Button(root, text = "Confirm", command = mark).pack()

# first()
second()
root.mainloop()