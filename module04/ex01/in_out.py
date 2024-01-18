def square(x: int | float) -> int | float:
    """square function"""
    return x**2


def pow(x: int | float) -> int | float:
    """pow function"""
    return x**x


def outer(x: int | float, function) -> object:
    """outer function"""
    def inner() -> float:
        """inner function"""
        nonlocal x
        x = function(x)
        return x

    return inner
