# 100 Days of Code: Python
# June 22, 2022
# Learning Flask authentication

# Import modules
from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

# Set up Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'harrypotterravenclaw'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Set up login manager
login_manager = LoginManager()
login_manager.init_app(app)

# Configure User table in database
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

# Make the database -> comment out when done
# db.create_all()

# Required: call-back function to get a user by id
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Flask routes
@app.route('/')
def home():
    return render_template("index.html")

@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    elif request.method == "POST":
        user = User.query.filter_by(email=request.form.get("email")).first()
        if user != None:
            flash("You've already signed up with that email. Login instead!")
            return redirect(url_for("login"))
        else:
            new_user = User(
                email=request.form.get("email"),
                password=generate_password_hash(request.form.get("password"), method="pbkdf2:sha256", salt_length=8),
                name=request.form.get("name")
            )
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
            return redirect(url_for("secrets"))

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        user = User.query.filter_by(email=request.form.get("email")).first()

        if user == None:
            flash("That email does not exist! Please try again.")
            return redirect(url_for("login"))
        elif check_password_hash(user.password, request.form.get("password")):
            login_user(user)
            return redirect(url_for("secrets"))

@app.route('/secrets')
@login_required
def secrets():
    print(current_user.name)
    return render_template("secrets.html", name=current_user.name)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/download', methods=["GET"])
@login_required
def download():
    return send_from_directory(directory=app.static_folder, path='files/cheat_sheet.pdf')

if __name__ == "__main__":
    app.run(debug=True)
