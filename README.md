# 02
## ./Fibonacci
This folder contains solutions to the multithreaded fibonacci sequence calculation problem.
### ./Fibonacci/orderedbarrier.py
This file contains an implementation of a barrier for N threads, where N-1 threads are blocked until the Nth thread arrives at the barrier. Order of released threads is given by their corresponding thread_id. To achieve this, a dictionary is used, in which pairs of thread_ids and synchronization objects (either Events or Semaphores) are stored.
### ./Fibonacci/fibonacci.py
fibonacci.py serves as a test for the aforementioned barrier. The barrier is used before the actual computation of sequence elements begins, ensuring all threads have data necessary for their operation.
### ./Fibonacci/activeFibonacci.py
This file contains an experiment of sorts. It also contains multithreaded calculation of the fibonacci sequence, however it doesn't use any synchronization patterns. It ensures validity of the results by checking a condition in a while loop, which checks whether all required elements have already been calculated.
