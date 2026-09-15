"""Lesson 11.1 - plotting straight from a Pandas DataFrame.

Two charts over the same small table: a line plot for the trend of sales and
expenses over the months, and a bar plot for the sales of each month on its own.
Pandas draws them, Matplotlib puts them on the screen.
"""

import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Sales": [100, 150, 200, 250, 300, 350],
    "Expenses": [80, 120, 180, 200, 220, 300],
}
df = pd.DataFrame(data)

# A line plot suits a trend over time: the eye follows the slope between months.
df.plot(x="Month", y=["Sales", "Expenses"], kind="line", title="Sales vs. Expenses")
plt.show()

# A bar plot suits a comparison between categories: each month is its own bar.
df.plot(x="Month", y="Sales", kind="bar", color="skyblue", title="Monthly Sales")
plt.show()
