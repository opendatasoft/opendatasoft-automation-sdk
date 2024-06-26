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

from opendatasoft_automation.models.httpo_auth2_auth import HTTPOAuth2Auth

class TestHTTPOAuth2Auth(unittest.TestCase):
    """HTTPOAuth2Auth unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> HTTPOAuth2Auth:
        """Test HTTPOAuth2Auth
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `HTTPOAuth2Auth`
        """
        model = HTTPOAuth2Auth()
        if include_optional:
            return HTTPOAuth2Auth(
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
            return HTTPOAuth2Auth(
                client_id = '',
                client_secret = '',
                scope = '',
                token_endpoint = '',
                grant_type = 'password',
        )
        """

    def testHTTPOAuth2Auth(self):
        """Test HTTPOAuth2Auth"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
