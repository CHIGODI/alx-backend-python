#!/usr/bin/env python3
""" """
from parameterized import parameterized
from client import GithubOrgClient
import unittest
from unittest.mock import patch, Mock
from typing import Mapping


class TestGithubOrgClient(unittest.TestCase):
    """ """
    @parameterized.expand([
        ('google', {}),
        ('abc', {})
    ])
    @patch('utils.requests.get')
    def test_org(self, org_name: str,
                 expected: Mapping,
                 mock_get) -> None:
        """Testing GithubOrgClient class org method"""
        org = GithubOrgClient(org_name)
        mock_response = Mock()
        mock_response.json.return_value = expected

        mock_get.return_value = mock_response
        result = org.org

        self.assertEqual(result, expected)
        mock_get.assert_called_once()
