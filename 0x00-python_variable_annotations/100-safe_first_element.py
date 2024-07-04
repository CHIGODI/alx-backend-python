#!/usr/bin/env python3
""" This module contains the function safe_first_element """

from typing import Sequence, Any, Optional


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """Returns the first element of a sequence if it exists, otherwise None"""
    if lst:
        return lst[0]
    else:
        return None
