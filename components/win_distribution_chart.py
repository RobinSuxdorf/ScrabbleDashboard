from dash import Dash, dcc,  html
import pandas as pd
import plotly.express as px

def render(app: Dash, data: pd.DataFrame) -> html.Div:
    return html.Div(
        children=[
            dcc.Graph(figure=px.histogram(data, x='Sieger', color='Sieger'))
        ]
    )