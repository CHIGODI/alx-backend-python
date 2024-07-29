#!/usr/bin/env python3
"""
Test suite for access_nested_map function
"""
from parameterized import parameterized
import unittest
from unittest import mock
from utils import access_nested_map, get_json, memoize
from typing import Any, Sequence, Mapping
from unittest.mock import Mock, patch, PropertyMock


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
        """Test acccess_nested with invalid inputs"""
        with self.assertRaises(expected_exception):
            access_nested_map(nested_map, path)

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('utils.requests.get')
    def test_get_json(self, url: str, expected: Mapping, mock_get) -> None:
        """Test get_json with various inputs"""

        mock_response = Mock()
        mock_response.json.return_value = expected

        mock_get.return_value = mock_response
        result = get_json(url)

        self.assertEqual(result, expected)
        mock_get.assert_called_once_with(url)


class TestMemoize(unittest.TestCase):
    """Testing memoize"""
    def test_memoize(self):
        """Testing memoize"""
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        instance = TestClass()

        with patch.object(instance, 'a_method',
                          return_value=42) as mock_a_method:
            result1 = instance.a_property
            result2 = instance.a_property

            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)

            mock_a_method.assert_called_once()
