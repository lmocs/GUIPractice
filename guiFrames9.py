from tkinter import *

root = Tk()
root.title("Frame Practice")

# This is a frame, but without anything in it nothing will run
def display():
    # Size of Frame
    frame = LabelFrame(root, padx = 50, pady = 50)
    # Space outside of frame
    frame.pack(padx = 100, pady = 100)

    # Notice that the button is placed in frame, not root
    button1 = Button(frame, text = "Push", padx = 10, pady = 10)
    button1.grid(row = 0, column = 1)

    # Also, it is possible to pack the frame and grid within the frame
    button2 = Button(frame, text = "Don't push", padx = 10, pady = 10)
    button2.grid(row = 1, column = 1)

display()

root.mainloop()