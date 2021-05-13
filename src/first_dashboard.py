import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()  # same as app = Flask()

app.layout = html.Div(children=[
    html.H1("Hello Dash!"),
    html.Div("Dash: Web development with python"),
    dcc.Graph(id='example',
              figure={'data': [
                 {'x': [1, 2, 3], 'y':[4, 1, 2], 'type':'bar', 'name':'SF'},
                 {'x': [1, 2, 3], 'y':[2, 4, 5], 'type':'bar', 'name':'NYC'}
              ],
                  'layout':{'title': 'bar plots!'}})
])


if __name__ == "__main__":
    app.run_server(debug=True)
