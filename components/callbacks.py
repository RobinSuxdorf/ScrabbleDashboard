from dash import Dash
from .game_analysis import game_analysis_callbacks


def get_callbacks(app: Dash) -> None:
    game_analysis_callbacks.get_callbacks(app)