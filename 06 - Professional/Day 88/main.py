# 100 Days of Code: Python
# August 13-14, 2022
# "To-Do" task manager web app
# Using the theme Astral from https://html5up.net/

# garrett@email.com
# qwerty

# Import modules
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy import asc, desc
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, DateField, SelectField
from wtforms.validators import DataRequired

# Set up Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = "harrypotterravenclaw"
Bootstrap(app)

# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///items.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Set up login manager
login_manager = LoginManager()
login_manager.init_app(app)

# Function to make a 0 or 1 a Boolean valaue
def make_bool(val: int) -> bool:
    return bool(int(val))

# Configure User table in database
class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

    # This will act like a list of Item objects attached to each User.
    # The "author" refers to the author property in the Item class.
    items = relationship("Item", back_populates="author")

# Configure Item table in database
class Item(db.Model):
    __tablename__ = "items"
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(500), unique=False, nullable=False)
    due_date = db.Column(db.String(250), nullable=False)
    status = db.Column(db.Boolean, nullable=False)

    # Create Foreign Key, "users.id" the users refers to the table name of User.
    author_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    # Create reference to the User object, the "items" refers to the items property in the User class.
    author = relationship("User", back_populates="items")

    # *************** Child Relationship ************* #
    category_id = db.Column(db.Integer, db.ForeignKey("categories.id"))
    parent_category = relationship("Category", back_populates="items")

# Configure Category table in database
class Category(db.Model):
    __tablename__ = "categories"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)

    # *************** Parent Relationship ************* #
    items = relationship("Item", back_populates="parent_category")

# Make the database -> comment out when done
# with app.app_context():
#     db.create_all()
    
# Methods
# Get list of all categories, use as dropdown list in form
def get_all_categories():
    all_categories_db = db.session.query(Category).all()
    category_list = []
    for c in all_categories_db:
        category_list.append(c.name)
    return category_list

# Get list of options to sort tasks by due date, use as dropdown list in form
def get_date_sort_options():
    return ["Neither", "Sooner First", "Later First"]

# Get list of options to sort categories, use as dropdown list in form
def get_category_sort_options():
    category_list = get_all_categories()
    category_list.insert(0, "All")
    return category_list

# Get list of options to sort completion status, use as dropdown list in form
def get_completed_sort_options():
    return ["All", "Completed", "Not Completed"]

# Get all items from database for the current user
def get_all_items(user_id, date_sort, category_sort, completed_sort):
    # all_items = Item.query.filter_by(author_id=int(user_id)).all()
    all_items = None
    if category_sort != "All":
        result = Category.query.filter_by(name=category_sort).first()
        selected_category_id = result.id
        print(selected_category_id)

    if category_sort != "All":
        if date_sort == "Sooner First":
            if completed_sort == "Completed":
                all_items = Item.query.filter_by(author_id=int(user_id)).filter_by(
                    category_id=int(selected_category_id)).filter_by(status=True).order_by(asc(Item.due_date))
            elif completed_sort == "Not Completed":
                all_items = Item.query.filter_by(author_id=int(user_id)).filter_by(
                    category_id=int(selected_category_id)).filter_by(status=False).order_by(asc(Item.due_date))
            else:
                all_items = Item.query.filter_by(author_id=int(user_id)).filter_by(
                    category_id=int(selected_category_id)).order_by(asc(Item.due_date))
        elif date_sort == "Later First":
            if completed_sort == "Completed":
                all_items = Item.query.filter_by(author_id=int(user_id)).filter_by(
                    category_id=int(selected_category_id)).filter_by(status=True).order_by(desc(Item.due_date))
            elif completed_sort == "Not Completed":
                all_items = Item.query.filter_by(author_id=int(user_id)).filter_by(
                    category_id=int(selected_category_id)).filter_by(status=False).order_by(desc(Item.due_date))
            else:
                all_items = Item.query.filter_by(author_id=int(user_id)).filter_by(
                    category_id=int(selected_category_id)).order_by(desc(Item.due_date))
        else:
            if completed_sort == "Completed":
                all_items = Item.query.filter_by(author_id=int(user_id)).filter_by(
                    category_id=int(selected_category_id)).filter_by(status=True)
            elif completed_sort == "Not Completed":
                all_items = Item.query.filter_by(author_id=int(user_id)).filter_by(
                    category_id=int(selected_category_id)).filter_by(status=False)
            else:
                all_items = Item.query.filter_by(author_id=int(user_id)).filter_by(
                    category_id=int(selected_category_id))
    else:
        if date_sort == "Sooner First":
            if completed_sort == "Completed":
                all_items = Item.query.filter_by(author_id=int(user_id)).filter_by(status=True).order_by(asc(Item.due_date))
            elif completed_sort == "Not Completed":
                all_items = Item.query.filter_by(author_id=int(user_id)).filter_by(status=False).order_by(asc(Item.due_date))
            else:
                all_items = Item.query.filter_by(author_id=int(user_id)).order_by(asc(Item.due_date))
        elif date_sort == "Later First":
            if completed_sort == "Completed":
                all_items = Item.query.filter_by(author_id=int(user_id)).filter_by(status=True).order_by(desc(Item.due_date))
            elif completed_sort == "Not Completed":
                all_items = Item.query.filter_by(author_id=int(user_id)).filter_by(status=False).order_by(desc(Item.due_date))
            else:
                all_items = Item.query.filter_by(author_id=int(user_id)).order_by(desc(Item.due_date))
        else:
            if completed_sort == "Completed":
                all_items = Item.query.filter_by(author_id=int(user_id)).filter_by(status=True)
            elif completed_sort == "Not Completed":
                all_items = Item.query.filter_by(author_id=int(user_id)).filter_by(status=False)
            else:
                all_items = Item.query.filter_by(author_id=int(user_id))
    return all_items

# Form classes
class RegisterForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    name = StringField("Name", validators=[DataRequired()])
    submit_register = SubmitField("Sign me up!")

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit_login = SubmitField("Login")

class CreateItemForm(FlaskForm):
    category = SelectField(label="Category", validators=[DataRequired()], choices=get_all_categories)
    text = StringField("Task", validators=[DataRequired()])
    due_date = DateField("Due Date", validators=[DataRequired()])
    submit_item = SubmitField("Add Task")

class CreateCategoryForm(FlaskForm):
    name = StringField("", validators=[DataRequired()])
    submit_category = SubmitField("Add Category")

class SortItemForm(FlaskForm):
    date_sort = SelectField(label="Sort Dates By", choices=get_date_sort_options)
    category_sort = SelectField(label="Select Category View", choices=get_category_sort_options)
    completed_sort = SelectField(label="Completion Status", choices=get_completed_sort_options)
    submit_sort = SubmitField("Filter")

# Required: call-back function to get a user by id
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Flask routes
@app.route("/", methods=["GET", "POST"])
def home():
    register_form = RegisterForm()
    category_form = CreateCategoryForm()
    item_form = CreateItemForm()
    if request.method == "GET":
        return render_template("index.html", register_form=register_form, category_form=category_form, item_form=item_form)

@app.route("/items", methods=["GET", "POST"])
@login_required
def items():
    item_list = get_all_items(current_user.id, "Neither", "All", "All")
    form = SortItemForm()
    if request.method == "GET":
        return render_template("items.html", items=item_list, form=form)
    elif request.method == "POST":
        date_sort = request.form["date_sort"]
        category_sort = request.form["category_sort"]
        completed_sort = request.form["completed_sort"]
        updated_item_list = get_all_items(current_user.id, date_sort, category_sort, completed_sort)
        return render_template("items.html", items=updated_item_list, form=form)

@app.route("/additem", methods=["GET", "POST"])
@login_required
def add_item():
    form = CreateItemForm()
    if request.method == "GET":
        return render_template("add_item.html", form=form)
    elif request.method == "POST":
        category_name = request.form["category"]
        selected_category = Category.query.filter_by(name=category_name).first()
        category_id = selected_category.id
        new_item = Item(
            category_id=category_id,
            text=request.form["text"],
            due_date=request.form["due_date"],
            status=False,
            author=current_user
        )
        db.session.add(new_item)
        db.session.commit()
        return redirect(url_for("items"))

@app.route("/edit-item/<item_id>")
@login_required
def edit_item(item_id):
    item_to_update = Item.query.filter_by(id=int(item_id)).first()
    item_to_update.status = True
    db.session.commit()

    item_list = get_all_items(current_user.id, "Neither", "All", "All")
    return redirect(url_for("items", items=item_list))

@app.route("/delete-item/<item_id>")
@login_required
def delete_item(item_id):
    db.session.query(Item).filter(Item.id==int(item_id)).delete()
    db.session.commit()
    item_list = get_all_items(current_user.id, "Neither", "All", "All")
    return redirect(url_for("items", items=item_list))

@app.route("/addcategory", methods=["GET", "POST"])
@login_required
def add_category():
    form = CreateCategoryForm()
    if request.method == "GET":
        return render_template("add_category.html", form=form)
    elif request.method == "POST":
        new_category = Category(
            name=request.form["name"]
        )
        db.session.add(new_category)
        db.session.commit()
        return redirect(url_for("items"))

# Authentication routes
@app.route('/register', methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if request.method == "GET":
        return render_template("register.html", form=form)
    elif request.method == "POST":
        user = User.query.filter_by(email=request.form["email"]).first()
        if user != None:
            flash("You've already signed up with that email. Login instead!")
            return redirect(url_for("login"))
        else:
            new_user = User(
                email=request.form["email"],
                password=generate_password_hash(request.form["password"], method="pbkdf2:sha256", salt_length=8),
                name=request.form["name"]
            )
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
            return redirect(url_for("home"))

@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if request.method == "GET":
        return render_template("login.html", form=form)
    elif request.method == "POST":
        user = User.query.filter_by(email=request.form.get("email")).first()
        if user == None:
            flash("That email does not exist! Please try again.")
            return redirect(url_for("login"))
        elif check_password_hash(user.password, request.form.get("password")):
            login_user(user)
            return redirect(url_for("items"))

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

# Run app
if __name__ == '__main__':
    app.run(debug=True)