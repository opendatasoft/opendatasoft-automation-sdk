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

from openapi_client.models.get_dataset_status200_response import GetDatasetStatus200Response

class TestGetDatasetStatus200Response(unittest.TestCase):
    """GetDatasetStatus200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetDatasetStatus200Response:
        """Test GetDatasetStatus200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetDatasetStatus200Response`
        """
        model = GetDatasetStatus200Response()
        if include_optional:
            return GetDatasetStatus200Response(
                status = 'idle',
                previous = 'idle',
                next = 'idle',
                since = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                is_published = True,
                message = '',
                records_errors = [],
                params = {}
            )
        else:
            return GetDatasetStatus200Response(
        )
        """

    def testGetDatasetStatus200Response(self):
        """Test GetDatasetStatus200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()