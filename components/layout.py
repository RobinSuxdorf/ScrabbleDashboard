from dash import Dash, dcc, html, Input, Output
import pandas as pd

from .overview import overview
from .game_analysis import game_analysis

def create_layout(app: Dash, data: pd.DataFrame) -> html.Div:
    """
    Creates the layout of the application.

    Args:
        app (Dash): The dash app.
        data (pd.DataFrame): The scrabble data.

    Returns:
        html.Div: Container for the app.
    """
    @app.callback(
        Output('tabs_content', 'children'),
        Input('navigation_tabs', 'value')
    )
    def render_content(tab: str) -> html.Div:
        """
        Callback for the tabs.

        Args:
            tab (str): Value of the chosen tab.

        Returns:
            html.Div: Div container for the tab navigation.
        """
        if tab == 'tab_overview':
            return overview.render(app, data)

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