from bdb import effective
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

root = Tk()
root.title("File Dialogue")

def open():
    # Need to make 'img' a global variable!!!
    global img

    # This opens a file dialog                 This sets the initial directory          Can also make this a tuple   First parameter is the title, second is the file type
    root.filename = filedialog.askopenfilename(initialdir = "/Python", title = "Select a file", filetypes = ((".jpeg", "*.jpeg"), ("All Files", "*.*")))

    # This shows file location
    show = Label(root, text = root.filename)
    show.pack()

    # This displays the chosen image
    img = ImageTk.PhotoImage(Image.open(root.filename))
    display = Label(image = img)
    display.pack()

# This is a button that opens the file dialog
button = Button(root, text = "Open File", command = open)
button.pack()

root.mainloop()