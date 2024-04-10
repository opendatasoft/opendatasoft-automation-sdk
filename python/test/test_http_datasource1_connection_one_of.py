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

from openapi_client.models.http_datasource1_connection_one_of import HTTPDatasource1ConnectionOneOf

class TestHTTPDatasource1ConnectionOneOf(unittest.TestCase):
    """HTTPDatasource1ConnectionOneOf unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> HTTPDatasource1ConnectionOneOf:
        """Test HTTPDatasource1ConnectionOneOf
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `HTTPDatasource1ConnectionOneOf`
        """
        model = HTTPDatasource1ConnectionOneOf()
        if include_optional:
            return HTTPDatasource1ConnectionOneOf(
                uid = ''
            )
        else:
            return HTTPDatasource1ConnectionOneOf(
                uid = '',
        )
        """

    def testHTTPDatasource1ConnectionOneOf(self):
        """Test HTTPDatasource1ConnectionOneOf"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
