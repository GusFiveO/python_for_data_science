class calculator:
    """calculator class"""

    def __init__(self, array: list):
        """init method"""
        self.array = array

    def __add__(self, object) -> None:
        """add method"""
        for i in range(len(self.array)):
            self.array[i] += object
        print(self.array)

    def __mul__(self, object) -> None:
        """mul method"""
        for i in range(len(self.array)):
            self.array[i] *= object
        print(self.array)

    def __sub__(self, object) -> None:
        """sub method"""
        for i in range(len(self.array)):
            self.array[i] -= object
        print(self.array)

    def __truediv__(self, object) -> None:
        """truediv method"""
        try:
            for i in range(len(self.array)):
                self.array[i] /= object
            print(self.array)
        except ZeroDivisionError:
            print("Error: cannot divide by zero")
