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

from openapi_client.models.resource_unsaved_preview_request import ResourceUnsavedPreviewRequest

class TestResourceUnsavedPreviewRequest(unittest.TestCase):
    """ResourceUnsavedPreviewRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ResourceUnsavedPreviewRequest:
        """Test ResourceUnsavedPreviewRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ResourceUnsavedPreviewRequest`
        """
        model = ResourceUnsavedPreviewRequest()
        if include_optional:
            return ResourceUnsavedPreviewRequest(
                datasource = {"type":"http","connection":{"type":"http","url":"https://my-server.com","auth":null},"headers":[{"name":"header-name","value":"header-value"}],"relative_url":"/fromages.csv"},
                type = 'csvfile',
                params = {"doublequote":true,"encoding":"utf-8","first_row_no":1,"headers_first_row":true,"separator":";"}
            )
        else:
            return ResourceUnsavedPreviewRequest(
                datasource = {"type":"http","connection":{"type":"http","url":"https://my-server.com","auth":null},"headers":[{"name":"header-name","value":"header-value"}],"relative_url":"/fromages.csv"},
                type = 'csvfile',
        )
        """

    def testResourceUnsavedPreviewRequest(self):
        """Test ResourceUnsavedPreviewRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
