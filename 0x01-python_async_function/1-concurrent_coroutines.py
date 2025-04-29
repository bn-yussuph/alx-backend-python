#!/usr/bin/env python3
"""
Function returns the list of all the delays (float values).
The list of the delays are in ascending order without using `sort()` because of
concurrency.
"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Parameters
        n: int
        max_delay: int

    Return
        A list of float values
    """
    
    delays = []
    for i in range(0, n):
        task = wait_random(max_delay)
        result = await task
        delays.append(result)
    
    return delays


if __name__ == "__main__":
    asyncio.run(wait_n(5, 5))
