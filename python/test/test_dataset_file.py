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

from opendatasoft_automation.models.dataset_file import DatasetFile

class TestDatasetFile(unittest.TestCase):
    """DatasetFile unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DatasetFile:
        """Test DatasetFile
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DatasetFile`
        """
        model = DatasetFile()
        if include_optional:
            return DatasetFile(
                uid = 'fromages.csv',
                filename = 'fromages.csv',
                mimetype = 'text/csv',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return DatasetFile(
        )
        """

    def testDatasetFile(self):
        """Test DatasetFile"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
