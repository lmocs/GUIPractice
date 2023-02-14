from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Kakashi")

load= Image.open("/Users/loganmoreno/Desktop/Python/Images/kakashi.jpeg")
render = ImageTk.PhotoImage(load)
img = Label(root, image=render)
img.pack()

quit_button = Button(root, text = "Sayonara, Kakashi-Senpai!", command = root.quit)
quit_button.pack()

root.mainloop()

'''
from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Images")

my_img = ImageTk.PhotoImage(Image.open(file = "lolli.jpg"))
my_label = Label(root, text = "Lolli", image = my_img)
my_label.pack()

root.mainloop()
'''