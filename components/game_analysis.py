from dash import Dash, dcc, dash_table, html, Input, Output
import plotly.express as px
import pandas as pd

from data.loader import DataSchema

def render(app: Dash, data: pd.DataFrame) -> html.Div:
    filtered_data = data[data[DataSchema.DENIZ_SPIELVERLAUF].isna() == False]

    def clean_game_data(score_data: str) -> list[int]:
        score_data = score_data[1:-1]
        score_data = score_data.split(' ')
        score_data = [int(v) for v in score_data]
        return score_data

    @app.callback(
        Output('game_process_graph', 'children'),
        Input('game_analysis_table', 'selected_rows'))
    def on_click_cell(selected_rows: list[int]) -> html.Div:
        if selected_rows is None:
            return html.Div('No row selected.')

        selected_row = selected_rows[0]
        game_data = filtered_data.iloc[selected_row]

        game_data_dict = {
            DataSchema.DENIZ: clean_game_data(game_data[DataSchema.DENIZ_SPIELVERLAUF]),
            DataSchema.DANYEL: clean_game_data(game_data[DataSchema.DANYEL_SPIELVERLAUF]),
            DataSchema.ROBIN: clean_game_data(game_data[DataSchema.ROBIN_SPIELVERLAUF])
        }

        game_data_dict['x_values'] = range(len(game_data_dict[DataSchema.DENIZ]))

        game_df = pd.DataFrame(game_data_dict)

        return html.Div(
            children=[
                dcc.Graph(figure=px.line(game_df, x='x_values', y=[DataSchema.DENIZ, DataSchema.DANYEL, DataSchema.ROBIN]))
            ]
        )

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
    