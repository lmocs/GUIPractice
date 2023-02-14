from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Popup Practice")

def popup():
    # messagebox. -> showinfo, showwarning, showerror, askquestion, askokcancel, askyesno
    # Returns values:   ok         ok          ok        yes/no        1/0         1/0
    # First parameter is the title, second is text inside popup
    response = messagebox.showinfo("This is my popup!", "Hello World!")
    if response == "ok" or response == "yes" or response == 1:
        Label(root, text = "Cool!").pack()
    else:
        return

click = Button(root, text = "Click Me!", command = popup)
click.pack()

root.mainloop()