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

from opendatasoft_automation.models.dataset_security import DatasetSecurity

class TestDatasetSecurity(unittest.TestCase):
    """DatasetSecurity unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DatasetSecurity:
        """Test DatasetSecurity
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DatasetSecurity`
        """
        model = DatasetSecurity()
        if include_optional:
            return DatasetSecurity(
                is_data_visible = True,
                visible_fields = ["year","coty_code"],
                filter_query = 'year!=2022',
                api_calls_quota = opendatasoft_automation.models.dataset_security_api_calls_quota.DatasetSecurity_api_calls_quota(
                    unit = 'month', 
                    limit = 12000, )
            )
        else:
            return DatasetSecurity(
        )
        """

    def testDatasetSecurity(self):
        """Test DatasetSecurity"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
