# 07
main.py contains a very simple showcase of the usage of generator objects. Each of the three 
generators waits until the dispatcher function provides a randomly generated integer before performing
a simple divisibility test. 

Before actually sending any values, the dispatcher first calls next() on all supplied generators to 
get them into a state where they are waiting for a value to be provided. 
