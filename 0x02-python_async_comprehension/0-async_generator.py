#!/usr/bin/env python3
"""
This module provides an asyncchronous generator function that
yields a random float between 0 and 10 after a second delay
for a total of 10 iterations.
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Asynchronous generator function that yiels a random float
    between 0 and 10 after a one second delay for a total of 10 iterations.

    Returns:
    Generator: Asyncchronous generator object that can be used in  an awaiting context.
    """
    for _ in range(10):
        await asnycio.sleep(1)
        yield random.random() * 10
