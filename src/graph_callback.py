import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv(r"data\gapminderDataFiveYear.csv")
print(df.head())

# We need to get
# {
#     'label': str(year)
#     'value': year
# }
year_option = [{'label': str(year),
                'value': int(year)} for year in df['year'].unique()]

countries = df['continent'].unique()

app = dash.Dash()


app.layout = html.Div([
    dcc.Graph(id="scatter_plot"),
    dcc.Dropdown(id='dropDownMenu', options=year_option,
                 value=df['year'].min())
])


@app.callback(Output(component_id='scatter_plot', component_property='figure'),
              Input(component_id='dropDownMenu', component_property='value'))
def get_graph(year_value):
    fig = go.Figure()

    for country in countries:
        subset_df = df.loc[(df['continent'] == country) &
                           (df['year'] == year_value)]
        fig.add_trace(go.Scatter(
            x=subset_df['lifeExp'],
            y=subset_df['gdpPercap'],
            mode='markers',
            name=country,
            marker=dict(size=10),
            hovertext=subset_df['country'])
        )

        fig.update_layout(title="GDP against Life Expectancy",
                          xaxis=dict(title='GDP Per Capita', type='log'),
                          yaxis=dict(title='Life Expectancy'))

    return fig


if __name__ == "__main__":
    app.run_server(debug=True)
