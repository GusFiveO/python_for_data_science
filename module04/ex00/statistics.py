def execute_method(method, array):
    jumping_table = {}

    def jump_table(input_value):
        def decorator(func):
            jumping_table[input_value] = func
            return func

        return decorator

    @jump_table("mean")
    def mean(array):
        """mean function"""
        if len(array) == 0:
            print("ERROR")
            return
        total = sum(array)
        print(f"mean: {total / len(array)}")

    @jump_table("median")
    def median(array):
        """median function"""
        len_array = len(array)
        if len_array == 0:
            print("ERROR")
            return
        sorted_array = sorted(array)
        if len_array % 2 == 0:
            tot = (
                sorted_array[int(len_array / 2)] +
                sorted_array[int(len_array / 2) - 1]
            )
            print(f"median: {tot / 2}")
        else:
            print(f"median: {sorted_array[int(len_array / 2)]}")

    @jump_table("quartile")
    def quartile(array):
        """quartile function"""
        len_array = len(array)
        if len_array == 0:
            print("ERROR")
            return
        sorted_array = sorted(array)
        first = sorted_array[int(len_array / 4)]
        second = sorted_array[int((3 * len_array) / 4)]
        print(f"quartile: {[first, second]}")

    @jump_table("std")
    def std(array):
        """std function"""
        len_array = len(array)
        if len_array == 0:
            print("ERROR")
            return
        mean = sum(array) / len_array
        square_diff_sum = sum([pow(item - mean, 2) for item in array])

        print(f"std: {(square_diff_sum / (len_array)) ** (1 / 2)}")

    @jump_table("var")
    def var(array):
        """var function"""
        len_array = len(array)
        if len_array == 0:
            print("ERROR")
            return
        mean = sum(array) / len_array
        square_diff_sum = sum([pow(item - mean, 2) for item in array])

        print(f"var: {square_diff_sum / (len_array)}")

    func = jumping_table.get(method)
    if func:
        func(array)


def ft_statistics(*args: any, **kwargs: any) -> None:
    """ft_statistics"""
    for method in kwargs.values():
        execute_method(method, args)
