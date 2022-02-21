# 01

## Mutex
Files first.py, second.py and third.py showcase three different ways of using a mutex to avoid erroneous behaviour of two threads running in parrallel.

### first.py
In first.py, the mutex lock/unlock surround the whole body of the main while loop in increment_elms(). The mutex is also unlocked if shared.counter is greater than or equal to shared.end. This solution completely eliminated incorrect behavior which can be observed if the mutex is not used.

### second.py
second.py is very similar to first.py in its usage of the mutex, however the condition of the main while loop in increments_elms() is "while shared.counter < shared.elms" as opposed to just "while True", and the above mentioned unlocking condition in first.py is omitted. Therefore, this solution increments elements in shared.elms correctly, however, at the end of the while loop, one thread causes an exception, because it tries to increment at an invalid index (beyond size of shared.elms). This is because both threads evaluate the condition of the while loop as True, therefore both attempt to perform the incrementation and one of them does so at an incorrect index.

### third.py
The solution in third.py is the most simple one of the three, because the first thread to enter increment_elms() acquires the lock even before entering the while loop. The second thread has to wait for the first one to complete the loop and unlock the lock. It then acquires the lock, evaluates the condition of the while loop as False, therefore it never performs any incrementation, unlocks the lock and exits the function. This obviously eliminates any undesirable behaviour, since the incrementation is only performed by one of the threads.
