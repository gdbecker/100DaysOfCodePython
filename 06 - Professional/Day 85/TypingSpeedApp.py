# 100 Days of Code: Python
# July 9, 2022
# GUI app for measuring typing speed

# Import modules
import random
from tkinter import *

# CONSTANTS & starting variables
BACKGROUND_COLOR = "#3F4E4F"
FONT_NAME = "Arial"
prompts = [
    "The quick brown fox jumped over the lazy dog by the river and over the hedge one hundred thousand times",
    "Some say ice cream is only for the summer but I always love it year round especially in winter",
    "Libraries have to be one of the most magical places on earth because of the endless worlds to explore in books",
    "Harry Potter is one of the best book and tv series ever written and made and enjoyed by fans everywhere",
    "Marvel comics are underrated and there are so many characters and storylines that interconnect"
]
running = None
count = 0
timer = None

# Function for selecting a random prompt
def select_prompt():
    start_button.grid_forget()
    submit_button.grid(column=2, row=2)

    p = random.choice(prompts)
    canvas.itemconfig(prompt_text, text=p)
    start_timer()

# Function for running the timer
def start_timer():
    global running
    global count
    global timer

    running = True
    if running:
        timer_text.config(text=f"{count}")
        timer = window.after(1000, start_timer)
        count += 1

# Function for stopping the timer
def stop_timer():
    global running
    global count
    global timer

    running = False
    window.after_cancel(timer)

# Function to submit text to measure typing speed
def submit():
    global count

    stop_timer()

    entered_text = input_box.get()
    words = entered_text.split()
    num_words = len(words)

    minutes = count / 60

    speed = round(num_words / minutes, 2)
    status_label.config(text=f"{speed} words/min")

# Function to restart the app
def restart():
    global count
    count=0
    timer_text.config(text="0")

    stop_timer()

    canvas.itemconfig(prompt_text, text="")
    input_box.delete(0, END)
    start_button.grid(column=2, row=2)
    submit_button.grid_forget()
    status_label.config(text="")

# UI setup
window = Tk()
window.title("Typing Speed App")
window.config(padx=100, pady=100, bg=BACKGROUND_COLOR)

timer_text = Label(text="", bg=BACKGROUND_COLOR, fg="white",font=(FONT_NAME, 20, "bold"))
timer_text.grid(column=2, row=0)

restart_img = PhotoImage(file="images/restart.png")
restart_button = Button(image=restart_img, command=restart)
restart_button.grid(column=3, row=0)

canvas = Canvas(width=500, height=300, bg=BACKGROUND_COLOR, highlightthickness=0)
prompt_text = canvas.create_text(250, 110, text="", fill="white", font=(FONT_NAME, 20, "bold"), width=400, justify="c")
input_box = Entry(width=50, font=(FONT_NAME, 15))
canvas.create_window(250, 200, window=input_box)
canvas.grid(column=1, row=1, columnspan=3)

start_button = Button(text="Start", width=15, height=3, font=(FONT_NAME, 12), highlightthickness=0, command=select_prompt)
start_button.grid(column=2, row=2)

submit_button = Button(text="Submit", width=15, height=3, font=(FONT_NAME, 12), highlightthickness=0, command=submit)
submit_button.grid_forget()

status_label = Label(text="", bg=BACKGROUND_COLOR, fg="white", font=(FONT_NAME, 10, "bold"))
status_label.grid(column=2, row=3)

# Window controls
window.mainloop()