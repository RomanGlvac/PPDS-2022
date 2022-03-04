"""
Author:         Roman Glvac
University:     STU
Course:         PPDS
Year:           2022
License:        MIT
"""


from fei.ppds import Mutex, Semaphore


class Shared:
    """Represents a shared storage space.
    Useful for simulating a multithreaded production / consumption process.

    """
    def __init__(self, storage_size):
        self.finished = False
        self.mutex = Mutex()
        self.free = Semaphore(storage_size)
        self.items = Semaphore(0)
