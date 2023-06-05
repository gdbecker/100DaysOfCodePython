# 100 Days of Code: Python
# June 21-22, 2022
# Learning to make my own RESTful API
# API documentation is in Postman

# Import modules
from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from random import choice

# Set up Flask app
app = Flask(__name__)

# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Function to make a 0 or 1 a Boolean valaue
def make_bool(val: int) -> bool:
    return bool(int(val))

# Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        # Method 1.
        dictionary = {}
        # Loop through each column in the data record
        for column in self.__table__.columns:
            # Create a new dictionary entry;
            # where the key is the name of the column
            # and the value is the value of the column
            dictionary[column.name] = getattr(self, column.name)
        return dictionary

        # Method 2. Altenatively use Dictionary Comprehension to do the same thing.
        # return {column.name: getattr(self, column.name) for column in self.__table__.columns}

# Flask routes
@app.route("/")
def home():
    return render_template("index.html")
    
# GET: random cafe
@app.route("/random", methods=["GET"])
def random():
    all_cafes_db = db.session.query(Cafe).all()
    random_cafe = choice(all_cafes_db)
    return jsonify(
        id=random_cafe.id,
        name=random_cafe.name,
        map_url=random_cafe.map_url,
        img_url=random_cafe.img_url,
        location=random_cafe.location,
        seats=random_cafe.seats,
        has_toilet=random_cafe.has_toilet,
        has_wifi=random_cafe.has_wifi,
        has_sockets=random_cafe.has_sockets,
        can_take_calls=random_cafe.can_take_calls,
        coffee_price=random_cafe.coffee_price,
    )

# GET: all cafes
@app.route("/all", methods=["GET"])
def all():
    all_cafes_db = db.session.query(Cafe).all()
    return jsonify(cafes=[cafe.to_dict() for cafe in all_cafes_db])

# GET: search for a cafe
@app.route("/search", methods=["GET"])
def search():
    loc = request.args.get("loc")
    print(loc)
    cafe_lookup = Cafe.query.filter_by(location=loc).all()
    print(cafe_lookup)
    if len(cafe_lookup) > 0:
        return jsonify(cafe=[cafe.to_dict() for cafe in cafe_lookup])
    else:
        return jsonify(error={"Not Found":"Sorry! We don't have a cafe at that location."})

# POST: add a new cafe
@app.route("/add", methods=["POST"])
def add():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("location"),
        seats=request.form.get("seats"),
        has_toilet=make_bool(request.form.get("has_toilet")),
        has_wifi=make_bool(request.form.get("has_wifi")),
        has_sockets=make_bool(request.form.get("has_sockets")),
        can_take_calls=make_bool(request.form.get("can_take_calls")),
        coffee_price=request.form.get("coffee_price")
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"Success": "Successfully added the new cafe."})

# PATCH: change a cafe's coffee price
@app.route("/update-price/<cafe_id>", methods=["PATCH"])
def change_price(cafe_id):
    cafe_to_update = Cafe.query.filter_by(id=int(cafe_id)).first()
    cafe_to_update.coffee_price = request.args.get("new_price")
    db.session.commit()
    if cafe_to_update != None:
        return jsonify(response={"Success": "Successfully updated the price."})
    else:
        return jsonify(error={"Not Found":"Sorry! That cafe was not found in our database."})

# DELETE: delete a cafe
@app.route("/report-closed/<cafe_id>", methods=["DELETE"])
def delete(cafe_id):
    if request.args.get("api-key") == "TopSecretAPIKey":
        cafe_to_delete = Cafe.query.filter_by(id=int(cafe_id)).first()
        if cafe_to_delete != None:
            db.session.query(Cafe).filter(Cafe.id == cafe_id).delete()
            db.session.commit()
            return jsonify(response={"Success": "Successfully deleted the cafe."})
        else:
            return jsonify(error={"Not Found": "Sorry! That cafe was not found in our database."})
    else:
        return jsonify({"Error": "Sorry, that's not allowed. Make sure you have the correct api-key."})

if __name__ == '__main__':
    app.run(debug=True)
