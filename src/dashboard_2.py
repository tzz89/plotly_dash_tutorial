import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import numpy as np


app = dash.Dash()

# creating data
np.random.seed(42)
random_x = np.random.randint(1, 100, 100)
random_y = np.random.randint(1, 100, 100)


app.layout = html.Div([dcc.Graph(id='scatterplot',
                                 figure={'data': [go.Scatter(x=random_x, y=random_y, mode='markers', marker={'size': 12,
                                                                                                             'color': 'rgb(31,204,153)'})],
                                         'layout': go.Layout(title='My Scatterplot',
                                                             xaxis={'title': 'some xtitle'})}),
                       dcc.Graph(id='scatterplot2',
                                 figure={'data': [go.Scatter(x=random_x, y=random_y, mode='markers', marker={'size': 12,
                                                                                                             'color': 'rgb(31,204,153)'})],
                                         'layout': go.Layout(title='Second Scatterplot',
                                                             xaxis={'title': 'some xtitle'})})


                       ])

if __name__ == "__main__":
    app.run_server(debug=True)
