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

from opendatasoft_automation.models.dataset_metadata_default import DatasetMetadataDefault

class TestDatasetMetadataDefault(unittest.TestCase):
    """DatasetMetadataDefault unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DatasetMetadataDefault:
        """Test DatasetMetadataDefault
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DatasetMetadataDefault`
        """
        model = DatasetMetadataDefault()
        if include_optional:
            return DatasetMetadataDefault(
                title = {"value":"Metadata value","remote_value":"Metadata value on the remote dataset, if there is one","override_remote_value":true},
                description = {"value":"Metadata value","remote_value":"Metadata value on the remote dataset, if there is one","override_remote_value":true},
                keyword = {"value":"Metadata value","remote_value":"Metadata value on the remote dataset, if there is one","override_remote_value":true},
                modified = {"value":"Metadata value","remote_value":"Metadata value on the remote dataset, if there is one","override_remote_value":true},
                modified_updates_on_metadata_change = {"value":"Metadata value","remote_value":"Metadata value on the remote dataset, if there is one","override_remote_value":true},
                modified_updates_on_data_change = {"value":"Metadata value","remote_value":"Metadata value on the remote dataset, if there is one","override_remote_value":true},
                geographic_reference = {"value":"Metadata value","remote_value":"Metadata value on the remote dataset, if there is one","override_remote_value":true},
                geographic_reference_auto = {"value":"Metadata value","remote_value":"Metadata value on the remote dataset, if there is one","override_remote_value":true},
                language = {"value":"Metadata value","remote_value":"Metadata value on the remote dataset, if there is one","override_remote_value":true},
                timezone = {"value":"Metadata value","remote_value":"Metadata value on the remote dataset, if there is one","override_remote_value":true},
                publisher = {"value":"Metadata value","remote_value":"Metadata value on the remote dataset, if there is one","override_remote_value":true},
                references = {"value":"Metadata value","remote_value":"Metadata value on the remote dataset, if there is one","override_remote_value":true},
                attributions = {"value":"Metadata value","remote_value":"Metadata value on the remote dataset, if there is one","override_remote_value":true}
            )
        else:
            return DatasetMetadataDefault(
                title = {"value":"Metadata value","remote_value":"Metadata value on the remote dataset, if there is one","override_remote_value":true},
                modified = {"value":"Metadata value","remote_value":"Metadata value on the remote dataset, if there is one","override_remote_value":true},
                language = {"value":"Metadata value","remote_value":"Metadata value on the remote dataset, if there is one","override_remote_value":true},
        )
        """

    def testDatasetMetadataDefault(self):
        """Test DatasetMetadataDefault"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
