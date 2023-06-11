# 100 Days of Code: Python
# May 22-23, 2022
# Password manager app with tkinter

# Import modules
from tkinter import *
from tkinter import messagebox
import pyperclip
import json
import random

# Function to search for a password
def search():
    try:
        website = website_entry.get().title()
        with open("passwords.json", "r") as file:
            data = json.load(file)
        username = data[website]["username"]
        password = data[website]["password"]
        messagebox.showinfo(title="Info", message=f"Email: {username}\nPassword: {password}")

    except FileNotFoundError:
        messagebox.showinfo(title="File Error", message="No passwords file found.")
    except KeyError:
        messagebox.showinfo(title="Website Error", message="No password found for this site.")

# Function to add a password
def save():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    # Setup json data format to save
    new_data = {
        website: {
            "username": username,
            "password": password,
        }
    }

    # Check for empty fields
    fields_empty = website == "" or password == ""
    if fields_empty:
        messagebox.showinfo(title="Error", message="Please don't leave any fields empty!")

    # Confirm details
    is_ok= False
    if not fields_empty:
        is_ok = messagebox.askokcancel(title=f"{website}", message=f"These are the details entered: \nEmail: {username}\nPassword: {password}\nIs it okay to save?")

    if is_ok:
        try:
            with open("passwords.json", "r") as file:
                data = json.load(file)
                data.update(new_data)
        except:
            data = new_data
        finally:
            with open("passwords.json", "w") as file:
                json.dump(data, file, indent=4)

        website_entry.delete(0, END)
        password_entry.delete(0, END)

# Function to make a random password
def generate_password():
    password_entry.delete(0, END)

    # Variable sets
    letters = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    symbols = list("!#$%&\()*+,-./:;<=>?@")
    numbers = list("0123456789")

    # Make password
    password = []
    password.extend([letters[random.randint(0, len(letters) - 1)] for l in range(0,5)])
    password.extend([symbols[random.randint(0, len(symbols) - 1)] for s in range(0, 5)])
    password.extend([numbers[random.randint(0, len(numbers) - 1)] for c in range(0, 5)])
    random.shuffle(password)
    password = ''.join(password)
    password_entry.insert(0, f"{password}")

    # Immediately copy the password for use
    pyperclip.copy(password)

# Function to close the app
def quit():
    window.destroy()

# UI setup
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(125, 100, image=logo_img)
canvas.grid(column=2, row=1)

website_label = Label(text="Website:")
website_label.grid(column=1, row=2)
website_entry = Entry(width=33)
website_entry.grid(column=2, row=2)
website_entry.focus()

username_label = Label(text="Username/email:")
username_label.grid(column=1, row=3)
username_entry = Entry(width=52)
username_entry.grid(column=2, row=3, columnspan=2)
username_entry.insert(0, "example@email.com")

password_label = Label(text="Password")
password_label.grid(column=1, row=4)
password_entry = Entry(width=33)
password_entry.grid(column=2, row=4)

password_button = Button(text="Generate Password", command=generate_password)
password_button.grid(column=3, row=4)

add_button = Button(text="Add", width=44, command=save)
add_button.grid(column=2, row=5, columnspan=2)

search_button = Button(text="Search", width=14, command=search)
search_button.grid(column=3, row=2)

exit_button = Button(text="Exit", width=10, command=quit)
exit_button.grid(column=3, row=0)

# Window controls
window.mainloop()