#!/usr/bin/env python3
"""
Test suite for access_nested_map function
"""
from parameterized import parameterized
import unittest
from utils import access_nested_map
from typing import Any, Sequence, Mapping


class TestAccessNestedMap(unittest.TestCase):
    """Test case for the access_nested_map function"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self,
                               nested_map: Mapping,
                               path: Sequence,
                               expected: Any) -> None:
        """Test access_nested_map with various inputs"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ('a'), KeyError),
        ({"a": 1}, ('a', 'b'), KeyError)
    ])
    def test_access_nested_map_exception(self,
                                         nested_map: Mapping,
                                         path: Sequence,
                                         expected_exception: Any) -> None:
        """ """
        with self.assertRaises(expected_exception):
            access_nested_map(nested_map, path)
