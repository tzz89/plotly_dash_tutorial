from typing import Text
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash()

app.layout = html.Div([
    dcc.Input(id="user_input", value="Value here",
              type='text', style={"border": "2px solid black"}),
    html.Div(id="user_output")
])


@app.callback(Output(component_id='user_output', component_property="children"),
              Input(component_id="user_input", component_property="value"),
              )
def parse_msg(user_input):
    return "You Entered: {}".format(user_input)


if __name__ == "__main__":
    app.run_server(debug=True)
