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

from opendatasoft_automation.models.oidc_auth import OIDCAuth

class TestOIDCAuth(unittest.TestCase):
    """OIDCAuth unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OIDCAuth:
        """Test OIDCAuth
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OIDCAuth`
        """
        model = OIDCAuth()
        if include_optional:
            return OIDCAuth(
                client_id = '',
                client_secret = '',
                scope = '',
                token_endpoint = '',
                grant_type = 'authorization_code',
                code = '',
                claims = None
            )
        else:
            return OIDCAuth(
                client_id = '',
                client_secret = '',
                scope = '',
                token_endpoint = '',
                grant_type = 'authorization_code',
        )
        """

    def testOIDCAuth(self):
        """Test OIDCAuth"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
