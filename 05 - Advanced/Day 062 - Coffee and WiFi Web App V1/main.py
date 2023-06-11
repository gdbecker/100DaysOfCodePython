# 100 Days of Code: Python
# June 20, 2022
# Flask project: coffee and wifi web app
# practicing what I've learned

# Import modules
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField, SelectField
from wtforms.validators import DataRequired
import csv

# Set up Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'harrypotterravenclaw'
Bootstrap(app)

# Dropdown list options for cafe form
COFFEE_RATINGS = ["☕","☕☕","☕☕☕","☕☕☕☕","☕☕☕☕☕"]
WIFI_RATINGS = ["💪","💪💪","💪💪💪","💪💪💪💪","💪💪💪💪💪"]
POWER_RATINGS = ["🔌","🔌🔌","🔌🔌🔌","🔌🔌🔌🔌","🔌🔌🔌🔌🔌"]

class CafeForm(FlaskForm):
    cafe_name = StringField(label='Cafe Name', validators=[DataRequired()])
    location_url = URLField(label='Location URL', validators=[DataRequired()])
    open_time = StringField(label='Open Time', validators=[DataRequired()])
    closing_time = StringField(label='Closing Time', validators=[DataRequired()])
    coffee_rating = SelectField(label='Coffee Rating', validators=[DataRequired()], choices=COFFEE_RATINGS)
    wifi_rating = SelectField(label='WiFi Rating', validators=[DataRequired()], choices=WIFI_RATINGS)
    power_rating = SelectField(label='Power Rating', validators=[DataRequired()], choices=POWER_RATINGS)
    submit = SubmitField('Submit')

# Flask routes
@app.route("/")
def home():
    return render_template("index.html")

@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding="utf8") as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template("cafes.html", cafes=list_of_rows)

@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        cafe_name = form.cafe_name.data
        location_url = form.location_url.data
        open_time = form.open_time.data
        closing_time = form.closing_time.data
        coffee_rating = form.coffee_rating.data
        wifi_rating = form.wifi_rating.data
        power_rating = form.power_rating.data
        data_row = [cafe_name,location_url,open_time,closing_time,coffee_rating,wifi_rating,power_rating]

        with open("cafe-data.csv", "a", newline="", encoding='utf-8') as cafe_file:
            write = csv.writer(cafe_file)
            write.writerow(data_row)
        with open("cafe-data.csv", newline="", encoding="utf8") as csv_file:
            csv_data = csv.reader(csv_file, delimiter=",")
            list_of_rows = []
            for row in csv_data:
                list_of_rows.append(row)
        return render_template("cafes.html", cafes=list_of_rows)

    return render_template('add.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
