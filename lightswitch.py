"""
Author:         Roman Glvac
University:     STU
Course:         PPDS
Year:           2022
License:        MIT
"""


from fei.ppds import Mutex, Semaphore


class Lightswitch:
    """ Implements a lightswitch-style sync object.
    A Semaphore object is used to represent a 'room'.
    First thread to call Lightswitch.lock() locks the semaphore representing the room ('switches on the light').
    Last thread to call Lightswitch.unlock() does the opposite by unlocking the semaphore ('switches off the light').
    """
    def __int__(self):
        self.counter = 0
        self.mutex = Mutex()

    def lock(self, semaphore: Semaphore):
        """Increment thread counter and 'turn on the light', if necessary.

        :param semaphore: semaphore representing the room
        :return: None
        """
        self.mutex.lock()
        if self.count == 0:
            semaphore.wait()
        self.counter += 1
        self.mutex.unlock()

    def unlock(self, semaphore: Semaphore):
        """Decrement thread counter and 'turn off the light', if necessary.

        :param semaphore: semaphore representing the room
        :return: None
        """
        self.mutex.lock()
        self.counter -= 1
        if self.counter == 0:
            semaphore.signal()
        self.mutex.unlock()
