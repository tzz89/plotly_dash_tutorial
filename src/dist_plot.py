import numpy as np
import plotly.figure_factory as ff
import plotly.offline as pyo

x1 = np.random.randn(200)
x2 = np.random.randn(200)
x3 = np.random.randn(200)
x4 = np.random.randn(200)

hist_data = [x1, x2, x3, x4]
group_label = ['x1', 'x2', 'x3', 'x4']

fig = ff.create_distplot(hist_data, group_label)

pyo.plot(fig)
