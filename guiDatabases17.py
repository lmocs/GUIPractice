# Databases
from tkinter import *
import sqlite3

root = Tk()
root.title("Databases")
root.geometry("1920x1080")

# This creates or connects to a database / conn is short for connection
conn = sqlite3.connect("address_book.db")

# Create cursor / c is short for cursor
c = conn.cursor()

# Create table
c.execute('''CREATE TABLE addresses (
        first_name text,
        last_name text,
        address text, 
        city text,
        state text, 
        zipcode integer
        )''')

# Whenever you want to make a change in a database, must commit those changes to the database
conn.commit()

# This is to close the connection
conn.close()

root.mainloop()