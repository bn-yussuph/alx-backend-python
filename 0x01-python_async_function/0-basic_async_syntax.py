#!/usr/bin/env python3

import asyncio
from random import random

async def wait_random(max_delay: int = 10):
    wait = max_delay * random()
    await asyncio.sleep(wait)
    return wait


if __name__ == "__main__":
    asyncio.run(wait_random())