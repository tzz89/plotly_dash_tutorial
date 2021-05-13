import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv(r"data\mocksurvey.csv", index_col=0)
print(df.head())

data = [go.Bar(y=df.index, x=df[respond], name=respond, orientation='h')
        for respond in df.columns]
# layout = go.Layout(title="Mock Survey Results",
#                    xaxis=dict(title="Percentage of respond"),
#                    yaxis=dict(title="Question number"),
#                    hovermode='closest',
#                    barmode='stack',
#                    )
fig = go.Figure(data=data)
fig.update_layout(title="Mock Survey Results",
                  xaxis=dict(title="Percentage of respond"),
                  yaxis=dict(title="Question number"),
                  hovermode='closest',
                  barmode='stack')
pyo.plot(fig)
