# coding: utf-8

"""
    Opendatasoft's Automation API Documentation

    Opendatasoft REST API to manage your portal and its catalog

    The version of the OpenAPI document: 1.0
    Contact: support@opendatasoft.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from opendatasoft_automation.api.api_keys_api import APIKeysApi


class TestAPIKeysApi(unittest.TestCase):
    """APIKeysApi unit test stubs"""

    def setUp(self) -> None:
        self.api = APIKeysApi()

    def tearDown(self) -> None:
        pass

    def test_get_apikey(self) -> None:
        """Test case for get_apikey

        Retrieve an API key
        """
        pass

    def test_get_apikeys(self) -> None:
        """Test case for get_apikeys

        List API keys
        """
        pass

    def test_post_apikeys(self) -> None:
        """Test case for post_apikeys

        Create an API key
        """
        pass

    def test_post_apikeys_apikey_uid_revoke(self) -> None:
        """Test case for post_apikeys_apikey_uid_revoke

        Revoke an API key
        """
        pass

    def test_put_apikeys_apikey_uid(self) -> None:
        """Test case for put_apikeys_apikey_uid

        Update an API key
        """
        pass

    def test_search_apikey(self) -> None:
        """Test case for search_apikey

        Search an API key
        """
        pass


if __name__ == '__main__':
    unittest.main()
