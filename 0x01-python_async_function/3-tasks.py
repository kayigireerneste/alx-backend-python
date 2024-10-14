#!/usr/bin/env python3
"""
Module for creating a task using wait_random coroutine.
"""

import asyncio
from typing import Union
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates an asyncio.Task for wait_random with the specified max_delay.

    Args:
        max_delay (int): Maximum delay for the wait_random coroutine.

    Returns:
        asyncio.Task: A task object that represents the wait_random coroutine.
    """
    task = asyncio.create_task(wait_random(max_delay))
    return task

