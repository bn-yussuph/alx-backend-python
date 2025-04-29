#!/usr/bin/env python3
"""
Function takes an integer `max_delay` and returns a `asyncio.Task`
"""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Parameters
        max_delay: int, default 10

    Return
        an object: asyncio.Task
    """
    
    delays = []
    for i in range(0, n):
        task = task_wait_random(max_delay)
        result = await task
        delays.append(result)
    
    return delays


if __name__ == "__main__":
    asyncio.run(task_wait_n(5, 5))
