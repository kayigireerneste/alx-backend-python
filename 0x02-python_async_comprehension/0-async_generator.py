#!/usr/bin/env python3
"""
Module for creating an asynchronous generator that yields random float numbers.
"""
import asyncio
import random
from typing import Generator
async def async_generator() -> Generator[float, None, None]:
    """
    Asynchronous generator that yields a random float between 0 and 10.
    The coroutine will loop 10 times, and in each iteration, it will
    asynchronously wait for 1 second and then yield a random float.
    Yields:
        float: A random float between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
