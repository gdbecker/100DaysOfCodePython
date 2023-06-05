# 100 Days of Code: Python
# July 28, 2022
# Flask project: coffee and wifi web app
# Combining days 62 & 66: base site with database access

# Import modules
from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from flask_sqlalchemy import SQLAlchemy
from wtforms import StringField, SubmitField, URLField, SelectField, BooleanField
from wtforms.validators import DataRequired

# Set up Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'harrypotterravenclaw'
Bootstrap(app)

# Dropdown list options for cafe form
COFFEE_RATINGS = ["☕","☕☕","☕☕☕","☕☕☕☕","☕☕☕☕☕"]
WIFI_RATINGS = ["💪","💪💪","💪💪💪","💪💪💪💪","💪💪💪💪💪"]
POWER_RATINGS = ["🔌","🔌🔌","🔌🔌🔌","🔌🔌🔌🔌","🔌🔌🔌🔌🔌"]

# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Function to make a 0 or 1 a Boolean valaue
def make_bool(val: int) -> bool:
    return bool(int(val))

# Cafe TABLE Configuration for db
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    open_time = db.Column(db.String(250), nullable=False)
    closing_time = db.Column(db.String(250), nullable=False)
    coffee_rating = db.Column(db.String(250), nullable=False)
    wifi_rating = db.Column(db.String(250), nullable=False)
    power_rating = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=True)
    can_take_calls = db.Column(db.Boolean, nullable=True)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        dictionary = {}
        for column in self.__table__.columns:
            dictionary[column.name] = getattr(self, column.name)
        return dictionary

# Make the database -> comment out when done
# with app.app_context():
#     db.create_all()

class CafeForm(FlaskForm):
    cafe_name = StringField(label='Cafe Name', validators=[DataRequired()])
    map_url = URLField(label='Map URL', validators=[DataRequired()])
    img_url = URLField(label='Image URL', validators=[DataRequired()])
    location = StringField(label='Location', validators=[DataRequired()])
    open_time = StringField(label='Opening Time', validators=[DataRequired()])
    closing_time = StringField(label='Closing Time', validators=[DataRequired()])
    coffee_rating = SelectField(label='Coffee Rating', validators=[DataRequired()], choices=COFFEE_RATINGS)
    wifi_rating = SelectField(label='WiFi Rating', validators=[DataRequired()], choices=WIFI_RATINGS)
    power_rating = SelectField(label='Power Rating', validators=[DataRequired()], choices=POWER_RATINGS)
    seats = StringField(label='Number of Seats', validators=[DataRequired()])
    has_toilet = BooleanField(label='Has a toilet?')
    can_take_calls = BooleanField(label='Can take calls?')
    coffee_price = StringField(label='Coffee Price', validators=[DataRequired()])
    submit = SubmitField('Submit')

# Flask routes
@app.route("/")
def home():
    return render_template("index.html")

# Show all cafes
@app.route('/cafes')
def cafes():
    all_cafes_db = db.session.query(Cafe).all()
    list_of_rows = [["Cafe Name", "Map URL", "Image URL", "Location", "Open", "Close", "Coffee", "WiFi", "Power", "# Seats", "Has Toilet?", "Can Take Calls?", "Price"]]

    cafes = [cafe.to_dict() for cafe in all_cafes_db]

    for c in cafes:
        row = [c["name"], c["map_url"], c["img_url"], c["location"], c["open_time"], c["closing_time"], c["coffee_rating"], c["wifi_rating"], c["power_rating"], c["seats"], c["has_toilet"], c["can_take_calls"], c["coffee_price"], c["id"]]
        list_of_rows.append(row)

    return render_template("cafes.html", cafes=list_of_rows)

# Add cafe via form
@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        new_cafe = Cafe(
            name=form.cafe_name.data,
            map_url=form.map_url.data,
            img_url=form.img_url.data,
            location=form.location.data,
            open_time=form.open_time.data,
            closing_time=form.closing_time.data,
            coffee_rating=form.coffee_rating.data,
            wifi_rating=form.wifi_rating.data,
            power_rating=form.power_rating.data,
            seats=form.seats.data,
            has_toilet=make_bool(form.has_toilet.data),
            can_take_calls=make_bool(form.can_take_calls.data),
            coffee_price=form.coffee_price.data
        )
        db.session.add(new_cafe)
        db.session.commit()

        return redirect(url_for("cafes"))

    return render_template('add.html', form=form)

# Delete a cafe
@app.route("/delete/<cafe_id>")
def delete_cafe(cafe_id):
    cafe_to_delete = Cafe.query.filter_by(id=int(cafe_id)).first()
    if cafe_to_delete != None:
        db.session.query(Cafe).filter(Cafe.id == cafe_id).delete()
        db.session.commit()
        return redirect(url_for("cafes"))
    else:
        return redirect(url_for("cafes"))

if __name__ == '__main__':
    app.run(debug=True)