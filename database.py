import psycopg2
conn = psycopg2.connect(host='localhost',port=5432,user='postgres',password='saka2010.',dbname='myduka')
cur = conn.cursor()

def insert_products(values):
    cur.execute(
        "INSERT INTO products (name, buying_price, selling_price) VALUES (%s, %s, %s)",
        values
    )
    conn.commit()

def insert_sales(values):
    cur.execute(
        "INSERT INTO sales (pid, quantity) VALUES (%s, %s)",
        values
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

def get_stock():
    cur.execute('select * from stock')
    return cur.fetchall()

def sales_per_day():
    cur.execute("""
        SELECT DATE(created_at), SUM(quantity)
        FROM sales
        GROUP BY DATE(created_at)
        ORDER BY DATE(created_at)
    """)
    return cur.fetchall()

def profit_per_day():
    cur.execute("""
        SELECT DATE(s.created_at), SUM((p.selling_price - p.buying_price) * s.quantity)
        FROM sales s
        JOIN products p ON s.pid = p.id
        GROUP BY DATE(s.created_at)
        ORDER BY DATE(s.created_at)
    """)
    return cur.fetchall()

def sales_per_product():
    cur.execute("""
        SELECT p.name, SUM(s.quantity)
        FROM sales s
        JOIN products p ON s.pid = p.id
        GROUP BY p.name
        ORDER BY SUM(s.quantity) DESC
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

print(get_products())
print(get_sales())
print(get_stock())
print(sales_per_day())
print(profit_per_day())
print(sales_per_product())
print(profit_per_product())
