from flask import Flask
app = Flask (__name__)
@app.route('/')
def home():
    return "Hello word. This is home"

@app.route('/products')
def products():
    return "Products page"

@app.route('/sales')
def sales():
    return "Sales page"

@app.route('/stock')
def stock():
    return "Stock page"
app.run()