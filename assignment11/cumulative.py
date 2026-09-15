"""Assignment 11, task 2 - cumulative revenue over the orders, as a line plot.

Each order is worth the sum of price * quantity over its line items. Ordered by
order_id and added up as we go, those totals show how the revenue accumulated.
"""

import sqlite3

import pandas as pd
import matplotlib.pyplot as plt

DB_PATH = "../db/lesson.db"

SQL_STATEMENT = """
SELECT orders.order_id,
       SUM(products.price * line_items.quantity) AS total_price
FROM orders
JOIN line_items ON orders.order_id = line_items.order_id
JOIN products ON line_items.product_id = products.product_id
GROUP BY orders.order_id
ORDER BY orders.order_id
"""

conn = None

try:
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query(SQL_STATEMENT, conn)
except sqlite3.Error as e:
    print(f"A database error occurred: {type(e).__name__} {e}")
    raise SystemExit(1)
finally:
    if conn is not None:
        conn.close()

# cumsum() walks the column once and keeps a running total. The apply() version
# shown in the lesson re-adds every row above the current one, so it does the
# same work again on every row - the same answer for a lot more effort.
df["cumulative"] = df["total_price"].cumsum()

print(df.head())
print(f"\n{len(df)} orders, total revenue {df['cumulative'].iloc[-1]:,.2f}")

df.plot(
    x="order_id",
    y="cumulative",
    kind="line",
    color="seagreen",
    legend=False,
    figsize=(10, 6),
    title="Cumulative revenue by order",
)
plt.xlabel("Order id")
plt.ylabel("Cumulative revenue ($)")
plt.grid(color="gray", linestyle="--", linewidth=0.5)
plt.tight_layout()
plt.show()
