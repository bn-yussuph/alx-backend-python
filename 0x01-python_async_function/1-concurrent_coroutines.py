#!/usr/bin/env python3

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n, max_delay) -> List[float]:
    delays = []
    for i in range(0, n):
        task = wait_random(max_delay)
        result = await task
        delays.append(result)
    
    return delays


if __name__ == "__main__":
    asyncio.run(wait_n(5, 5))