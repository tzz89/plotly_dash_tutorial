import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv(r"data\mpg.csv")
print(df.head())
print(df.columns)

fig = go.Figure()

fig.add_trace(go.Scatter(x=df['horsepower'], y=df['mpg'], mode='markers',
                         text=(df['name']),
                         marker=dict(size=df['weight']/100,
                                     color=df['cylinders'],
                                     showscale=True),

                         )
              )
fig.update_layout(title='Bubble Chart',
                  xaxis=dict(title="horsepower"),
                  yaxis=dict(title="mpg"))
pyo.plot(fig)
