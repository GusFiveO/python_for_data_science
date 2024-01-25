import polars


def load(path: str) -> polars.DataFrame:
    """load a csv file"""
    csv = {}
    try:
        csv = polars.read_csv(path)
        print(f"Loading dataset of dimensions {csv.shape}")
    except Exception as e:
        print(e)
        return None
    return csv
