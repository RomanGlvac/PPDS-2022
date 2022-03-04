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


def producer(shared):
    """Simulating the production process of a producer thread.
    Production and storage time is represented by sleep().

    :param shared: object representing the 'storage room'
    :return: None
    """
    while True:
        sleep(randint(1, 10) / 10)
        print("PRODUCER THREAD")
        shared.free.wait()
        if shared.finished:
            break
        shared.mutex.lock()
        sleep(randint(1, 10) / 100)
        shared.mutex.unlock()
        shared.items.signal()


def consumer(shared):
    """Simulating the consumption process of a consumer thread.
    Retrieval and consumption time is represented by sleep().

    :param shared: object representing the 'storage room'
    :return: None
    """
    while True:
        shared.items.wait()
        if shared.finished:
            break
        shared.mutex.lock()
        sleep(randint(1, 10) / 50)
        shared.mutex.unlock()
        print("CONSUMER THREAD")
        sleep(randint(1, 10) / 10)


def main():
    for i in range(10):
        # storage = Shared(10)
        N_CONSUMERS = 5
        N_PRODUCERS = 10
        # consumers = [Thread(consumer, storage) for _ in range(N_CONSUMERS)]
        # producers = [Thread(producer, storage) for _ in range(N_PRODUCERS)]

        sleep(1)
        # storage.finished = True
        # storage.items.signal(100)
        # storage.free.signal(100)
        # [thread.join() for thread in consumers + producers]


if __name__ == "__main__":
    main()
