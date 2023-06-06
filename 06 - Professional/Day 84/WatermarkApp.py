# 100 Days of Code: Python
# July 8, 2022
# GUI app that adds a watermark to desired image

# Import modules
import os
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image

# Function to select an image to upload
def upload_image():
    global img
    global filename

    f_types = [('Png Files', '*.png')]
    filename = filedialog.askopenfilename(filetypes=f_types)
    img = ImageTk.PhotoImage(file=filename)
    canvas.itemconfig(image_container, image=img)

# Function to add the watermark
def add_watermark():
    global img_modified
    global filename
    global img_raw

    img_raw = Image.open(filename)
    watermark_raw = Image.open("images/watermark.png")

    w, h = img_raw.size
    watermark_w, watermark_h = watermark_raw.size

    pos = ((w - watermark_w) // 2, (h - watermark_h) // 2)

    img_raw.paste(watermark_raw, pos, mask=watermark_raw)
    img_modified = ImageTk.PhotoImage(img_raw)
    canvas.itemconfig(image_container, image=img_modified)

# Function to save watermarked image
def save():
    global filename
    global img_raw

    file_basename = os.path.basename(filename)
    new_filename = "watermarked-" + file_basename

    img_raw.save(f"images/{new_filename}")
    status_label.config(text="Image saved!")

# Function to reset the app
def restart():
    canvas.itemconfig(image_container, image=watermark_img)
    status_label.config(text="")

# Function to exit the app
def exit():
    window.destroy()

# CONSTANTS & starting variables
BACKGROUND_COLOR = "#6E85B7"
FONT_NAME = "Arial"

# UI setup
window = Tk()
window.title("Watermark App")
window.config(padx=100, pady=100, bg=BACKGROUND_COLOR)

exit_img = PhotoImage(file="images/exit.png")
exit_button = Button(image=exit_img, command=exit)
exit_button.grid(column=1, row=0)

status_label = Label(text="", bg=BACKGROUND_COLOR, fg="white", font=(FONT_NAME, 15, "bold"))
status_label.grid(column=2, row=0)

restart_img = PhotoImage(file="images/restart.png")
restart_button = Button(image=restart_img, command=restart)
restart_button.grid(column=3, row=0)

canvas = Canvas(width=800, height=500, bg=BACKGROUND_COLOR, highlightthickness=0)
watermark_img = PhotoImage(file="images/watermark.png")
image_container = canvas.create_image(400, 250, image=watermark_img)
canvas.grid(column=1, row=1, columnspan=3)

upload_img = PhotoImage(file="images/camera.png")
upload_button = Button(image=upload_img, command=upload_image)
upload_button.grid(column=1, row=2)
upload_label = Label(text=f"Upload", bg=BACKGROUND_COLOR, font=(FONT_NAME, 15, "bold"))
upload_label.grid(column=1, row=3)

convert_img = PhotoImage(file="images/convert.png")
convert_button = Button(image=convert_img, command=add_watermark)
convert_button.grid(column=2, row=2)
convert_label = Label(text=f"Convert", bg=BACKGROUND_COLOR, font=(FONT_NAME, 15, "bold"))
convert_label.grid(column=2, row=3)

save_img = PhotoImage(file="images/save.png")
save_button = Button(image=save_img, command=save)
save_button.grid(column=3, row=2)
save_label = Label(text=f"Save", bg=BACKGROUND_COLOR, font=(FONT_NAME, 15, "bold"))
save_label.grid(column=3, row=3)

# Window controls
window.mainloop()