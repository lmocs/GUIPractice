from tkinter import *
from PIL import Image, ImageTk
# from tkinter import messagebox

root = Tk()
root.title("Window 1")

def second_window():
    # 'img' variable needs to be global because if not it won't appear on second window
    # Sometimes it needs to be a local variable to work as well
    global img

    # This declares the second window
    top = Toplevel()
    top.title("Window 2")

    # This packs the image into top
    img = ImageTk.PhotoImage(Image.open("/Users/loganmoreno/Desktop/Python/Images/kakashi.jpeg"))
    Label(top, image = img).pack()

    # Close Button in second window
    close_button = Button(top, text = "Bye Kakashi", command = top.destroy)
    close_button.pack()

# This button opens the second window
open = Button(root, text = "See Kakashi", command = second_window)
open.pack()

# Can also do top.mainloop() to prevent image resetting!
root.mainloop()