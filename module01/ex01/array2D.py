import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """slice_me"""
    if not isinstance(family, list):
        print("First parameter must be a list")
        return None
    if len(family) and not all(len(elem) == len(family[0]) for elem in family):
        print("First parameter must be a list of same size list")
        return None
    try:
        np_family = np.array(family)
        new_family = np_family[start:end]
        print(f"My shape is : {np_family.shape}")
        print(f"My new shape is : {new_family.shape}")
        return new_family
    except Exception:
        print("Last two parameter must be integer")
