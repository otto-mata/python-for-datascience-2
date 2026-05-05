import pandas as pd


def load(path: str) -> pd.DataFrame | None:
    """Load a CSV file using pandas.read_csv, returning
    the newly created pandas.DataFrame. In the event of
    an error, print the error and return None."""
    try:
        df = pd.read_csv(path)
        print(df.shape)
        return df
    except (FileNotFoundError, ValueError) as ex:
        print(f"{ex.__class__.__name__}: {ex}")
        return None
