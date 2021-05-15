import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

app.layout = html.Div([
    html.Label("Dropdown"),
    dcc.Dropdown(options=[{'label': "New york city",
                           'value': "NYC"},
                          {'label': "San Francisco",
                           "value": 'SF'}
                          ], value="SF"),
    html.Label("Slider"),
    dcc.Slider(min=-10, max=10, step=0.5, value=0,
               marks={i: str(i) for i in range(-10, 10)}),

    html.Label("Radio items"),
    dcc.RadioItems(options=[{'label': "New york city",
                             'value': "NYC"},
                            {'label': "San Francisco",
                             "value": 'SF'}
                            ], value="SF")
])


if __name__ == "__main__":
    app.run_server(debug=True)
