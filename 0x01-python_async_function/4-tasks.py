#!/usr/bin/env python3
"""
Module that defines task_wait_n function, similar to wait_n but uses task_wait_random.
"""

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Executes task_wait_random n times concurrently with the given max_delay.

    Args:
        n (int): Number of times to call task_wait_random.
        max_delay (int): Maximum delay value for each task_wait_random call.

    Returns:
        List[float]: List of delays (float) in ascending order.
    """
    tasks: List[asyncio.Task] = [task_wait_random(max_delay) for _ in range(n)]
    all_delays: List[float] = [await task for task in asyncio.as_completed(tasks)]
    return all_delays
