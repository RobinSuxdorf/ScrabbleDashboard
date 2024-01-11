from dash import Dash, dcc, html, Input, Output
import pandas as pd

from . import win_distribution_chart
from . import game_analysis

def create_layout(app: Dash, data: pd.DataFrame) -> html.Div:
    @app.callback(
        Output('tabs_content', 'children'),
        Input('navigation_tabs', 'value')
    )
    def render_content(tab: str) -> html.Div:
        if tab == 'tab_overview':
            return win_distribution_chart.render(app, data)

        elif tab == 'tab_game_analysis':
            return game_analysis.render(app, data)

    return html.Div(
        children=[
            html.H1(app.title),
            html.Hr(),
            dcc.Tabs(
                id='navigation_tabs',
                value='tab_overview',
                children=[
                    dcc.Tab(value='tab_overview', label='Überblick'),
                    dcc.Tab(value='tab_game_analysis', label='Spielverlauf')
                ]
            ),
            html.Div(id='tabs_content')
        ]
    )