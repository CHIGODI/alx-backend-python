#!/usr/bin/env python3
"""This module contains the zoom_array function """

from typing import Tuple, Iterable, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """ returns tupple """
    zoomed_in: List = list(
        item for item in lst
        for i in range(factor)
    )
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
