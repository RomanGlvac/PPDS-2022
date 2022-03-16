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
from shared import Shared
from barrier import SimpleBarrier


N_SAVAGES = 10
N_COOKS = 3
N_PORTIONS = 20


def cook(cook_id, shared, barrier):
    """Simulates a savage cook.

    :param cook_id: id of the cook
    :param shared: instance of the Shared class, used to simulate a shared pot
    :param barrier: a Barrier object, used for all cooks to start cooking at the same time
    :return: None
    """
    while True:
        barrier.wait()
        shared.pot_empty.wait()
        print(f"Cook {cook_id} cooking.")
        sleep(randint(1, 300) / 100)

        shared.cook_mutex.lock()
        shared.cook_counter += 1
        if shared.cook_counter == N_COOKS:
            shared.portions += N_PORTIONS
            shared.cook_counter = 0
            print(f"Cook {cook_id} serving.")
            shared.pot_empty.clear()
            shared.pot_full.signal()
        shared.cook_mutex.unlock()


def savage(savage_id, shared, barrier):
    """Simulates one savage dining, retrieves servings from a shared pot.

    :param savage_id: id of the savage
    :param shared: instance of the Shared class, used to simulate a shared pot
    :param barrier: a Barrier object, used to make savages wait for each other before they start eating
    :return: None
    """
    sleep(randint(1, 100) / 100)
    while True:
        barrier.wait()
        shared.mutex.lock()
        if shared.portions == 0:
            print(f"Savage {savage_id} calling cook. (pot empty)")
            shared.pot_empty.signal()
            shared.pot_full.wait()
        print(f"Savage {savage_id} getting serving from pot.")
        shared.portions -= 1
        shared.mutex.unlock()
        # print(f"Savage {savage_id} eating.")
        sleep(randint(1, 10) / 100)
        # print(f"Savage {savage_id} finished eating.")


def main():
    """Simulating a dinner situation in a tribe.
    There a two types of tribe members - savage and cook.
    Savages retrieve and eat portions of steamed missionaries from a shared pot.
    Cooks provide the food by cooking and filling the pot.

    :return: None
    """
    shared = Shared(0)
    barrier_savage = SimpleBarrier(N_SAVAGES)
    barrier_cook = SimpleBarrier(N_COOKS)
    savages = [Thread(savage, i, shared, barrier_savage) for i in range(N_SAVAGES)]
    cooks = [Thread(cook, i, shared, barrier_cook) for i in range(N_COOKS)]

    [thread.join() for thread in savages + cooks]


if __name__ == "__main__":
    main()
