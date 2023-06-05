# 100 Days of Code: Python
# July 13, 2022
# GUI app that deletes text if user hasn't typed for 5 seconds

# Import modules
from tkinter import *

# CONSTANTS & starting variables
BACKGROUND_COLOR = "#E8AA42"
FONT_NAME = "Arial"
TIME_LIMIT = 5
count = TIME_LIMIT
timer = None

# Function for when user is typing
def key_pressed(event):
    global count
    global timer
    count = TIME_LIMIT
    window.after_cancel(timer)
    timer = None

    canvas.itemconfig(timer_text, text="Typing...")
    timer = window.after(1000, start_timer)

# Function for starting the count down
def start_timer():
    global count
    count_down(count)

def count_down(count):
    global timer
    canvas.itemconfig(timer_text, text=f"{count}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    elif count == 0:
        clear_text()

# Function for clearing text from input box
def clear_text():
    input_box.delete(0, END)

# UI setup
window = Tk()
window.title("Disappearing Text")
window.config(padx=40, pady=40, bg=BACKGROUND_COLOR)

canvas = Canvas(width=500, height=300, bg=BACKGROUND_COLOR, highlightthickness=0)
timer_text = canvas.create_text(250, 100, text="", fill="white",font=(FONT_NAME, 20, "bold"))
input_box = Entry(width=40, font=(FONT_NAME, 15))
canvas.create_window(250, 200, window=input_box)
canvas.grid(column=1, row=1, columnspan=3)

window.bind("<Key>", key_pressed)
timer = window.after(1000, start_timer)

# Window controls
window.mainloop()