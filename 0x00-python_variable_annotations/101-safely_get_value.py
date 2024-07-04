#!/usr/bin/env python3
"""  This module contains the function safely_get_value """

from typing import Union, Any, Mapping, Optional, TypeVar

T = TypeVar('T')


def safely_get_value(
        dct: Mapping, key: Any,
        default: Optional[T] = None
        ) -> Union[Any, T]:
    """ Returns dict val or None """
    if key in dct:
        return dct[key]
    else:
        return default
