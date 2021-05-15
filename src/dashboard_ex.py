import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd

app = dash.Dash()

df = pd.read_csv(r"data\OldFaithful.csv")
print(df.head())

x_data = df['X']
y_data = df['Y']

fig = go.Figure()
scatter_plot_marker = dict(size=10.0, color='aliceblue')

fig.add_trace(go.Scatter(x=x_data, y=y_data,
              mode='markers', marker=scatter_plot_marker))

layout = go.Layout(title='Old Faithful Eruption Intervals vs Duration',
                   xaxis=dict(title="Duration of eruption (minutes)"),
                   yaxis=dict(title="Interval to next Eruption (minutes)"),
                   plot_bgcolor="#111111",
                   height=700)
fig.update_layout(layout)

header_H1_style = {
    "fontsize": 3,
    "color": "#111111",
    "text-align": "center"
}

app.layout = html.Div(children=[
    html.H1("Welcome to my Dashboard", style=header_H1_style),
    dcc.Graph(id="First scatter plot",
              figure=fig)
])

if __name__ == "__main__":
    app.run_server(debug=True)
