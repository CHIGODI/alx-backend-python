#!/usr/bin/env python3
""" This module contains a function t0_kv """

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple where the second element is the square
    of the input value
    """
    return (k, float(v) ** 2)
