# 06
## Problem specification
The goal of this application is to simulate the operation of a barbershop. There is one employee, 
who serves multiple customers one at a time. The barbershop also has a certain capacity - n seats in the
waiting room and the barber's chair. This means, that only n+1 customers can be in the store at a time. If a customer
enters the store and finds out that it's full, he leaves and returns after some time.
Since we only have one barber, only one customer can be server at one time, while all others wait in the waiting room.

## Synchronization
This application uses two types of sync patterns, one mutex and multiple semaphores. The mutex is used to 
preserve integrity of the customer counter and the customer queue (more on the queue later). The semaphores
are used to signal various events between the customers and the barber, such as a customer arriving in the store,
finishing the haircut etc. To ensure the customers are served in order, a queue of semaphores is used,
since the semaphores we use are not 'strong' semaphores. Everytime a customer enters the store (and the store is 
not full), he creates a 'personal' semaphore only used by him and adds it to the queue. When the barber is ready
to cut hair, he retrieves a semaphore from the queue and calls .signal() on it, letting the particular customer
into the barber chair. This creates a FIFO system, where the first customer to enter the store is also served first,
the second customer to enter is served second etc.
