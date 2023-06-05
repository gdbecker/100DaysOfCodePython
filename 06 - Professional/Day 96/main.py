# 100 Days of Code: Python
# August 19-23, 2022
# Online Shop web app
# Using the theme Twenty from https://html5up.net/

# Import modules
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor, CKEditorField
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy import asc, desc, func
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, SelectField, FloatField, IntegerField
from wtforms.validators import DataRequired
from flask_gravatar import Gravatar

# STATIC VARIABLES
US_STATES = ["", "AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY",
             "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH",
             "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]
ITEM_STATUS = ["Available", "Sold Out", "On Order", "Restocking"]
ITEM_RATING = ["⭐", "⭐⭐", "⭐⭐⭐", "⭐⭐⭐⭐", "⭐⭐⭐⭐⭐"]
CARD_TYPE = ["Visa", "Mastercard", "American Express", "Discover"]

# Set up Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = "harrypotterravenclaw"
ckeditor = CKEditor(app)
Bootstrap(app)

# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///store.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Set up login manager
login_manager = LoginManager()
login_manager.init_app(app)

# Set up Gravatar icons for comments
gravatar = Gravatar(app,
                    size=50,
                    rating='g',
                    default='retro',
                    force_default=False,
                    force_lower=False,
                    use_ssl=False,
                    base_url=None
        )

# Function to make a 0 or 1 a Boolean valaue
def make_bool(val: int) -> bool:
    return bool(int(val))

# Configure User table in database
class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100), nullable=False)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(1000), nullable=True)
    city = db.Column(db.String(100), nullable=True)
    state = db.Column(db.String(10), nullable=True)
    zip = db.Column(db.String(10), nullable=True)

    # *************** User is the PARENT to Card ************* #
    # User has multiple cards
    cards = relationship("Card", back_populates="shopper")

    # *************** User is the PARENT to Order ************* #
    # User has multiple orders
    orders = relationship("Order", back_populates="shopper")

    # *************** Item is the PARENT to Temp_Order ************* #
    # Item is in multiple temp_orders
    temp_orders = relationship("Temp_Order", back_populates="shopper")

    # *************** User is the PARENT to Review ************* #
    # User has multiple reviews
    reviews = relationship("Review", back_populates="shopper")

# Configure Item table in database
class Card(db.Model):
    __tablename__ = "cards"
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(500), unique=False, nullable=False)
    cardholder_name = db.Column(db.String(500), unique=False, nullable=False)
    card_number = db.Column(db.String(100), unique=False, nullable=False)
    expiration_date = db.Column(db.String(100), unique=False, nullable=False)
    security_code = db.Column(db.String(5), unique=False, nullable=False)

    # *************** Card is the CHILD to User ************* #
    # Multiple cards per User
    shopper_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    shopper = relationship("User", back_populates="cards")

# Configure Item table in database
class Item(db.Model):
    __tablename__ = "items"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(500), unique=False, nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(2000), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    status = db.Column(db.String(100), nullable=False)

    # *************** Item is the CHILD to Category ************* #
    # Multiple items per Category
    category_id = db.Column(db.Integer, db.ForeignKey("categories.id"))
    parent_category = relationship("Category", back_populates="items")

    # *************** Item is the PARENT to Order ************* #
    # Item is in multiple orders
    orders = relationship("Order", back_populates="parent_item")

    # *************** Item is the PARENT to Temp_Order ************* #
    # Item is in multiple temp_orders
    temp_orders = relationship("Temp_Order", back_populates="parent_item")

    # *************** Item is the PARENT to Review ************* #
    # Item has multiple reviews
    reviews = relationship("Review", back_populates="parent_item")

# Configure Category table in database
class Category(db.Model):
    __tablename__ = "categories"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)

    # *************** Category is the PARENT to Item ************* #
    # Category has multiple items
    items = relationship("Item", back_populates="parent_category")

# Configure Order table in database
class Order(db.Model):
    __tablename__ = "orders"
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, unique=False, nullable=False)
    quantity = db.Column(db.Integer, unique=False, nullable=False)
    date = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(100), nullable=False)

    # *************** Order is the CHILD to Item ************* #
    # Multiple orders per Item
    item_id = db.Column(db.Integer, db.ForeignKey("items.id"))
    parent_item = relationship("Item", back_populates="orders")

    # *************** Order is the CHILD to User ************* #
    # Multiple orders per User
    shopper_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    shopper = relationship("User", back_populates="orders")

# Configure Temp_Order table in database
# Hold Order info here as User shops, delete when they place the order officially
class Temp_Order(db.Model):
    __tablename__ = "temp_orders"
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, unique=False, nullable=False)
    quantity = db.Column(db.Integer, unique=False, nullable=False)

    # *************** Temp_Order is the CHILD to Item ************* #
    # Multiple temp_orders per Item
    item_id = db.Column(db.Integer, db.ForeignKey("items.id"))
    parent_item = relationship("Item", back_populates="temp_orders")

    # *************** Temp_Order is the CHILD to User ************* #
    # Multiple temp_orders per User
    shopper_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    shopper = relationship("User", back_populates="temp_orders")

# Configure Review table in database
class Review(db.Model):
    __tablename__ = "reviews"
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(1000), nullable=True)
    date = db.Column(db.String(100), nullable=False)
    rating = db.Column(db.String(10), nullable=False)

    # *************** Review is the CHILD to Item ************* #
    # Multiple reviews per Item
    item_id = db.Column(db.Integer, db.ForeignKey("items.id"))
    parent_item = relationship("Item", back_populates="reviews")

    # *************** Review is the CHILD to User ************* #
    # Multiple reviews per User
    shopper_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    shopper = relationship("User", back_populates="reviews")

# Make the database -> comment out when done
with app.app_context():
    db.create_all()

# Methods
# Get list of all categories, use as dropdown list in form
def get_category_list():
    all_categories_db = db.session.query(Category).all()
    category_list = []
    for c in all_categories_db:
        category_list.append(c.name)
    category_list.sort()
    return category_list

# Get list of all categories
def get_all_categories():
    all_categories_db = db.session.query(Category).all()
    return all_categories_db

# Get list of all items
def get_all_items():
    all_items_db = db.session.query(Item).all()
    return all_items_db

# Get list of all items in shopping cart
def get_all_cart_items(user_id):
    all_items_db = Temp_Order.query.filter_by(shopper_id=int(user_id))
    return all_items_db

# Get list of all orders for user
def get_order_history(user_id):
    all_order_items_db = Order.query.filter_by(shopper_id=int(user_id))
    return all_order_items_db

# Get list of all orders
def get_all_orders():
    all_orders_db = db.session.query(Order).all()
    return all_orders_db

# Get list of reviews for an item
def get_reviews_by_item(item_id):
    all_reviews_db = Review.query.filter_by(item_id=int(item_id))
    return all_reviews_db

# Get list of reviews for user
def get_reviews_by_user(user_id):
    all_reviews_db = Review.query.filter_by(shopper_id=int(user_id))
    return all_reviews_db

# Get list of cards for user
def get_cards_by_user(user_id):
    all_cards_db = Card.query.filter_by(shopper_id=int(user_id))
    return all_cards_db

# Get list of cards for user at shopping cart
def get_cards_by_user_form(user_id):
    all_cards_db = Card.query.filter_by(shopper_id=int(user_id))
    card_list = []
    for c in all_cards_db:
        card_list.append(f"{c.cardholder_name}: {c.card_number}")
    return card_list

# Form classes
class RegisterForm(FlaskForm):
    email = StringField(label="Email", validators=[DataRequired()])
    password = PasswordField(label="Password", validators=[DataRequired()])
    first_name = StringField(label="First Name", validators=[DataRequired()])
    last_name = StringField(label="Last Name", validators=[DataRequired()])
    submit_register = SubmitField("Sign up!")

class LoginForm(FlaskForm):
    email = StringField(label="Email", validators=[DataRequired()])
    password = PasswordField(label="Password", validators=[DataRequired()])
    submit_login = SubmitField("Log In")

class EditUserForm(FlaskForm):
    email = StringField(label="Email", validators=[DataRequired()])
    first_name = StringField(label="First Name", validators=[DataRequired()])
    last_name = StringField(label="Last Name", validators=[DataRequired()])
    address = StringField(label="Address")
    city = StringField(label="City")
    state = SelectField(label="State", choices=US_STATES)
    zip = StringField(label="Zip Code")
    submit_user = SubmitField("Confirm Changes")

class CreateCategoryForm(FlaskForm):
    name = StringField(label="", validators=[DataRequired()])
    submit_category = SubmitField("Add Category")

class CreateItemForm(FlaskForm):
    category = SelectField(label="Category", validators=[DataRequired()], choices=get_category_list)
    name = StringField(label="Item Name", validators=[DataRequired()])
    price = FloatField(label="Price", validators=[DataRequired()])
    description = CKEditorField(label="Description", validators=[DataRequired()])
    img_url = StringField(label='Image Location/URL', validators=[DataRequired()])
    status = SelectField(label="Item Status", validators=[DataRequired()], choices=ITEM_STATUS)
    submit_item = SubmitField("Submit Item")

class AddItemToOrderForm(FlaskForm):
    quantity = IntegerField(label="Quantity", validators=[DataRequired()])
    submit_item = SubmitField("Add to Order")

class SubmitOrderForm(FlaskForm):
    payment = SelectField(label="Payment Method", validators=[DataRequired()])
    submit_order = SubmitField("Submit Order")

class ReviewForm(FlaskForm):
    rating = SelectField(label="Add a Review", validators=[DataRequired()], choices=ITEM_RATING)
    text = CKEditorField(label="", validators=[DataRequired()])
    submit_review = SubmitField("Submit Review")

class CardForm(FlaskForm):
    type = SelectField(label="Card Type", validators=[DataRequired()], choices=CARD_TYPE)
    cardholder_name = StringField(label="Cardholder Name", validators=[DataRequired()])
    card_number = StringField(label="Card Number", validators=[DataRequired()])
    expiration_date = StringField(label="Expiration Date", validators=[DataRequired()])
    security_code = StringField(label="Security Code", validators=[DataRequired()])
    submit_card = SubmitField("Add Card")

# Required: call-back function to get a user by id
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Flask routes
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "GET":
        return render_template("index.html")

@app.route("/account", methods=["GET", "POST"])
@login_required
def account():
    form = EditUserForm(obj=current_user)
    form.state.data = current_user.state
    if request.method == "GET":
        return render_template("account.html", form=form)
    elif request.method == "POST":
        current_user.email = request.form["email"]
        current_user.first_name = request.form["first_name"]
        current_user.last_name = request.form["last_name"]
        current_user.address = request.form["address"]
        current_user.city = request.form["city"]
        current_user.state = request.form["state"]
        current_user.zip = request.form["zip"]
        db.session.commit()
        return redirect(url_for("home"))

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
        return redirect(url_for("home"))

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
            name=request.form["name"],
            price=request.form["price"],
            description=request.form["description"],
            img_url=request.form["img_url"],
            status=request.form["status"]
        )
        db.session.add(new_item)
        db.session.commit()
        return redirect(url_for("catalog_manager"))

@app.route("/edit-item/<item_id>", methods=["GET", "POST"])
@login_required
def edit_item(item_id):
    item_to_update = Item.query.filter_by(id=int(item_id)).first()
    form = CreateItemForm(obj=item_to_update)
    form.category.data = item_to_update.parent_category.name
    if request.method == "GET":
        return render_template("edit_item.html", form=form, item=item_to_update)
    if request.method == "POST":
        category_name = request.form["category"]
        selected_category = Category.query.filter_by(name=category_name).first()
        category_id = selected_category.id
        item_to_update.category_id = category_id
        item_to_update.name = request.form["name"]
        item_to_update.price = request.form["price"]
        item_to_update.img_url = request.form["img_url"]
        item_to_update.status = status=request.form["status"]
        db.session.commit()
        return redirect(url_for("catalog_manager"))

@app.route("/delete-item/<item_id>")
@login_required
def delete_item(item_id):
    db.session.query(Item).filter(Item.id==int(item_id)).delete()
    db.session.commit()
    return redirect(url_for("home"))

@app.route("/catalog-manager")
@login_required
def catalog_manager():
    all_categories = get_all_categories()
    all_items = get_all_items()
    return render_template("catalog_manager.html", categories=all_categories, items=all_items)

@app.route("/order-manager")
@login_required
def order_manager():
    all_orders = get_all_orders()
    order_ids_raw = []
    for u in all_orders:
        order_ids_raw.append(u.order_id)
    order_ids = set(order_ids_raw)

    return render_template("order_manager.html", ids=order_ids, order=all_orders)

@app.route("/update-order/<row_id>/<option>")
@login_required
def update_order(row_id, option):
    row_to_update = Order.query.filter_by(id=int(row_id)).first()

    if option == "✔":
        row_to_update.status = "Complete"
    elif option == "✘":
        row_to_update.status = "Processing"
    db.session.commit()
    return redirect(url_for("order_manager"))

@app.route("/products")
def products():
    all_categories = get_all_categories()
    all_items = get_all_items()
    return render_template("products.html", categories=all_categories, items=all_items)

@app.route("/view-item/<item_id>", methods=["GET", "POST"])
def view_item(item_id):
    add_item_form = AddItemToOrderForm()
    add_review_form = ReviewForm()
    item_to_view = Item.query.filter_by(id=int(item_id)).first()
    item_reviews = get_reviews_by_item(item_id)
    if request.method == "GET":
        return render_template("view_item.html", add_item_form=add_item_form, add_review_form=add_review_form, item=item_to_view, reviews=item_reviews)
    elif request.method == "POST":
        if add_item_form.submit_item.data:
            new_temp_order = Temp_Order(
                order_id=0,
                quantity=request.form["quantity"],
                item_id=item_id,
                shopper_id=current_user.id
            )
            db.session.add(new_temp_order)
            db.session.commit()
            return redirect(url_for("shopping_cart"))
        elif add_review_form.submit_review.data:
            today = datetime.now()
            today_formatted = today.strftime("%m/%d/%Y")
            new_reivew = Review(
                text=request.form["text"],
                date=today_formatted,
                rating=request.form["rating"],
                item_id=item_id,
                shopper_id=current_user.id
            )
            db.session.add(new_reivew)
            db.session.commit()
            return redirect(url_for("view_item", item_id=item_id))

@app.route("/shopping-cart", methods=["GET", "POST"])
@login_required
def shopping_cart():
    form = SubmitOrderForm()
    form.payment.choices = get_cards_by_user_form(current_user.id)
    user_items = get_all_cart_items(current_user.id)

    # Get total cost
    total_cost = 0
    for i in user_items:
        total_cost += i.parent_item.price * i.quantity

    if request.method == "GET":
        return render_template("shopping_cart.html", form=form, order=user_items, cost=total_cost)
    elif request.method == "POST":
        user_items = get_all_cart_items(current_user.id)
        today = datetime.now()
        today_formatted = today.strftime("%m/%d/%Y")
        order_num = db.session.query(func.max(Order.order_id)).scalar()
        if order_num is None:
            order_num = 1
        else:
            order_num += 1
        for i in user_items:
            new_order_item = Order(
                order_id=order_num,
                quantity=i.quantity,
                date=today_formatted,
                status="Processing",
                item_id=i.item_id,
                shopper_id=i.shopper_id
            )
            db.session.add(new_order_item)
            db.session.commit()
        db.session.query(Temp_Order).filter(Temp_Order.shopper_id == int(current_user.id)).delete()
        db.session.commit()
        return redirect(url_for("order_history"))

@app.route("/delete-cart-item/<row_id>")
@login_required
def delete_cart_item(row_id):
    db.session.query(Temp_Order).filter(Temp_Order.id == int(row_id)).delete()
    db.session.commit()
    return redirect(url_for("shopping_cart"))

@app.route("/submit-order")
@login_required
def submit_order():
    user_items = get_all_cart_items(current_user.id)
    today = datetime.now()
    today_formatted = today.strftime("%m/%d/%Y")
    order_num = db.session.query(func.max(Order.order_id)).scalar()
    if order_num is None:
        order_num = 1
    else:
        order_num += 1
    for i in user_items:
        new_order_item = Order(
            order_id=order_num,
            quantity=i.quantity,
            date=today_formatted,
            status="Processing",
            item_id=i.item_id,
            shopper_id=i.shopper_id
        )
        db.session.add(new_order_item)
        db.session.commit()
    db.session.query(Temp_Order).filter(Temp_Order.shopper_id == int(current_user.id)).delete()
    db.session.commit()
    return redirect(url_for("order_history"))

@app.route("/payments", methods=["GET", "POST"])
@login_required
def payments():
    user_cards = get_cards_by_user(current_user.id)
    form = CardForm()
    if request.method == "GET":
        return render_template("payments.html", form=form, cards=user_cards)
    elif request.method == "POST":
        new_card = Card(
            type=request.form["type"],
            cardholder_name=request.form["cardholder_name"],
            card_number=request.form["card_number"],
            expiration_date=request.form["expiration_date"],
            security_code=request.form["security_code"],
            shopper_id=current_user.id
        )
        db.session.add(new_card)
        db.session.commit()
        return redirect(url_for("payments"))

@app.route("/payments-delete/<card_id>")
@login_required
def delete_payment(card_id):
    db.session.query(Card).filter(Card.id == int(card_id)).delete()
    db.session.commit()
    return redirect(url_for("payments"))

@app.route("/order-history")
@login_required
def order_history():
    user_order_items = get_order_history(current_user.id)
    order_ids_raw = []
    for u in user_order_items:
        order_ids_raw.append(u.order_id)
    order_ids = set(order_ids_raw)

    return render_template("order_history.html", ids=order_ids, order=user_order_items)

@app.route("/review-history")
@login_required
def review_history():
    user_review = get_reviews_by_user(current_user.id)

    return render_template("review_history.html", reviews=user_review)

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
                first_name=request.form["first_name"],
                last_name=request.form["last_name"]
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
            return redirect(url_for("home"))

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

# Run app
if __name__ == '__main__':
    app.run(debug=True)