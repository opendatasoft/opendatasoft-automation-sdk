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

from opendatasoft_automation.api.dataset_resources_api import DatasetResourcesApi


class TestDatasetResourcesApi(unittest.TestCase):
    """DatasetResourcesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = DatasetResourcesApi()

    def tearDown(self) -> None:
        pass

    def test_clean_resource_cache(self) -> None:
        """Test case for clean_resource_cache

        Clean cache of resource
        """
        pass

    def test_create_dataset_resource(self) -> None:
        """Test case for create_dataset_resource

        Create dataset resource
        """
        pass

    def test_delete_dataset_resource(self) -> None:
        """Test case for delete_dataset_resource

        Delete dataset resource
        """
        pass

    def test_delete_recover_data_resource(self) -> None:
        """Test case for delete_recover_data_resource

        Delete realtime recovered data
        """
        pass

    def test_disable_resource(self) -> None:
        """Test case for disable_resource

        Disable realtime resource
        """
        pass

    def test_download_dataset_resource_file(self) -> None:
        """Test case for download_dataset_resource_file

        Download dataset resource file
        """
        pass

    def test_enable_resource(self) -> None:
        """Test case for enable_resource

        Enable realtime resource
        """
        pass

    def test_guess_unsaved_resource_extractor_params(self) -> None:
        """Test case for guess_unsaved_resource_extractor_params

        Guess unsaved resource extractor parameters
        """
        pass

    def test_guess_unsaved_resource_extractors(self) -> None:
        """Test case for guess_unsaved_resource_extractors

        Guess unsaved resource extractors
        """
        pass

    def test_list_dataset_resources(self) -> None:
        """Test case for list_dataset_resources

        List dataset resources
        """
        pass

    def test_list_extractors(self) -> None:
        """Test case for list_extractors

        List extractors
        """
        pass

    def test_recover_resource(self) -> None:
        """Test case for recover_resource

        Recover realtime data
        """
        pass

    def test_resource_guess_extractor_params(self) -> None:
        """Test case for resource_guess_extractor_params

        Guess resource extractor parameters
        """
        pass

    def test_resource_guess_extractors(self) -> None:
        """Test case for resource_guess_extractors

        Guess resource extractors
        """
        pass

    def test_resource_preview(self) -> None:
        """Test case for resource_preview

        Preview resource records
        """
        pass

    def test_resource_renew_api_key(self) -> None:
        """Test case for resource_renew_api_key

        Renew realtime resource API key
        """
        pass

    def test_resource_unsaved_preview(self) -> None:
        """Test case for resource_unsaved_preview

        Preview unsaved resource records
        """
        pass

    def test_retrieve_dataset_resource(self) -> None:
        """Test case for retrieve_dataset_resource

        Retrieve dataset resource
        """
        pass

    def test_retrieve_dataset_resource_file(self) -> None:
        """Test case for retrieve_dataset_resource_file

        Retrieve dataset resource file
        """
        pass

    def test_update_dataset_resource(self) -> None:
        """Test case for update_dataset_resource

        Update dataset resource
        """
        pass

    def test_upload_resource_file(self) -> None:
        """Test case for upload_resource_file

        Upload resource file
        """
        pass


if __name__ == '__main__':
    unittest.main()
