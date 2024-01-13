# highest score, etc.
# design

# readme -> run the app
# improve imports from ... import ()
# doc strings
# naming in csv

# player stats
    # score distribution, boxplot
    # distance to winner distribution
    # lowest/highest score
    # close looses
    # games with > 200 points
    # games with < 100 points
    # games with > 50 point lead
        # categorize wins

# game analysis
    # best turn

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
