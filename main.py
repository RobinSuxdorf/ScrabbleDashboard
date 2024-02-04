# design
# categorize wins

# readme -> run the app, requirements, etc.
# improve imports from ... import ()
# doc strings
# naming in csv

# game analysis
    # best turn
    # average turn
    # count of turns

# settings
    # language
    # player colors
    # light/dark mode
    # selected players

# add entry

from dash import Dash
import pandas as pd

from components.layout import create_layout
from data.loader import load_scrabble_data
from components.callbacks import get_callbacks

DATA_PATH = "./scrabble_data.csv"

def main() -> None:
    data = load_scrabble_data(DATA_PATH)

    app = Dash(__name__)
    app.title = 'Scrabble Dashboard'
    app.layout = create_layout(app, data)
    get_callbacks(app)
    app.run(debug=True)

if __name__ == '__main__':
    main()
