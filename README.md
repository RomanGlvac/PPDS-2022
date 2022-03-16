# 05

## Problem specification
The goal of this application is to simulate a dinner situation in a tribe. There are two types of tribesmen -
savages and cooks. Savages gather at dinner, where they receive and eat servings of steamed missionaries from
a shared pot. The amount of servings in the pot gradually lowers as the dinner goes on, until it eventually 
completely runs out of servings. The first savage to notice the empty pot 'wakes up' the cooks. The cooks' job is to prepare more 
servings of missionaries and place them into the pot. When the food preparation is complete, the aforementioned 
savage is notified by one of the cooks and he and his colleagues can continue eating.

## Solution
The solution utilizes multiple synchronization patterns to achieve the goal described above.

Specifically they are (sync pattern - usage count):
* Mutex - 3
* Event - 2
* Semaphore - 1

These are used within shared.py and barrier.py. shared.py contains the Shared class, which represents the shared pot.
barrier.py, as the name implies, contains an implementation of a barrier, which is used to make sure that savages start 
eating dinner at the same time, and also to ensure that all cooks are ready when they are notified by one of the savages.
###Pseudocode
```
def main():
    shared = Shared(0)
    barrier_savage = Barrier(N_SAVAGES)
    barrier_cook = Barrier(N_COOKS)
    
    for i in <0, N_SAVAGES):
        create_and_run_thread(savage, i, shared, barrier_savage)
    for i in <0, N_COOKS):
        create_and_run_thread(cook, i, shared, barrier_cook)
        

def savage(savage_id, shared, barrier):
    // sleep to randomize arrival order at barrier
    sleep(0.01 to 1 seconds)
    while True:
    
        // wait for all savages
        barrier.wait()
        shared.mutex.lock()
        
        // notify the cooks if the pot is empty
        if shared.portions == 0:
            print("Savage {savage_id} calling cook.")
            wake_up_cooks()
            wait_for_food()
            
        // pot has a portion available, proceed to eat
        print("Savage {savage_id} getting serving from pot.")
        shared.portions -= 1
        shared.mutex.unlock()
        sleep(0.01 to 1 seconds)
        
        
def cook(cook_id, shared, barrier):
    while True:
        // make sure all cooks are ready to cook
        barrier.wait()
        // waiting until pot to is empty
        shared.pot_empty.wait()
        print("Cook {cook_id} cooking.")
        // simulating cooking time
        sleep(0.01 to 3 seconds)
        
        // using mutex to preserve integrity of the cook counter
        shared.cook_mutex.lock()
        shared.cook_counter += 1
        // if all cooks have finished cooking
        if shared.cook_counter == N_COOKS:
            shared.portions += N_PORTIONS
            shared.cook_counter = 0
            print("Cook {cook_id} serving.")
            shared.pot_empty.clear()
            // notify savage that he can continue eating
            shared.pot_full.signal()
        shared.cook_mutex.unlock()
```

#####Disclaimer
No missionaries were harmed, hurt or harassed during the simulation.
