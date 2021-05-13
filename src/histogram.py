import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv(r"data\mpg.csv")
print(df.head())

fig = go.Figure()
fig.add_trace(go.Histogram(x=df['mpg'], xbins=dict(start=0, end=25, size=2)))

fig.update_layout(title='histogram')

pyo.plot(fig)
