#!/usr/bin/env python3
"""
Module for basic asynchronous coroutine.
"""

import random
import asyncio
from typing import Union


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay and returns the delay.

    Args:
        max_delay (int): Maximum number of seconds to wait. Default is 10.

    Returns:
        float: The actual time delayed in seconds.
    """
    delay_time = random.uniform(0, max_delay)
    await asyncio.sleep(delay_time)
    return delay_time

