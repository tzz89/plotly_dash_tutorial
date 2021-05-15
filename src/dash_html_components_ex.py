import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

app.layout = html.Div(["This is the outer most div",
                       html.Div("This is inner loop_1",
                                style={"color": 'blue', "border": "blue 2px solid"}),
                       html.Div("This is inner_loop2",
                                style={"color": 'green', "border": "2px solid green"})
                       ],
                      style={'color': 'red', 'border': "2px solid red"}
                      )


if __name__ == "__main__":
    app.run_server(debug=True)
