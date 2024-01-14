from dash import Dash, html, dash_table
import pandas as pd

def render(app: Dash, data: pd.DataFrame) -> html.Div:
    return html.Div(
        children=[
            dash_table.DataTable(
                data=data.describe().to_dict('records')
            )
        ]
    )