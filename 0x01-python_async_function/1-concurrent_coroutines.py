#!/usr/bin/env python3
"""
Module for concurrent asynchronous coroutine execution.
"""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Execute wait_random n times concurrently with the given max_delay.

    Args:
        n (int): Number of times to call wait_random.
        max_delay (int): Maximum delay value for wait_random.

    Returns:
        List[float]: List of delays (float) in ascending order.
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = [await delay for delay in asyncio.as_completed(tasks)]
    return delays

