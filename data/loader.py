import pandas as pd

class DataSchema:
    DENIZ = "Deniz"
    DANYEL = "Danyel"
    ROBIN = "Robin"
    SIEGER = "Sieger"
    STARTER = "Starter"
    DENIZ_SPIELVERLAUF = "Deniz Spielverlauf"
    DANYEL_SPIELVERLAUF = "Danyel Spielverlauf"
    ROBIN_SPIELVERLAUF = "Robin Spielverlauf"

def load_scrabble_data(path: str) -> pd.DataFrame:
    data = pd.read_csv(
        path,
        dtype={
            DataSchema.DENIZ: int,
            DataSchema.DANYEL: int,
            DataSchema.ROBIN: int,
            DataSchema.SIEGER: str,
            DataSchema.STARTER: str,
            DataSchema.DENIZ_SPIELVERLAUF: object,
            DataSchema.DANYEL_SPIELVERLAUF: object,
            DataSchema.ROBIN_SPIELVERLAUF: object
        },
        index_col=0
    )
    return data