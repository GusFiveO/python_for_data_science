def ft_filter(check_function, _list):
    """filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""
    filtered_list = [elem for elem in _list if check_function
                     is None or check_function(elem) is True]
    return filtered_list


def check_even(number):
    """returning a boolean depending if the number passed in
     parameter is Even or not"""
    if number % 2 == 0:
        return True
    return False


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def main():
    print(ft_filter(check_even, numbers))
    print(list(filter(check_even, numbers)))
    print(ft_filter(None, numbers))
    print(list(filter(None, numbers)))
    print(ft_filter(None, 4))
    print(list(filter(None, 4)))
    print(filter.__doc__)
    print(ft_filter.__doc__)


if __name__ == "__main__":
    main()
