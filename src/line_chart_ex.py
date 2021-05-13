import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv(r'data\2010YumaAZ.csv')
print(df.head())

days = df['DAY'].unique().tolist()

data = [go.Scatter(x=df.loc[df['DAY'] == day, "LST_TIME"],
                   y=df.loc[df['DAY'] == day, "T_HR_AVG"],
                   mode='lines',
                   name=day) for day in days]

layout = go.Layout(title='Temperature variation over the day',
                   xaxis=dict(title="Time"),
                   yaxis=dict(title='Temperature'),
                   hovermode='closest')

fig = go.Figure(data=data, layout=layout)
pyo.plot(fig)
