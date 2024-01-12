def isNan(value):
    return value != value


def NULL_not_found(obj: any) -> int:
    trick_dict = {
        None: "Nothing",
        float("NaN"): "Cheese",
        0: "Zero",
        "": "Empty",
        False: "Fake",
    }

    associated_string = trick_dict.get(obj)

    if associated_string:
        print(f"{associated_string}: {obj} {type(obj)}")
    elif isNan(obj):
        print(f"Cheese: {obj} {type(obj)}")
    else:
        print("Type not Found")
        return 1
    return 0
