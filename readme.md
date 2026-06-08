pip install flask
pip install psycopg2-binary

### Sales Per Day
```sql
SELECT DATE(s.created_at), SUM(s.quantity * p.selling_price)
FROM sales s
JOIN products p ON s.pid = p.id
GROUP BY DATE(s.created_at)
ORDER BY DATE(s.created_at)
```

### Profit Per Day
```sql
SELECT DATE(s.created_at), SUM((p.selling_price - p.buying_price) * s.quantity)
FROM sales s
JOIN products p ON s.pid = p.id
GROUP BY DATE(s.created_at)
ORDER BY DATE(s.created_at)
```

### Sales Per Product
```sql
SELECT p.name, SUM(s.quantity)
FROM sales s
JOIN products p ON s.pid = p.id
GROUP BY p.name
ORDER BY SUM(s.quantity) DESC
```

### Profit Per Product
```sql
SELECT p.name, SUM((p.selling_price - p.buying_price) * s.quantity) AS profit
FROM sales s
JOIN products p ON s.pid = p.id
GROUP BY p.name
ORDER BY profit DESC
```