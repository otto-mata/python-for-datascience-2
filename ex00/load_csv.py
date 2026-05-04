import pandas as pd


def load(path: str) -> pd.DataFrame | None:
    try:
        df = pd.read_csv(path)
        print(df.shape)
        return df
    except (FileNotFoundError, ValueError) as ex:
        print(f"{ex.__class__.__name__}: {ex}")
        return None
