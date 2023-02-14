from tkinter import *

root = Tk()
root.title("Sliders")
root.geometry("1920x1080")

def slide():
    aspect_ratio = Label(root, text = str(horizontal.get()) + "x" + str(vertical.get()))
    aspect_ratio.pack()
    root.geometry(str(horizontal.get()) + "x" + str(vertical.get()))


# Scale Widget is a Slider, defaults to a vertical slider
horizontal = Scale(root, from_ = 0, to = 1920, orient = HORIZONTAL)
horizontal.pack()

vertical = Scale(root, from_ = 0, to = 1080)
vertical.pack()

confirm = Button(root, text = "Confirm", command = slide)
confirm.pack()


root.mainloop()