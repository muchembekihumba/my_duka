import psycopg2
conn = psycopg2.connect(host='localhost',port=5432,user='postgres',password='saka2010.',dbname='myduka')
cur = conn.cursor()

def insert_products(values):
    cur.execute(
        "INSERT INTO products (name, buying_price, selling_price) VALUES (%s, %s, %s)",
        values
    )
    conn.commit()

def create_transaction():
    cur.execute("INSERT INTO transactions DEFAULT VALUES RETURNING id")
    transaction_id = cur.fetchone()[0]
    conn.commit()
    return transaction_id

def insert_sales(transaction_id, pid, quantity):
    cur.execute(
        "INSERT INTO sales (transaction_id, pid, quantity) VALUES (%s, %s, %s)",
        (transaction_id, pid, quantity)
    )
    conn.commit()

def insert_stock(values):
    cur.execute(
        "INSERT INTO stock (pid, stock_quantity) VALUES (%s, %s)",
        values
    )
    conn.commit()

def get_products():
    cur.execute('select * from products')
    return cur.fetchall()

def get_sales():
    cur.execute('select * from sales')
    return cur.fetchall()

def get_sales_with_names():
    cur.execute("""
        SELECT t.id, p.name, s.quantity, t.created_at
        FROM sales s
        JOIN products p ON s.pid = p.id
        JOIN transactions t ON s.transaction_id = t.id
        ORDER BY t.id
    """)
    return cur.fetchall()

def get_stock():
    cur.execute('select * from stock')
    return cur.fetchall()

def get_stock_with_names():
    cur.execute("""
        SELECT s.id, p.name, s.stock_quantity
        FROM stock s
        JOIN products p ON s.pid = p.id
    """)
    return cur.fetchall()

def sales_per_day():
    cur.execute("""
        SELECT DATE(s.created_at), SUM(s.quantity * p.selling_price) AS "Total Sales"
        FROM sales s
        JOIN products p ON s.pid = p.id
        GROUP BY DATE(s.created_at)
        ORDER BY DATE(s.created_at)
    """)
    return cur.fetchall()

def profit_per_day():
    cur.execute("""
        SELECT DATE(s.created_at), SUM((p.selling_price - p.buying_price) * s.quantity) AS "Gross Profit"
        FROM sales s
        JOIN products p ON s.pid = p.id
        GROUP BY DATE(s.created_at)
        ORDER BY DATE(s.created_at)
    """)
    return cur.fetchall()

def sales_per_product():
    cur.execute("""
        SELECT p.name, SUM(s.quantity * p.selling_price) AS "Total Sales"
        FROM sales s
        JOIN products p ON s.pid = p.id
        GROUP BY p.name
        ORDER BY SUM(s.quantity * p.selling_price) DESC
    """)
    return cur.fetchall()

def profit_per_product():
    cur.execute("""
        SELECT p.name, SUM((p.selling_price - p.buying_price) * s.quantity) AS profit
        FROM sales s
        JOIN products p ON s.pid = p.id
        GROUP BY p.name
        ORDER BY profit DESC
    """)
    return cur.fetchall()

def insert_user(full_name, email, phone_number, password_hash):
    cur.execute(
        "INSERT INTO users (full_name, email, phone_number, password) VALUES (%s, %s, %s, %s)",
        (full_name, email, phone_number, password_hash)
    )
    conn.commit()

def get_user_by_email(email):
    cur.execute("SELECT id, full_name, email FROM users WHERE email = %s", (email,))
    return cur.fetchone()


