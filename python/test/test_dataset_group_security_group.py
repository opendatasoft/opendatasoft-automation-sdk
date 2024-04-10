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

from openapi_client.models.dataset_group_security_group import DatasetGroupSecurityGroup

class TestDatasetGroupSecurityGroup(unittest.TestCase):
    """DatasetGroupSecurityGroup unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DatasetGroupSecurityGroup:
        """Test DatasetGroupSecurityGroup
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DatasetGroupSecurityGroup`
        """
        model = DatasetGroupSecurityGroup()
        if include_optional:
            return DatasetGroupSecurityGroup(
                uid = 'content_designers'
            )
        else:
            return DatasetGroupSecurityGroup(
                uid = 'content_designers',
        )
        """

    def testDatasetGroupSecurityGroup(self):
        """Test DatasetGroupSecurityGroup"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
