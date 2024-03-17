# Project Miles to KM Converter
from tkinter import *

def Miles_to_KM():
    miles = new_entry.get()
    km = int(miles)*1.6
    value.config(text=km)


window = Tk()
window.minsize(width=200, height=200)
window.title("Mile to Km Converter")
window.config(padx=100, pady=100)

# First Row
new_entry = Entry(width=18)
new_entry.grid(column=1, row=0)
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

# Second Row
isequal_label = Label(text="is equal to")
isequal_label.grid(column=0, row=1)
value = Label(text="0")
value.grid(column=1, row=1)
unit = Label(text="Km")
unit.grid(column=2, row=1)

# Third Row
button = Button(text="Calculate", command=Miles_to_KM)
button.grid(column=1, row=2)


window.mainloop()