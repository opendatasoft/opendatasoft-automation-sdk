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

from openapi_client.models.dataset_alternative_export import DatasetAlternativeExport

class TestDatasetAlternativeExport(unittest.TestCase):
    """DatasetAlternativeExport unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DatasetAlternativeExport:
        """Test DatasetAlternativeExport
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DatasetAlternativeExport`
        """
        model = DatasetAlternativeExport()
        if include_optional:
            return DatasetAlternativeExport(
                uid = 'ae_mm8lbn',
                title = 'Alternative export title',
                description = 'Alternative export description',
                mimetype = 'text/csv',
                type = 'url',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return DatasetAlternativeExport(
                title = 'Alternative export title',
                type = 'url',
        )
        """

    def testDatasetAlternativeExport(self):
        """Test DatasetAlternativeExport"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()