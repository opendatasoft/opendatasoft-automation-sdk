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

from openapi_client.models.publish_dataset400_response import PublishDataset400Response

class TestPublishDataset400Response(unittest.TestCase):
    """PublishDataset400Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PublishDataset400Response:
        """Test PublishDataset400Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PublishDataset400Response`
        """
        model = PublishDataset400Response()
        if include_optional:
            return PublishDataset400Response(
                error_code = 'invalid_dataset_status',
                message = '0'
            )
        else:
            return PublishDataset400Response(
                error_code = 'invalid_dataset_status',
                message = '0',
        )
        """

    def testPublishDataset400Response(self):
        """Test PublishDataset400Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()