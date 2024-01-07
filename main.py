# from dash import Dash, html, dcc, callback, Output, Input
# import pandas as pd
# import plotly.express as px
# import plotly.graph_objs as go
# import numpy as np

# df = pd.read_csv('./Spiele-Tabelle.csv', index_col=0)

# player_colors = {
#     'Deniz': 'green',
#     'Danyel': 'orange',
#     'Robin': 'blue',
#     'Unentschieden': 'red'
# }

# app = Dash(__name__)

# app.layout = html.Div([
#     html.Div(children='Hello World'),
#     html.Hr(),
#     dcc.Checklist(
#         ['Deniz', 'Danyel', 'Robin'],
#         ['Deniz', 'Danyel', 'Robin'],
#         inline=True,
#         id='checklist-control'
#     ),
#     dcc.Graph(figure=px.histogram(df, x='Sieger', color='Sieger', color_discrete_map=player_colors)),
#     dcc.Graph(figure={}, id='graph_score_distribution')
# ])

# @callback(
#     Output(component_id='graph_score_distribution', component_property='figure'),
#     Input(component_id='checklist-control', component_property='value')
# )
# def upgrade_score_distribution_graph(chosen_players):
#     plot_df = pd.DataFrame(dict(
#         player = np.concatenate([[player] * len(df) for player in chosen_players]),
#         data = np.concatenate([df[player] for player in chosen_players])
#     ))
    
#     fig = px.histogram(
#         plot_df,
#         x='data',
#         color='player',
#         color_discrete_map=player_colors,
#         title='Punkteverteilunng',
#         barmode='overlay'
#     )

#     return fig

# if __name__ == '__main__':
#     app.run(debug=True)

from dash import Dash

from components.layout import create_layout

def main() -> None:
    app = Dash(__name__)
    app.title = 'Scrabble Dashboard'
    app.layout = create_layout(app)
    app.run()

if __name__ == '__main__':
    main()