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

from openapi_client.models.google_drive_connection import GoogleDriveConnection

class TestGoogleDriveConnection(unittest.TestCase):
    """GoogleDriveConnection unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GoogleDriveConnection:
        """Test GoogleDriveConnection
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GoogleDriveConnection`
        """
        model = GoogleDriveConnection()
        if include_optional:
            return GoogleDriveConnection(
                auth = {"type":"oidc","grant_type":"authorization_code","claims":{}}
            )
        else:
            return GoogleDriveConnection(
        )
        """

    def testGoogleDriveConnection(self):
        """Test GoogleDriveConnection"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()