"""Lesson 11.2 - an interactive scatter plot with Plotly.

The iris dataset ships with Plotly, so no file is needed. The chart is written
to iris.html: the page carries its own JavaScript, so hovering, zooming and
selecting work in any browser, with no Python running behind it.
"""

import plotly.express as px
import plotly.data as pldata

df = pldata.iris(return_type="pandas")

fig = px.scatter(
    df,
    x="sepal_length",
    y="petal_length",
    color="species",
    title="Iris Data, Sepal vs. Petal Length",
    hover_data=["petal_length"],
)

# write_html, not fig.show(): show() often hangs outside a notebook.
fig.write_html("iris.html", auto_open=True)
print("iris.html written")
