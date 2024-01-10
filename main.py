# refactor csv, filter data correctly
# update csv
# score distribution
# distance to winner distribution
# highest score, etc.
# game tab
# player stats
# add entry
# player colors
# readme -> run the app
# improve imports from ... import ()

from dash import Dash
import pandas as pd

from components.layout import create_layout
from data.loader import load_scrabble_data

DATA_PATH = "./Spiele-Tabelle.csv"

def main() -> None:
    data = load_scrabble_data(DATA_PATH)

    app = Dash(__name__)
    app.title = 'Scrabble Dashboard'
    app.layout = create_layout(app, data)
    app.run(debug=True)

if __name__ == '__main__':
    main()
