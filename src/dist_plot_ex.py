import pandas as pd
import plotly.figure_factory as ff
import plotly.offline as pyo

df = pd.read_csv(r"data\iris.csv")
# print(df.head())

group_label = df['class'].unique()
data_array = [df.loc[df['class'] == flower, 'sepal_length']
              for flower in group_label]
# print(data_array)

fig = ff.create_distplot(data_array, group_label)
pyo.plot(fig)
