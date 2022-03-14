"""
Author:         Roman Glvac
University:     STU
Course:         PPDS
Year:           2022
License:        MIT

Simulating a power plant with x sensors and y monitors.
Sensors write values into a data storage, each sensor has its own data bracket, meaning they can write concurrently.
Monitors can also operate concurrently, since they do not modify any values.
However, the two operations are mutually exclusive, sensors cannot write data while reading is in progress (and vice versa).
"""


from time import sleep
from random import randint
from fei.ppds import Thread, Semaphore, Event, print
from lightswitch import Lightswitch


def sensor(sensor_id, valid_data, turnstile, ls_sensor, data_access):
    """Simulating the function of a sensor.

    :param sensor_id: id of the sensor (P, T, or H)
    :param valid_data: list of events to signal initial data write
    :param turnstile: turnstile to manage access to the room
    :param ls_sensor: lightswitch object, used to signal room occupation
    :param data_access: semaphore representing the room
    :return: None
    """
    while True:
        updating_time = randint(50, 60) / 1000
        sleep(updating_time)

        if sensor_id in ('T', 'P'):
            writing_time = randint(10, 20) / 1000
        else:
            writing_time = randint(20, 25) / 1000

        turnstile.wait()
        writing_sensor_count = ls_sensor.lock(data_access)
        turnstile.signal()

        print(f"Sensor id: {sensor_id}, no. of writing sensors: {writing_sensor_count}, writing time: {writing_time}")
        sleep(writing_time)

        ls_sensor.unlock(data_access)

        if sensor_id == 'P':
            valid_data[0].signal()
        elif sensor_id == 'T':
            valid_data[1].signal()
        else:
            valid_data[2].signal()


def monitor(monitor_id, valid_data, turnstile, ls_monitor, data_access):
    """Used to simulate the monitor process.

    :param monitor_id: id of the monitor
    :param valid_data: list of events to signal initial data write (monitors can start operating after some data has been written)
    :param turnstile: turnstile to manage access to the room
    :param ls_monitor: lightswitch object, used to signal room occupation
    :param data_access: semaphore representing the room
    :return: None
    """
    wait_for_data(valid_data)
    while True:
        turnstile.wait()
        turnstile.signal()
        reading_monitor_count = ls_monitor.lock(data_access)

        reading_time = randint(40, 50) / 1000
        print(f"Monitor id: {monitor_id}: no. of reading monitors: {reading_monitor_count}, reading_time: {reading_time}")
        sleep(reading_time)
        ls_monitor.unlock(data_access)


def wait_for_data(data_available):
    """Waiting for all events in data_available.

    :param data_available: list of events
    :return: None
    """
    for event in data_available:
        event.wait()


def main():
    data_access = Semaphore(1)
    turnstile = Semaphore(1)
    ls_monitor = Lightswitch()
    ls_sensor = Lightswitch()
    sensor_types = ('P', 'T', 'H')

    data_available = [Event() for _ in range(3)]
    monitors = [Thread(sensor,
                       sensor_type,
                       data_available,
                       turnstile,
                       ls_monitor,
                       data_access) for sensor_type in sensor_types]

    sensors = [Thread(monitor,
                      monitor_id,
                      data_available,
                      turnstile,
                      ls_sensor,
                      data_access) for monitor_id in range(8)]

    [thread.join() for thread in sensors + monitors]


if __name__ == "__main__":
    main()
