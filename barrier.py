"""
Author:         Roman Glvac
University:     STU
Course:         PPDS
Year:           2022
License:        MIT
"""


from fei.ppds import Event, Mutex


class SimpleBarrier:
    """ Implements a simple barrier mechanism for N threads
    """

    def __init__(self, N):
        self.N = N
        self.C = 0
        self.mutex = Mutex()
        self.barrier = Event()

    def wait(self):
        self.mutex.lock()
        self.C += 1

        if self.C == self.N:
            self.barrier.signal()

        self.mutex.unlock()
        self.barrier.wait()

        self.mutex.lock()
        if self.C == self.N:
            self.C = 0
            self.barrier.clear()
        self.mutex.unlock()
