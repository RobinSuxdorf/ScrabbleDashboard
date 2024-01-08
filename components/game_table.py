from dash import Dash, dash_table, html
import pandas as pd

def render(app: Dash, data: pd.DataFrame) -> html.Div:
    filtered_data = data[data['Deniz Spielverlauf'].isna() == False]

    return html.Div(
        children=[
            dash_table.DataTable(filtered_data.to_dict('records'))
        ]
    )