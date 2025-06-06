#!/usr/bin/env python3
"""
Function takes an integer `max_delay` and returns a `asyncio.Task`
"""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Parameters
        max_delay: int, default 10

    Return
        an object: asyncio.Task
    """
    
    task = asyncio.create_task(wait_random(max_delay))

    return task


if __name__ == "__main__":
    task_wait_random(5)
