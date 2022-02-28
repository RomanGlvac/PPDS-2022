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


def compute_fibonacci(i):
    """Used to compute element of fibonacci sequence

    :param i: index to calculate
    :return: None
    """
    if i != 0:
        while True:
            if fib_seq[i] != 0 and fib_seq[i + 1] != 0:
                fib_seq[i + 2] = fib_seq[i] + fib_seq[i + 1]
                break
    else:
        fib_seq[i + 2] = fib_seq[i] + fib_seq[i + 1]


def run_computation(thread_id):
    """Run multithreaded computation of fibonacci sequence

    :param thread_id: id of current thread
    :return: None
    """
    sleep(get_sleep_interval())
    compute_fibonacci(thread_id)


NUM_THREADS = 10
fib_seq = [0] * (NUM_THREADS + 2)
fib_seq[1] = 1
threads = [Thread(run_computation, i) for i in range(NUM_THREADS)]
[thread.join() for thread in threads]

print(fib_seq)
