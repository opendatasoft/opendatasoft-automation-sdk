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

from opendatasoft_automation.models.http_datasource1_headers import HTTPDatasource1Headers

class TestHTTPDatasource1Headers(unittest.TestCase):
    """HTTPDatasource1Headers unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> HTTPDatasource1Headers:
        """Test HTTPDatasource1Headers
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `HTTPDatasource1Headers`
        """
        model = HTTPDatasource1Headers()
        if include_optional:
            return HTTPDatasource1Headers(
                name = '',
                value = ''
            )
        else:
            return HTTPDatasource1Headers(
        )
        """

    def testHTTPDatasource1Headers(self):
        """Test HTTPDatasource1Headers"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
