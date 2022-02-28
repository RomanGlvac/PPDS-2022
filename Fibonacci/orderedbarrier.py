"""
Author:         Roman Glvac
University:     STU
Course:         PPDS
Year:           2022
License:        MIT
"""


from fei.ppds import Event, Mutex, Semaphore


class OrderedBarrier:
    """ Implements a barrier mechanism for N threads, where threads are released in ascending order given by their id
    """

    def __init__(self, N):
        self.N = N
        self.C = 0
        self.mutex = Mutex()
        self.release_counter = 0
        self.thread_dict = dict()

    def wait(self, thread_id):
        """Close barrier until all N threads arrive, then let threads through one by one.
        Last thread releases thread num. 0, which then releases thread num. 1 etc.
        Variable 'adt' can either be an Event, or a Semaphore initialized to 0.

        :param thread_id: identifier for current thread
        :return: None
        """
        self.mutex.lock()
        adt = Event()
        # adt = Semaphore(0)
        self.thread_dict[thread_id] = adt
        self.C += 1
        self.mutex.unlock()

        # releasing last thread
        if self.C == self.N:
            release_first = self.thread_dict[self.release_counter]
            self.release_counter += 1
            release_first.signal()

        adt.wait()

        self.mutex.lock()
        if self.release_counter != self.N:
            release_next = self.thread_dict[self.release_counter]
            self.release_counter += 1
            release_next.signal()
        self.mutex.unlock()
