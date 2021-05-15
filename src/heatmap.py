import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go
from plotly.subplots import make_subplots

df = pd.read_csv(r"data\2010SantaBarbaraCA.csv")
df2 = pd.read_csv(r'data\2010SitkaAK.csv')
df3 = pd.read_csv(r'data\2010YumaAZ.csv')

fig = make_subplots(rows=1, cols=3, shared_yaxes=True,
                    subplot_titles=['1', '2', '3'])
fig.add_trace(go.Heatmap(
    x=df['DAY'], y=df['LST_TIME'], z=df['T_HR_AVG'], colorscale='jet', name="barbara", zmin=5, zmax=40), row=1, col=1)
fig.add_trace(go.Heatmap(
    x=df2['DAY'], y=df2['LST_TIME'], z=df2['T_HR_AVG'], colorscale='jet', name="SitkaAK", zmin=5, zmax=40), row=1, col=2)
fig.add_trace(go.Heatmap(
    x=df3['DAY'], y=df3['LST_TIME'], z=df3['T_HR_AVG'], colorscale='jet', name="YumaAZ", zmin=5, zmax=40), row=1, col=3)

fig.update_layout(title="subplots")

pyo.plot(fig)
