import pandas as pd

class DataSchema:
    DENIZ = "Deniz"
    DANYEL = "Danyel"
    ROBIN = "Robin"
    WINNER = "winner"
    STARTING_PLAYER = "starting_player"
    DENIZ_SCORES = "deniz_scores"
    DANYEL_SCORES = "danyel_scores"
    ROBIN_SCORES = "robin_scores"

def load_scrabble_data(path: str) -> pd.DataFrame:
    """
    Function for loading the scrabble data.

    Args:
        path (str): The path of the datafile to be uploaded.

    Returns:
        pd.DataFrame: Returns the scrabble data.
    """
    data = pd.read_csv(
        path,
        dtype={
            DataSchema.DENIZ: int,
            DataSchema.DANYEL: int,
            DataSchema.ROBIN: int,
            DataSchema.WINNER: str,
            DataSchema.STARTING_PLAYER: str,
            DataSchema.DENIZ_SCORES: object,
            DataSchema.DANYEL_SCORES: object,
            DataSchema.ROBIN_SCORES: object
        },
        index_col=0
    )
    return data