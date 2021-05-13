import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv(r"data\abalone.csv")
print(df.head())

data = [go.Histogram(x=df['length'], xbins=dict(start=0, end=1, size=0.02))]
layout = go.Layout(title='Abalone length histogram')

fig = go.Figure(data=data, layout=layout)

pyo.plot(fig)
