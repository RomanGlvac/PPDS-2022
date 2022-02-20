from collections import Counter
from time import sleep
from random import randint
from fei.ppds import Thread, Mutex
from shared import Shared


def increment_elms(shared):
    while shared.counter < shared.end:
        mutex.lock()
        shared.elms[shared.counter] += 1
        # using Python version 3.10
        # sleep is needed to cause desired incorrect behaviour
        sleep(randint(1, 10)/1000)
        shared.counter += 1
        mutex.unlock()


mutex = Mutex()
shared = Shared(1000)

t1 = Thread(increment_elms, shared)
t2 = Thread(increment_elms, shared)

t1.join()
t2.join()

counter = Counter(shared.elms)
print(counter.most_common())
