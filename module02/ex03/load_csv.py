import pandas


def load(path: str) -> pandas.DataFrame:
    """load a csv file"""
    csv = {}
    try:
        csv = pandas.read_csv(path)
        print(f"Loading dataset of dimensions {csv.shape}")
    except Exception as e:
        print(e)
        return None
    return csv
