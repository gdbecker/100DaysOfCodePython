# 100 Days of Code: Python
# May 21, 2022
# Mile to kilometer converter GUI app

# Import modules
from tkinter import *

# Setup GUI window
window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=225, height=100)

# Conversion function
def convert():
    km = round(float(miles_entry.get()) * 1.609)
    result_label.config(text=f"{km}")

result = 0

# Entry
miles_entry = Entry(width=20)
miles_entry.grid(column=1, row=0)

# Labels
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

equal_label = Label(text="is equal to")
equal_label.grid(column=0, row=1)

result_label = Label(text="")
result_label.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

# Button
calculate_button = Button(text="Calculate", command=convert)
calculate_button.grid(column=1, row=2)

# Window controls
window.mainloop()
