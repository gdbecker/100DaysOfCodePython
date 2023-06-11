# 100 Days of Code: Python
# May 23-24, 2022
# Flashcard app with tkinter

# Import modules
from tkinter import *
import pandas
import csv
import random

# Function for starting the count down
def start_timer():
    count_down(5)

# Fuction for timer countdown
def count_down(count):
    global timer
    timer_text.config(text=f"{count}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    elif count == 0:
        flip_to_english()

# Function to get language name
def get_language():
    if is_english:
        return "English"
    elif not is_english:
        return "French"

# Function to flip to English card side
def flip_to_english():
    global language
    global is_english
    global index
    is_english = True
    language = get_language()
    random_word = words_to_learn[index]
    english_word = random_word[1]
    canvas.itemconfig(image_container, image=card_back_img)
    canvas.itemconfig(language_text, text=language)
    canvas.itemconfig(word_text, text=f"{english_word}")

# Function to go randomly get next foreign language card and start the countdown
def next_card():
    global words_to_learn
    global language
    global is_english
    global index
    is_english = False
    language = get_language()
    random_word = random.choice(words_to_learn)
    index = words_to_learn.index(random_word)
    foreign_word = random_word[0]

    canvas.itemconfig(image_container, image=card_front_img)
    canvas.itemconfig(language_text, text=language)
    canvas.itemconfig(word_text, text=f"{foreign_word}")

    start_timer()

# Function for adding word to "wrong" list
def wrong_button():
    global words_to_learn
    global FILE_HEADERS

    with open("words_to_learn.csv", "w", newline="", encoding='utf-8') as wrong_file:
        write = csv.writer(wrong_file)
        write.writerow(FILE_HEADERS)
        write.writerows(words_to_learn)

    next_card()

# Function for adding word to "correct" list
def right_button():
    global num_right
    global words_right
    global index
    global words_to_learn
    global num_cards_left
    global FILE_HEADERS
    num_right += 1
    random_word = words_to_learn[index]
    words_right.append(random_word)
    words_to_learn.remove(random_word)
    num_cards_left = len(words_to_learn) - 1

    with open("mastered_words.csv", "w", newline="", encoding='utf-8') as correct_file:
        write = csv.writer(correct_file)
        write.writerow(FILE_HEADERS)
        write.writerows(words_right)

    num_right_label.config(text=f"{num_right}")
    num_wrong_label.config(text=f"{num_cards_left}")
    next_card()

# Get words to learn list
words_to_learn = []
try:
    data = pandas.read_csv("words_to_learn.csv")
except:
    data = pandas.read_csv("data/french_words.csv")
finally:
    words = data.to_dict()
    number_of_words = len(words["English"])
    for n in range(number_of_words):
        words_to_learn.append([words["French"][n],words["English"][n]])

# Get correct words
words_right = []
num_right = len(words_right)
try:
    data = pandas.read_csv("mastered_words.csv")
    words = data.to_dict()
    num_right = len(words["English"])
    for n in range(number_of_words):
        words_right.append([words["French"][n], words["English"][n]])
except:
    pass

# CONSTANTS & starting variables
BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Arial"
FILE_HEADERS = ["French", "English"]
timer = None
index = 0
is_english = False
language = ""
num_cards_left = len(words_to_learn) - 1

# UI setup
window = Tk()
window.title("Flashcards")
window.config(padx=40, pady=40, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
image_container = canvas.create_image(400, 263, image=card_front_img)
language_text = canvas.create_text(400, 150, text="Language", fill="black", font=(FONT_NAME, 40, "italic"))
word_text = canvas.create_text(400, 263, text="Word", fill="black", font=(FONT_NAME, 60, "bold"))
canvas.grid(column=1, row=1, columnspan=2)

timer_text = Label(text="5", bg=BACKGROUND_COLOR, font=(FONT_NAME, 30, "bold"))
timer_text.grid(column=3, row=1)

wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img, command=wrong_button)
wrong_button.grid(column=1, row=2)
num_wrong_label = Label(text=f"{num_cards_left}", bg=BACKGROUND_COLOR, font=(FONT_NAME, 15, "bold"))
num_wrong_label.grid(column=1, row=3)

right_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_img, command=right_button)
right_button.grid(column=2, row=2)
num_right_label = Label(text=f"{num_right}", bg=BACKGROUND_COLOR, font=(FONT_NAME, 15, "bold"))
num_right_label.grid(column=2, row=3)

# Kick off the app
next_card()

# Window controls
window.mainloop()