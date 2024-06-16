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

from opendatasoft_automation.models.sharepoint_connection import SharepointConnection

class TestSharepointConnection(unittest.TestCase):
    """SharepointConnection unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SharepointConnection:
        """Test SharepointConnection
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SharepointConnection`
        """
        model = SharepointConnection()
        if include_optional:
            return SharepointConnection(
                auth = {"type":"oidc","grant_type":"authorization_code","claims":{}}
            )
        else:
            return SharepointConnection(
        )
        """

    def testSharepointConnection(self):
        """Test SharepointConnection"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
