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

from opendatasoft_automation.models.dataset_feedback_values import DatasetFeedbackValues

class TestDatasetFeedbackValues(unittest.TestCase):
    """DatasetFeedbackValues unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DatasetFeedbackValues:
        """Test DatasetFeedbackValues
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DatasetFeedbackValues`
        """
        model = DatasetFeedbackValues()
        if include_optional:
            return DatasetFeedbackValues(
                value = '',
                type = 'text'
            )
        else:
            return DatasetFeedbackValues(
        )
        """

    def testDatasetFeedbackValues(self):
        """Test DatasetFeedbackValues"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
