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



print(get_products())
print(get_sales())
print(get_stock())
