"""
Author:         Roman Glvac
University:     STU
Course:         PPDS
Year:           2022
License:        MIT
"""


from random import randint
from time import sleep
import time


def do_stuff(cycles):
    """Serves as a simulation of a repetitive task.
    :param cycles: task will be repeated "cycles" times
    :return: None
    """
    print(f"I will now do stuff {cycles} times.")
    for i in range(cycles):
        sleep(0.0000000001)


def main():
    """Runs do_stuff() a given amount of times and prints information about the duration of the whole process.
    :return: None
    """
    repetitions = 10
    lower_bound = 100
    start = time.time()

    for i in range(repetitions):
        do_stuff(lower_bound + randint(10, 100))

    end = time.time()
    print(f"That took {end - start} seconds.")


if __name__ == "__main__":
    main()
