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

from opendatasoft_automation.api.datasets_api import DatasetsApi


class TestDatasetsApi(unittest.TestCase):
    """DatasetsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = DatasetsApi()

    def tearDown(self) -> None:
        pass

    def test_abort_dataset(self) -> None:
        """Test case for abort_dataset

        Abort dataset publishing
        """
        pass

    def test_copy_dataset(self) -> None:
        """Test case for copy_dataset

        Copy dataset
        """
        pass

    def test_create_dataset(self) -> None:
        """Test case for create_dataset

        Create dataset
        """
        pass

    def test_delete_dataset(self) -> None:
        """Test case for delete_dataset

        Delete Dataset
        """
        pass

    def test_get_dataset_status(self) -> None:
        """Test case for get_dataset_status

        Retrieve dataset status
        """
        pass

    def test_list_datasets(self) -> None:
        """Test case for list_datasets

        List datasets
        """
        pass

    def test_publish_dataset(self) -> None:
        """Test case for publish_dataset

        Publish dataset
        """
        pass

    def test_publish_dataset_metadata(self) -> None:
        """Test case for publish_dataset_metadata

        Publish dataset metadata
        """
        pass

    def test_retrieve_dataset(self) -> None:
        """Test case for retrieve_dataset

        Retrieve Dataset
        """
        pass

    def test_unpublish_dataset(self) -> None:
        """Test case for unpublish_dataset

        Unpublish dataset
        """
        pass

    def test_update_dataset(self) -> None:
        """Test case for update_dataset

        Update Dataset
        """
        pass


if __name__ == '__main__':
    unittest.main()
