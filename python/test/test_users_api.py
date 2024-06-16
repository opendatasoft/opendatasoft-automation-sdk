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

from opendatasoft_automation.api.users_api import UsersApi


class TestUsersApi(unittest.TestCase):
    """UsersApi unit test stubs"""

    def setUp(self) -> None:
        self.api = UsersApi()

    def tearDown(self) -> None:
        pass

    def test_delete_user(self) -> None:
        """Test case for delete_user

        Delete user
        """
        pass

    def test_get_user(self) -> None:
        """Test case for get_user

        Retrieve user
        """
        pass

    def test_get_users(self) -> None:
        """Test case for get_users

        List users
        """
        pass

    def test_invite_users(self) -> None:
        """Test case for invite_users

        Invite users
        """
        pass

    def test_provision_users(self) -> None:
        """Test case for provision_users

        Provision users
        """
        pass

    def test_update_user(self) -> None:
        """Test case for update_user

        Update user
        """
        pass

    def test_users_export(self) -> None:
        """Test case for users_export

        Export users
        """
        pass


if __name__ == '__main__':
    unittest.main()
