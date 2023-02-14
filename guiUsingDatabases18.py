# Databases
from tkinter import *
import sqlite3

root = Tk()
root.title("Databases")
root.geometry("400x400")

# This creates or connects to a database / conn is short for connection
conn = sqlite3.connect("address_book.db")

# Create cursor / c is short for cursor
c = conn.cursor()

'''
# Commented out making a table because we don't want to repeat it

# Create table
c.execute("""CREATE TABLE addresses (
        first_name text,
        last_name text,
        address text, 
        city text,
        state text, 
        zipcode integer
        )""")
'''

# This function is to add records to the database after clicking the submit_button
def submit():
    # Need to redefine 'conn' and 'c' as well as .commit() and .close() into the function

    # This creates or connects to a database / conn is short for connection
    conn = sqlite3.connect("address_book.db")

    # Create cursor / c is short for cursor
    c = conn.cursor()

    # Insert into table                                                     Don't forget this comma
    c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)",
            # This creates a Python dictionary for each of these variables above
            {
                # Don't forget the commas!
                'f_name': f_name.get(),
                'l_name': l_name.get(),
                'address': address.get(),
                'city': city.get(),
                'state': state.get(),
                'zipcode': zipcode.get()
            })

    # Whenever you want to make a change in a database, must commit those changes to the database
    conn.commit()

    # This is to close the connection
    conn.close()

    # This clears the user input from the text boxes after submit_button is clicked
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)


# Create Query Function to show records that have been submitted after submit_button is activated
def query():
    # Need to redefine 'conn' and 'c' as well as .commit() and .close() into the function

    # This creates or connects to a database / conn is short for connection
    conn = sqlite3.connect("address_book.db")

    # Create cursor / c is short for cursor
    c = conn.cursor()

    # Query the database (Lines 78 - 89)
    c.execute("SELECT *, oid FROM addresses")
    records = c.fetchall()
    # print(records) --- This printed the records to the terminal!

    # MUST DEFINE 'print_records' as blank !!!
    print_records = ""
    # This for-loop takes the items (each value in the record list) and spits out them on seperate lines
    # Here in this loop you can do many different things by indexing an element within the list of 'record'
    for record in records:
        print_records += str(record) + "\n"

    query_label = Label(root, text = print_records)
    query_label.grid(row = 8, column = 0, columnspan = 2)


    # Whenever you want to make a change in a database, must commit those changes to the database
    conn.commit()

    # This is to close the connection
    conn.close()




# Create Text Boxes / Entry Fields and their labels
f_name = Entry(root, width = 30)
f_name.grid(row = 0, column = 1, padx = 20)
f_name_label = Label(root, text = "First Name")
f_name_label.grid(row = 0, column = 0)

l_name = Entry(root, width = 30)
l_name.grid(row = 1, column = 1, padx = 20)
l_name_label = Label(root, text = "Last Name")
l_name_label.grid(row = 1, column = 0)

address = Entry(root, width = 30)
address.grid(row = 2, column = 1, padx = 20)
address_label = Label(root, text = "Address")
address_label.grid(row = 2, column = 0)

city = Entry(root, width = 30)
city.grid(row = 3, column = 1, padx = 20)
city_label = Label(root, text = "City")
city_label.grid(row = 3, column = 0)

state = Entry(root, width = 30)
state.grid(row = 4, column = 1, padx = 20)
state_label = Label(root, text = "State")
state_label.grid(row = 4, column = 0)

zipcode = Entry(root, width = 30)
zipcode.grid(row = 5, column = 1, padx = 20)
zipcode_label = Label(root, text = "Zipcode")
zipcode_label.grid(row = 5, column = 0)



# This button submits the user's input into the database
submit_button = Button(root, text = "Submit", command = submit)
submit_button.grid(row = 6, column = 0, columnspan = 2, padx = 10, pady = 10, ipadx = 100) # ipadx stretches!

# Create a Query Button
query_button = Button(root, text = "Show Records", command = query)
query_button.grid(row = 7, column = 0, columnspan = 2, padx = 10, pady = 10, ipadx = 137)

# Whenever you want to make a change in a database, must commit those changes to the database
conn.commit()

# This is to close the connection
conn.close()

root.mainloop()