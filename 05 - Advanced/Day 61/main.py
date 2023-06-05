# 100 Days of Code: Python
# June 19, 2022
# Flask project
# advanced forms

# Import modules
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from flask_bootstrap import Bootstrap

# Set up Flask app
app = Flask(__name__)
Bootstrap(app)
app.secret_key = "harrypotterravenclaw"

# Credentials
auth_email = "admin@email.com"
auth_password = "12345678"

# Login Form Class
class LoginForm(FlaskForm):
    email = StringField(label="Email", validators=[DataRequired(), Email()])
    password = PasswordField(label="Password", validators=[DataRequired(), Length(min=8)])
    submit = SubmitField(label="Log In")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login_page():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        if login_form.email.data == auth_email and login_form.password.data == auth_password:
            return render_template("success.html")
        else:
            return render_template("denied.html")

    return render_template("login.html", form=login_form)

if __name__ == '__main__':
    app.run(debug=True)