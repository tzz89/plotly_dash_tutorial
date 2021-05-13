import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go
import numpy as np

df = pd.read_csv(r"data\abalone.csv")
print(df.head())
print(df.columns)

y1 = np.random.choice(df['rings'], 20, replace=False)
y2 = np.random.choice(df['rings'], 20, replace=False)

fig = go.Figure()
fig.add_trace(go.Box(y=y1))
fig.add_trace(go.Box(y=y2))
fig.update_layout(title="Is the sample from the same population?")

pyo.plot(fig)
