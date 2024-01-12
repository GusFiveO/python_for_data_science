import numpy as np


def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """give_bmi"""
    try:
        if len(height) != len(weight):
            print("Both parameter should have the same length")
            return None
    except Exception:
        print("Both parameter should be iterable")
        return None
    bmi_list = list()
    merged_list = np.column_stack((height, weight))
    for height, weight in merged_list:
        if not isinstance(height, float | int) \
                or not isinstance(weight, float | int):
            print("Both parameter should only contain float or integer")
            return None
        bmi_list.append(weight / np.square(height))
    return bmi_list


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """apply_limit"""
    try:
        for elem in bmi:
            if not isinstance(elem, float | int):
                print("Parameter should only contain float or integer")
                return None
        return np.array([True if elem >= limit else False for elem in bmi])
    except Exception:
        print("First parameter should be iterable")
        return None
