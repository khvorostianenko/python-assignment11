"""Assignment 11, task 1 - revenue per employee as a bar chart.

Every order belongs to an employee, every order has line items, and every line
item names a product with a price. Revenue per employee is therefore a chain of
three joins, summed as price * quantity and grouped by the employee.
"""

import sqlite3

import pandas as pd
import matplotlib.pyplot as plt

DB_PATH = "../db/lesson.db"

SQL_STATEMENT = """
SELECT employees.last_name,
       SUM(products.price * line_items.quantity) AS revenue
FROM employees
JOIN orders ON employees.employee_id = orders.employee_id
JOIN line_items ON orders.order_id = line_items.order_id
JOIN products ON line_items.product_id = products.product_id
GROUP BY employees.employee_id
"""

conn = None

try:
    conn = sqlite3.connect(DB_PATH)
    employee_results = pd.read_sql_query(SQL_STATEMENT, conn)
except sqlite3.Error as e:
    print(f"A database error occurred: {type(e).__name__} {e}")
    raise SystemExit(1)
finally:
    if conn is not None:
        conn.close()

print(employee_results)

# Sorted so the chart reads as a ranking rather than as the order of the table.
employee_results = employee_results.sort_values("revenue", ascending=False)

employee_results.plot(
    x="last_name",
    y="revenue",
    kind="bar",
    color="steelblue",
    edgecolor="black",
    legend=False,
    figsize=(10, 6),
    title="Revenue by employee",
)
plt.xlabel("Employee last name")
plt.ylabel("Revenue ($)")
plt.tight_layout()
plt.show()
