"""
Author:         Roman Glvac
University:     STU
Course:         PPDS
Year:           2022
License:        MIT
"""


from fei.ppds import Semaphore, Mutex


class Shared:
    """Used in the savages simulation to simulate a shared pot.
    """
    def __init__(self, portions):
        self.portions = portions
        self.mutex = Mutex()
        self.pot_empty = Semaphore(0)
        self.pot_full = Semaphore(0)
