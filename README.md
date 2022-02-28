# 02
Solutions to problems from the second seminar in the PPDS course. First two sections of README are descriptions of individual files/folders and the last section is dedicated to answering questions asked at the end of the seminar.
## ./reusable_barrier
Folder contains solution to the reusable barrier with events problem.
### ./reusable_barrier/simplebarrier.py
Implementation of a reusable barrier using the event synchronization pattern. All threads are blocked until the last one arrives and calls event.signal(), releasing all blocked threads. After crossing the barrier, one of the threads resets the event by calling event.clear(), allowing the barrier to be reusable, for example in a loop.
### ./reusable_barrier/barriertest.py
Used to run a testing function for the reusable barrier. Creates NUM_THREADS threads and runs barrier_cycle_example().

## ./Fibonacci
This folder contains solutions to the multithreaded fibonacci sequence calculation problem.
### ./Fibonacci/orderedbarrier.py
This file contains an implementation of a barrier for N threads, where N-1 threads are blocked until the Nth thread arrives at the barrier. 
Order of released threads is given by their corresponding thread_id. 
To achieve this, a dictionary is used, in which pairs of thread_ids and synchronization objects (either Events or Semaphores) are stored.
### ./Fibonacci/fibonacci.py
fibonacci.py serves as a test for the aforementioned barrier. 
The barrier is used before the actual computation of sequence elements begins, ensuring all threads have data necessary for their operation.
### ./Fibonacci/activeFibonacci.py
This file contains an experiment of sorts. 
It also contains multithreaded calculation of the fibonacci sequence, however it doesn't use any synchronization patterns. 
It ensures validity of the results by checking a condition in a while loop, which checks whether all required elements have already been calculated.

## Questions
Q: How many synchronization objects (mutexes, semaphores, events...) are required to solve the multithreaded Fibonacci sequence computation problem?

A: The solution in this repo uses NUM_THREADS + 1 synchronization objects - one 'shared' mutex and one event/semaphore per each thread. My attempts to reduce the number of synchronization objects led to nowhere, I wasn't able to make it work.
Well, I created the solution without any synchronization objects at all, but that is sidestepping the issue, really.

---
Q: Which synchronization objects can be reasonably used in the same problem? Describe your use of these objects.

A: My solution uses synchronization objects mentioned above, which are combined to create a barrier, which releases blocked threads in ascending order determined by their ID. The mutex is used to preserve integrity of the barrier thread counter, which is incremented everytime a thread arrives at the barrier.
Since a separate counter is used for releasing the threads in order, the same mutex is used to preserve the counter's integrity. The rest of the events/semaphores are used for releasing individual threads.