from dash import Dash, dcc, dash_table, html, Input, Output, State
import plotly.express as px
import pandas as pd

from data.loader import DataSchema

def render(app: Dash, data: pd.DataFrame) -> html.Div:
    filtered_data = data[data[DataSchema.DENIZ_SPIELVERLAUF].isna() == False]

    return html.Div(
        children=[
            dash_table.DataTable(
                id='game_analysis_table',
                data=filtered_data.to_dict('records'),
                columns=[
                    {"name": i, "id": i} for i in filtered_data.columns 
                    if i not in [DataSchema.DENIZ_SPIELVERLAUF, DataSchema.DANYEL_SPIELVERLAUF, DataSchema.ROBIN_SPIELVERLAUF]
                ],
                row_selectable='single'
            ),
            html.Div(id='game_process_graph')
        ]
    )
    