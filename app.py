# Import libraries
from dash import Dash, html, dcc, Input, Output
import pandas as pd
import plotly.express as px

# Load the dataset
avocado = pd.read_csv('Baseino_laisvos_vietos_cleen.csv')
# fig = px.line(avocado, x="Hour", y="Laisvos_vietos")
# Create the Dash app
app = Dash()


cats = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
# Set up the app layout
geo_dropdown = dcc.Dropdown(options=avocado['Weekday'].unique(),
                            value='Monday')


app.layout = html.Div(children=[
    html.H1(children='Baseino uzimtumo statistika'),
    geo_dropdown,
    dcc.Graph(
        id='bar_chart',
        # figure=fig
    )
])

# avocado['Laisvos_vietos'] = avocado['Laisvos_vietos'].mean().round(1)
# print(avocado)

# Set up the callback function
@app.callback(
    Output(component_id='bar_chart', component_property='figure'),
    Input(component_id=geo_dropdown, component_property='value')
)
def update_graph(selected_geography):
    filtered_avocado = avocado[avocado['Weekday'] == selected_geography].groupby('Hour', as_index=False).mean('Laisvos_vietos').round()
    line_fig = px.line(filtered_avocado,
                       x='Hour', y='Laisvos_vietos',
                       title=f' {selected_geography}')
    return line_fig


# Run local server
if __name__ == '__main__':
    app.run_server(debug=True)