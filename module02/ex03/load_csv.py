import pandas


def load(path: str):
    """load a csv file"""
    csv = {}
    try:
        csv = pandas.read_csv(path)
    except Exception as e:
        print(e)
        return None
    return csv
