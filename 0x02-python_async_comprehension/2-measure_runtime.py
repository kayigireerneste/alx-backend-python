#!/usr/bin/env python3
"""
Module for measuring the total runtime of executing async_comprehension four times in parallel.
"""

import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension

async def measure_runtime() -> float:
    """
    Executes async_comprehension four times in parallel and measures the total runtime.
    Returns:
        float: Total time taken to execute async_comprehension four times in parallel.
    """
    start_time = time.perf_counter()  # Record start time
    await asyncio.gather(
        async_comprehension(), async_comprehension(),
        async_comprehension(), async_comprehension()
    )  # Execute async_comprehension four times in parallel
    total_runtime = time.perf_counter() - start_time  # Calculate total runtime
    return total_runtime
