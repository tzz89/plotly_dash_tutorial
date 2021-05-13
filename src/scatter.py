import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go

np.random.seed(42)  # 42 is the answer to the ultimate question

random_x = np.random.randint(1, 101, 100)
random_y = np.random.randint(1, 101, 100)

data = [go.Scatter(x=random_x, y=random_y,
                   mode='markers',
                   marker=dict(
                       size=12,
                       color='rgb(41,203,144)',
                       symbol='pentagon',
                       line={'width': 2}
                   ))]

layout = go.Layout(title="Hello First plot",
                   xaxis={'title': "my X axis"},
                   yaxis=dict(title="my y axis"),
                   hovermode='closest',)

fig = go.Figure(data=data, layout=layout)

pyo.plot(fig)
