wait_random = __import__('0-basic_async_syntax').wait_random
import asyncio


def task_wait_random(max_delay):
    """
    Regular function that creates and returns an asyncio.Task
    that runs wait_random(max_delay).
    """
    return asyncio.create_task(wait_random(max_delay))
