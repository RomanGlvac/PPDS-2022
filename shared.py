"""
Author:         Roman Glvac
University:     STU
Course:         PPDS
Year:           2022
License:        MIT
"""


from fei.ppds import Mutex, Semaphore


class Shared:
    """ A helper class for the barbershop simulation.
    Used to store information about the barbershop, such as maximum capacity, number of customers present etc.
    Also provides a queue to make sure the customers are served in correct order.
    Synchronization objects are also provided to allow for proper signalling between the barber and customers.
    """

    def __init__(self, max_customers):
        """
        :param max_customers: maximum capacity of the barbershop
        """
        self.queue = []

        self.customers = 0
        self.customer_semaphore = Semaphore(0)
        self.max_customers = max_customers

        self.mutex = Mutex()

        self.customer_done = Semaphore(0)
        self.barber_done = Semaphore(0)
