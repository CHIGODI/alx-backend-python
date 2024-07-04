#!/usr/bin/env python3
""" This module contains the fucntion sum_mixed_list """

from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ returns sum of numbers in list mxd_list """
    return sum(mxd_lst)
