#!/usr/bin/env python3
"""
Module for measuring the execution time of an asynchronous coroutine.
"""

import asyncio
import time
from typing import Union
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the total runtime for executing wait_n and calculate the average time per call.

    Args:
        n (int): Number of calls to wait_n.
        max_delay (int): Maximum delay for each call of wait_random.

    Returns:
        float: Average time taken for each wait_n call.
    """
    start_time = time.time()  # Record the start time
    asyncio.run(wait_n(n, max_delay))  # Run the wait_n coroutine
    end_time = time.time()  # Record the end time

    total_time = end_time - start_time  # Calculate the total elapsed time
    return total_time / n  # Return the average time per call

