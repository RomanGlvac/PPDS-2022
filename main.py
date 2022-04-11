"""
Author:         Roman Glvac
University:     STU
Course:         PPDS
Year:           2022
License:        MIT
"""


from random import randint


def divisible_by_two():
    """Waits until a value is provided, then checks if it is divisible by two.

    :return: None
    """
    while True:
        num = (yield)
        if num % 2 == 0:
            print(f"{num} is divisible by two.")


def divisible_by_three():
    """Waits until a value is provided, then checks if it is divisible by three.

    :return: None
    """
    while True:
        num = (yield)
        if num % 3 == 0:
            print(f"{num} is divisible by three.")


def divisible_by_five():
    """Waits until a value is provided, then checks if it is divisible by five.

    :return: None
    """
    while True:
        num = (yield)
        if num % 5 == 0:
            print(f"{num} is divisible by five.")


def dispatch(funcs: list, iterations):
    """Sends random integers to iterator objects in 'funcs'.
    The process repeats 'iterations' times.

    :param funcs: list of generator objects
    :param iterations: repetitions of the sending process
    :return: None
    """
    for iterator in funcs:
        next(iterator)

    for i in range(iterations):
        num = randint(1, 100)
        for iterator in funcs:
            iterator.send(num)


def main():
    """Provides a simple demonstration for the usage of generator objects.

    :return: None
    """
    ii = divisible_by_two()
    iii = divisible_by_three()
    v = divisible_by_five()

    dispatch([ii, iii, v], 10)


if __name__ == "__main__":
    main()
