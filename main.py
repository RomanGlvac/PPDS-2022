"""
Author:         Roman Glvac
University:     STU
Course:         PPDS
Year:           2022
License:        MIT
"""


from random import randint
from time import sleep
from fei.ppds import Thread, Semaphore, print
from shared import Shared


def customer(customer_id, shared):
    """Simulates a customer visiting a barber shop.
    The barber shop has a certain capacity defined in the Shared object.
    If there is a seat available (either in the waiting room, or the barber chair) he stays in the shop.
    If there are no free seats, the customer leaves and returns in a random time.

    :param customer_id: id of the customer
    :param shared: instance of the Shared class
    :return: None
    """
    while True:
        barber_semaphore = Semaphore(0)
        shared.mutex.lock()

        print(f'Customer {customer_id} enters barbershop.')

        if shared.customers == shared.max_customers:
            print(f'Customer {customer_id} leaves (barbershop full).')
            shared.mutex.unlock()
            sleep(randint(10, 20) / 10)
            continue

        shared.customers += 1
        shared.queue.append(barber_semaphore)
        shared.mutex.unlock()

        shared.customer_semaphore.signal()
        barber_semaphore.wait()

        print(f'Customer {customer_id} getting haircut.')
        sleep(randint(10, 20) / 10)
        print(f'Customer {customer_id} finished cutting.')

        shared.customer_done.signal()
        shared.barber_done.wait()

        shared.mutex.lock()
        shared.customers -= 1
        shared.mutex.unlock()


def barber(shared):
    """Simulates a barber cutting customers' hair.
    First, the barber has to wait for a customer to arrive.
    If there is a customer in the store, the barber can call him to the barber chair and start cutting hair.
    After finishing the haircut, the process repeats.

    :param shared: instance of the Shared class
    :return: None
    """
    while True:
        shared.customer_semaphore.wait()

        semaphore = shared.queue.pop(0)
        semaphore.signal()

        # print('Barber cutting hair.')
        shared.customer_done.wait()
        shared.barber_done.signal()
        # print('Barber done.')


def main():
    """Runs the barbershop simulation, where a single barber cuts customers' hair.
    For a more detailed description, please refer to the docs in customer() and barber().

    :return: None
    """
    shared = Shared(3)
    brbr = Thread(barber, shared)
    customers = [Thread(customer, i, shared) for i in range(6)]


if __name__ == "__main__":
    main()
