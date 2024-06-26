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

from opendatasoft_automation.api.dataset_versions_api import DatasetVersionsApi


class TestDatasetVersionsApi(unittest.TestCase):
    """DatasetVersionsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = DatasetVersionsApi()

    def tearDown(self) -> None:
        pass

    def test_list_dataset_versions(self) -> None:
        """Test case for list_dataset_versions

        List all versions
        """
        pass

    def test_restore_version(self) -> None:
        """Test case for restore_version

        Restore version
        """
        pass

    def test_retrieve_dataset_version(self) -> None:
        """Test case for retrieve_dataset_version

        Retrieve version
        """
        pass


if __name__ == '__main__':
    unittest.main()
