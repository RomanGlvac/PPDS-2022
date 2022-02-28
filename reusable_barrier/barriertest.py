"""
Author:         Roman Glvac
University:     STU
Course:         PPDS
Year:           2022
License:        MIT
"""


from time import sleep
from random import randint
from fei.ppds import Thread, print
from simplebarrier import SimpleBarrier


def get_sleep_interval():
    """Used for a more succinct syntax when using sleep()

    :return: float between 0 and 1
    """
    return randint(1, 10) / 10


def rendezvous(thread_name):
    """Simulating a rendezvous point for threads.
    Prints id of currently running thread.

    :param thread_name: id of thread running function
    :return: None
    """
    sleep(get_sleep_interval())
    print('rendezvous: %s' % thread_name)


def ko(thread_name):
    """Simulating a rendezvous point for threads, same as rendezvous().
    Prints id of currently running thread.

    :param thread_name: id of thread running function
    :return: None
    """
    print('ko: %s' % thread_name)
    sleep(get_sleep_interval())


def barrier_example(barrier, thread_id):
    """Function used for testing the synchronization pattern barrier

    :param barrier: instance of barrier
    :param thread_id: id of thread
    :return: None
    """
    sleep(get_sleep_interval())
    print("Thread number %d before barrier" % thread_id)
    barrier.wait()
    print("Thread number %d after barrier" % thread_id)


def barrier_cycle_example(b1, thread_id):
    """Test synchronization pattern barrier in an infinite while loop

    :param b1: instance of barrier
    :param thread_id: id of thread
    :return: None
    """
    while True:
        b1.wait()
        rendezvous(thread_id)
        b1.wait()
        ko(thread_id)


def before_barrier(thread_id):
    """Used to distinguish threads before crossing barrier by printing their id

    :param thread_id: id of thread
    :return: None
    """
    sleep(get_sleep_interval())
    print("Before barrier %d" % thread_id)


def after_barrier(thread_id):
    """Used to distinguish threads after crossing barrier by printing their id

    :param thread_id: id of thread
    :return: None
    """
    print("After barrier %d" % thread_id)
    sleep(get_sleep_interval())


def main():
    """Creates NUM_THREADS threads and uses them to run a testing function

    :return: None
    """
    NUM_THREADS = 30
    b1 = SimpleBarrier(NUM_THREADS)
    threads = [Thread(barrier_cycle_example, b1, i) for i in range(0, NUM_THREADS)]
    # threads = [Thread(barrier_example, b1, i) for i in range(0, NUM_THREADS)]
    [thread.join for thread in threads]


if __name__ == "__main__":
    main()

