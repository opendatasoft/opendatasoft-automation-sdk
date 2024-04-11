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

from openapi_client.models.o_auth2_auth import OAuth2Auth

class TestOAuth2Auth(unittest.TestCase):
    """OAuth2Auth unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OAuth2Auth:
        """Test OAuth2Auth
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OAuth2Auth`
        """
        model = OAuth2Auth()
        if include_optional:
            return OAuth2Auth(
                client_id = '',
                client_secret = '',
                scope = '',
                token_endpoint = '',
                grant_type = 'password',
                username = '',
                password = '',
                code = ''
            )
        else:
            return OAuth2Auth(
                client_id = '',
                client_secret = '',
                scope = '',
                token_endpoint = '',
                grant_type = 'password',
        )
        """

    def testOAuth2Auth(self):
        """Test OAuth2Auth"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()