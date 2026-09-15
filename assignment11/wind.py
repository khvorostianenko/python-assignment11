"""Assignment 11, task 3 - an interactive scatter plot of the Plotly wind data.

The dataset gives, for each compass direction, how often the wind blew at each
strength band. The strength arrives as text ("0-1", "6+"), so it has to be
turned into a number before it can carry an axis.
"""

import plotly.express as px
import plotly.data as pldata

df = pldata.wind(return_type="pandas")

print("=== first 10 rows")
print(df.head(10))
print("\n=== last 10 rows")
print(df.tail(10))
print(f"\nstrength as read: {df['strength'].dtype}, values {sorted(df['strength'].unique())}")

# Each strength is a band rather than a measurement: "0-1" means "between 0 and
# 1". Dropping everything from the dash or the plus onwards keeps the lower
# bound of the band, which is the number the band is named after and the one
# that keeps the bands in their original order on the axis.
df["strength"] = df["strength"].str.replace(r"[-+].*$", "", regex=True).astype(float)

print(f"strength after cleaning: {df['strength'].dtype}, values {sorted(df['strength'].unique())}")

fig = px.scatter(
    df,
    x="strength",
    y="frequency",
    color="direction",
    title="Wind frequency by strength and direction",
    labels={
        "strength": "Wind strength (lower bound of the band)",
        "frequency": "Frequency (%)",
        "direction": "Direction",
    },
    hover_data=["direction", "strength", "frequency"],
)

# The HTML page carries its own JavaScript, so hover, zoom and the legend
# filtering keep working with no Python behind it.
fig.write_html("wind.html", auto_open=True)
print("\nwind.html written")
