#!/usr/bin/env python3

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random

async def task_wait_n(n, max_delay) -> List[float]:
    delays = []
    for i in range(0, n):
        task = task_wait_random(max_delay)
        result = await task
        delays.append(result)
    
    return delays


if __name__ == "__main__":
    asyncio.run(wait_n(5, 5))