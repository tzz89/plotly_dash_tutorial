import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv(r"data\2018WinterOlympics.csv")
print(df.head())


trace_1 = go.Bar(x=df['NOC'],
                 y=df['Gold'],
                 marker={'color': "#FFD700"})

trace_2 = go.Bar(x=df['NOC'],
                 y=df['Silver'],
                 marker={"color": "#9EA0A1"})

trace_3 = go.Bar(x=df['NOC'],
                 y=df['Bronze'],
                 marker={"color": "#CD7F32"})

data = [trace_1, trace_2, trace_3]
layout = go.Layout(title='Medals won by countries',
                   xaxis=dict(title='Countries'),
                   yaxis=dict(title='Number of medals'),
                   hovermode='closest',
                   barmode='stack')

fig = go.Figure(data=data, layout=layout)
pyo.plot(fig)
