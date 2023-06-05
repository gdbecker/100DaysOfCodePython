# 100 Days of Code: Python
# August 7, 2022
# Web app for showing top 10 colors in an uploaded image
# Using the theme "Eventually" from https://html5up.net/

# Import modules
from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import SubmitField
from PIL import Image
import webcolors

# Set up Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'harrypotterravenclaw'
Bootstrap(app)

# UploadForm class
class UploadForm(FlaskForm):
    file = FileField(label="", validators=[FileAllowed(['jpg','jpeg','png'])])
    submit = SubmitField('Submit')

# From StackOverflow: get closest color if a color cannot be named
def closest_colour(requested_colour):
    min_colours = {}
    for key, name in webcolors.CSS3_HEX_TO_NAMES.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - requested_colour[0]) ** 2
        gd = (g_c - requested_colour[1]) ** 2
        bd = (b_c - requested_colour[2]) ** 2
        min_colours[(rd + gd + bd)] = name
    return min_colours[min(min_colours.keys())]

# From PythonDex: convert RGB tuple into a hex code string
def rgb_to_hex(rgb):
    return "#%02x%02x%02x" % rgb

# Function for extracting colors from uploaded image
def extract_colors(image):
    colors_list = []
    uploaded_image = Image.open("static/uploads/" + image)
    uploaded_image = uploaded_image.quantize(colors=10, method=2)
    colors_raw = uploaded_image.getpalette()

    iterator = iter(colors_raw)
    for c in iterator:
        top_color = (c, next(iterator), next(iterator))
        try:
            colors_list.append(webcolors.rgb_to_name(top_color) + ": " + rgb_to_hex(top_color).upper())
        except:
            colors_list.append(closest_colour(top_color) + ": " + rgb_to_hex(top_color).upper())
        if len(colors_list) >= 10:
            break
    return colors_list

# Flask routes
@app.route("/", methods=['GET', 'POST'])
def home():
    form = UploadForm()
    if form.validate_on_submit():
        image_filename = form.file.data.filename
        form.file.data.save("static/uploads/" + image_filename)
        return redirect(url_for("results", image_filename=image_filename))
    return render_template("index.html", form=form)

@app.route("/results/<image_filename>", methods=['GET', 'POST'])
def results(image_filename):
    if request.method == "POST":
        return redirect(url_for("home"))
    colors_list = extract_colors(image_filename)
    return render_template("results.html", filename=image_filename, colors=colors_list)

if __name__ == '__main__':
    app.run(debug=True)