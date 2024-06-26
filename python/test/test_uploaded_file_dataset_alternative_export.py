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

from opendatasoft_automation.models.uploaded_file_dataset_alternative_export import UploadedFileDatasetAlternativeExport

class TestUploadedFileDatasetAlternativeExport(unittest.TestCase):
    """UploadedFileDatasetAlternativeExport unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UploadedFileDatasetAlternativeExport:
        """Test UploadedFileDatasetAlternativeExport
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UploadedFileDatasetAlternativeExport`
        """
        model = UploadedFileDatasetAlternativeExport()
        if include_optional:
            return UploadedFileDatasetAlternativeExport(
                filename = 'fromages.csv'
            )
        else:
            return UploadedFileDatasetAlternativeExport(
        )
        """

    def testUploadedFileDatasetAlternativeExport(self):
        """Test UploadedFileDatasetAlternativeExport"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
