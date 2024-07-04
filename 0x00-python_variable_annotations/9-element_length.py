#!/usr/bin/env python3
""" This module contains the function element_length """

from typing import Iterable, Tuple, List, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ Returns iterator """
    return [(i, len(i)) for i in lst]
