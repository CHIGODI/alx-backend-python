#!/usr/bin/env python3
"""
Measure Runtime Module
"""

import asyncio
from typing import List
from time import time
from asyncio import run

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measures the runtime of running async_comprehension four
    times in parallel.
    """
    start_time = time()

    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )

    end_time = time()
    runtime = end_time - start_time
    return runtime
