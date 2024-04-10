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

from openapi_client.models.resource import Resource

class TestResource(unittest.TestCase):
    """Resource unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Resource:
        """Test Resource
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Resource`
        """
        model = Resource()
        if include_optional:
            return Resource(
                uid = '0',
                type = '0',
                title = '0',
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                params = None,
                datasource = {"type":"http","connection":{"type":"http","url":"https://my-server.com","auth":null},"headers":[{"name":"header-name","value":"header-value"}],"relative_url":"/fromages.csv"}
            )
        else:
            return Resource(
                type = '0',
                title = '0',
                datasource = {"type":"http","connection":{"type":"http","url":"https://my-server.com","auth":null},"headers":[{"name":"header-name","value":"header-value"}],"relative_url":"/fromages.csv"},
        )
        """

    def testResource(self):
        """Test Resource"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
