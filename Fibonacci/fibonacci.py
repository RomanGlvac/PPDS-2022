"""
Author:         Roman Glvac
University:     STU
Course:         PPDS
Year:           2022
License:        MIT
"""


from time import sleep
from fei.ppds import Thread
from barriertest import get_sleep_interval
from orderedbarrier import OrderedBarrier


def compute_fibonacci(b, thread_id):
    """Multithreaded computation of fibonacci sequence.
    Each thread computes one element of the sequence at index [thread_id + 2].

    :param b: instance of barrier object
    :param thread_id: id of thread running this function
    :return: None
    """
    sleep(get_sleep_interval())
    b.wait(thread_id)
    fib_seq[thread_id + 2] = fib_seq[thread_id] + fib_seq[thread_id + 1]


if __name__ == "__main__":
    NUM_THREADS = 10
    barrier = OrderedBarrier(NUM_THREADS)

    fib_seq = [0] * (NUM_THREADS + 2)
    fib_seq[1] = 1

    threads = [Thread(compute_fibonacci, barrier, i) for i in range(NUM_THREADS)]
    [thread.join() for thread in threads]

    print(fib_seq)
