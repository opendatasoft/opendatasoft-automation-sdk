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

from openapi_client.models.publish_dataset200_response import PublishDataset200Response

class TestPublishDataset200Response(unittest.TestCase):
    """PublishDataset200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PublishDataset200Response:
        """Test PublishDataset200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PublishDataset200Response`
        """
        model = PublishDataset200Response()
        if include_optional:
            return PublishDataset200Response(
                detail = ''
            )
        else:
            return PublishDataset200Response(
                detail = '',
        )
        """

    def testPublishDataset200Response(self):
        """Test PublishDataset200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()