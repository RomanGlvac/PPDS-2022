# 04
Simulating the operation of a power plant with sensors and monitors. Sensors write detected data into a data storage,
while monitors retrieve said data. Multiple sensors and monitors can operate at once, however the operations are mutualy
exclusive, meaning that either reading or writing is performed at one time.

### Synchronization patterns utilized in solution
There are multiple types of sync patterns used in the provided solution
* Lightswitch - used to provide access to either monitors or sensors at a give time
* Semaphore - two semaphores are used, one is used by the lightswitch to perform its operation, while the other is utilized as a turnstile
* Event - used in the beginning of the simulation to signal initial data write by the sensors 
* Mutex - used within the lightswitch to preserve the integrity of its internal counter

### Pseudocode
```
def main():
    data_access = Semaphore(1)
    turnstile = Semaphore(1)
    ls_monitor = Lightswitch()
    ls_sensor = Lightswitch()
    data_available = [Event() for i in <0, 2>
    
    create_and_run_thread(sensor,
                       sensor_type,
                       data_available,
                       turnstile,
                       ls_monitor,
                       data_access) for sensor_type in ('T', 'P', 'H'))
    
    create_and_run_thread(monitor,
                      monitor_id,
                      data_available,
                      turnstile,
                      ls_sensor,
                      data_access) for monitor_id in <0, 7>)
                      

def monitor(monitor_id, valid_data, turnstile, ls_monitor, data_access):
    // monitors can only start operating after
    // all sensors performed at least one write
    wait_for_initial_write(valid_data)
    
    while True:
        turnstile.wait()
        turnstile.signal()
        reading_monitor_count = ls_monitor.lock(data_access)
        reading_time = rand(40 - 50 miliseconds)
        print("monitor: {monitor_id}: no. of reading monitors={reading_monitor_count}, reading time={reading_time}")
        sleep(reading_time)
        ls_monitor.unlock(data_access)
        

def sensor(sensor_id, valid_data, turnstile, ls_sensor, data_access):
    while True:
        updating_time = rand(50 - 60 miliseconds)
        sleep(updating_time)
        // writing time is determined by sensor_id
        writing_time = (10 - 20 miliseconds or 20 - 25 miliseconds)
        
        turnstile.wait()
        writing_sensor_count = ls_sensor.lock(data_access)
        turnstile.signal()
        print("sensor: {sensor_id}: no. of writing sensors={writing_sensor_count}, writing time={writing_time}")
        sleep(writing_time)
        ls_sensor.unlock(data_access)
        
        // signal that initial data has been written
        // index is determined by sensor_id
        valid_data[0, 1, or 2].signal()
```