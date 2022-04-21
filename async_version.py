"""
Author:         Roman Glvac
University:     STU
Course:         PPDS
Year:           2022
License:        MIT
"""


from random import randint
import time
import asyncio


async def do_stuff(cycles):
    """Serves as a simulation of a repetitive task, which can be performed asynchronously.
    :param cycles: task will be repeated "cycles" times
    :return: None
    """
    print(f"I will now do stuff {cycles} times.")
    for i in range(cycles):
        await asyncio.sleep(0.0000000001)


async def main():
    """Runs do_stuff() asynchronously 10 times and prints info about the duration of the whole process.
    :return: None
    """
    lower_bound = 100
    start = time.time()

    await asyncio.gather(
        do_stuff(lower_bound + randint(10, 100)),
        do_stuff(lower_bound + randint(10, 100)),
        do_stuff(lower_bound + randint(10, 100)),
        do_stuff(lower_bound + randint(10, 100)),
        do_stuff(lower_bound + randint(10, 100)),
        do_stuff(lower_bound + randint(10, 100)),
        do_stuff(lower_bound + randint(10, 100)),
        do_stuff(lower_bound + randint(10, 100)),
        do_stuff(lower_bound + randint(10, 100)),
        do_stuff(lower_bound + randint(10, 100)),
    )

    end = time.time()
    print(f"That took {end - start} seconds.")


if __name__ == "__main__":
    asyncio.run(main())
