#!/usr/bin/env python3
""" This module contains the function wait_random"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Wait for a random delay between 0 and max_delay seconds
    and return the actual delay."""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
