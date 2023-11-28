# Import libraries
from dash import Dash, html, dcc, Input, Output
import pandas as pd
import plotly.express as px
from uzimtumo_duomenu_analize import baseinas_clean

### update the newest dataset
baseinas_clean()

### Load the dataset
df_uzimtumas = pd.read_csv('Baseino_laisvos_vietos_cleen.csv')

### sort dropdown data list by weekdays
cats = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
df_uzimtumas['Weekday'] = pd.Categorical(df_uzimtumas['Weekday'], categories=cats, ordered=True)
df_uzimtumas = df_uzimtumas.sort_values('Weekday')

# Create the Dash app
app = Dash()
server = app.server


# Set up the app layout
day_dropdown = dcc.Dropdown(options=df_uzimtumas['Weekday'].unique(), value='Monday')


app.layout = html.Div(children=[
    html.H1(children='Baseino uzimtumo statistika'),
    day_dropdown,
    dcc.Graph(id='bar_chart')
])


# Set up the callback function
@app.callback(
    Output(component_id='bar_chart', component_property='figure'),
    Input(component_id=day_dropdown, component_property='value')
)
def update_graph(selected_day):
    filtered_uzimtumas = df_uzimtumas[df_uzimtumas['Weekday'] == selected_day].groupby('Hour', as_index=False).\
        mean('Laisvos_vietos').round()
    line_fig = px.line(filtered_uzimtumas,
                       x='Hour', y='Laisvos_vietos',
                       title=f' {selected_day}')
    return line_fig


# Run local server
if __name__ == '__main__':
    app.run_server(debug=True)