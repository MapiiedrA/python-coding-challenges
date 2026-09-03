### ASYNCHRONY ###

import datetime
import time
import asyncio

async def task(name: str, duration: int):
    print(
        f"Task: {name}, Duration: {duration}s. Start: {datetime.datetime.now()}")
    await asyncio.sleep(duration)
    print(
        f"Task: {name}, End: {datetime.datetime.now()}")


asyncio.run(task("1", 2))
asyncio.run(task("2", 3))

"""
EXTRA CHALLENGE (optional):
 * Using the concept of asynchrony and the previous function, create
 * the following program that executes in this order:
 * - A function C that lasts 10 seconds.
 * - A function B that lasts 7 seconds.
 * - A function A that lasts 4 seconds.
 * - A function D that lasts 1 second.
 * - Functions C, B, and A run in parallel.
 * - Function D starts its execution once the previous 3 have
 *   finished.
 """

async def async_task():
    await asyncio.gather(task("C", 10), task("B", 7), task("A", 4))
    await task("D", 1)

asyncio.run(async_task())