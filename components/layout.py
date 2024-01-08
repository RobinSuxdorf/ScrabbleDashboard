from dash import Dash, dcc, html, Input, Output
import pandas as pd

from . import win_distribution_chart
from . import game_table

def create_layout(app: Dash, data: pd.DataFrame) -> html.Div:
    @app.callback(
        Output('tabs-content', 'children'),
        Input('dashboard-tabs', 'value')
    )
    def render_content(tab: str) -> html.Div:
        if tab == 'general-data-tab':
            return win_distribution_chart.render(app, data)
        elif tab == 'game-analysis-tab':
            return game_table.render(app, data)

    return html.Div(
        children=[
            html.H1(app.title),
            html.Hr(),
            dcc.Tabs(
                id='dashboard-tabs', 
                value='general-data-tab',
                children=[
                    dcc.Tab(value='general-data-tab', label='General data'),
                    dcc.Tab(value='game-analysis-tab', label='Spielanalyse')
                ]
            ),
            html.Div(id='tabs-content')
        ]
    )