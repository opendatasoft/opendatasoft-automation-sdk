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

from openapi_client.models.google_drive_oidc_auth import GoogleDriveOIDCAuth

class TestGoogleDriveOIDCAuth(unittest.TestCase):
    """GoogleDriveOIDCAuth unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GoogleDriveOIDCAuth:
        """Test GoogleDriveOIDCAuth
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GoogleDriveOIDCAuth`
        """
        model = GoogleDriveOIDCAuth()
        if include_optional:
            return GoogleDriveOIDCAuth(
                nonce = '',
                grant_type = 'authorization_code',
                code = '',
                claims = openapi_client.models.claims.claims(),
                application_id = ''
            )
        else:
            return GoogleDriveOIDCAuth(
                nonce = '',
                grant_type = 'authorization_code',
                code = '',
                claims = openapi_client.models.claims.claims(),
                application_id = '',
        )
        """

    def testGoogleDriveOIDCAuth(self):
        """Test GoogleDriveOIDCAuth"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()