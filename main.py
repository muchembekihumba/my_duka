from flask import Flask, render_template, request, redirect, url_for, flash
from flask_bcrypt import Bcrypt
from database import get_products, insert_products, get_sales_with_names, get_stock_with_names, insert_sales, create_transaction, insert_user, get_user_by_email

app = Flask(__name__)
bcrypt = Bcrypt(app)

app.secret_key = 'dfretyh567gdwewf43s'

@app.route('/')
def home():
    number = 1000
    threshold = 500
    age=45
    return render_template("index.html", x=number, threshold=threshold, age=age)

@app.route('/products')
def products():
    products = get_products()
    return render_template("products.html", products=products)

@app.route('/products/add', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        name = request.form['name']
        buying_price = request.form['buying_price']
        selling_price = request.form['selling_price']
        insert_products((name, buying_price, selling_price))
        flash(f'Product "{name}" added successfully!', 'success')
        return redirect(url_for('products'))
    return render_template("add_product.html")

@app.route('/sales/new', methods=['GET', 'POST'])
def record_sale():
    if request.method == 'POST':
        pids = request.form.getlist('pid')
        quantities = request.form.getlist('quantity')
        transaction_id = create_transaction()
        for pid, quantity in zip(pids, quantities):
            insert_sales(transaction_id, pid, quantity)
        return redirect(url_for('sales'))
    products = get_products()
    return render_template("record_sale.html", products=products)

@app.route('/sales')
def sales():
    sales = get_sales_with_names()
    return render_template("sales.html", sales=sales)

@app.route('/stock')
def stock():
    stock = get_stock_with_names()
    return render_template("stock.html", stock=stock)

@app.route('/login')
def login():
    return render_template("login.html")


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        full_name = request.form['full_name']
        email = request.form['email']
        phone_number = request.form['phone_number']
        password = request.form['password']

        if get_user_by_email(email):
            flash('An account with that email already exists.', 'danger')
            return render_template("register.html")

        password_hash = bcrypt.generate_password_hash(password).decode('utf-8')
        insert_user(full_name, email, phone_number, password_hash)
        flash('Account created successfully! You can now log in.', 'success')
        return redirect(url_for('login'))

    return render_template("register.html")

@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html")
if __name__ == '__main__':
    app.run(debug=True)