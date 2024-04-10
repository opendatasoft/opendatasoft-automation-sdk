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

from openapi_client.models.amazon_s3_datasource_all_of_connection import AmazonS3DatasourceAllOfConnection

class TestAmazonS3DatasourceAllOfConnection(unittest.TestCase):
    """AmazonS3DatasourceAllOfConnection unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AmazonS3DatasourceAllOfConnection:
        """Test AmazonS3DatasourceAllOfConnection
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AmazonS3DatasourceAllOfConnection`
        """
        model = AmazonS3DatasourceAllOfConnection()
        if include_optional:
            return AmazonS3DatasourceAllOfConnection(
                uid = ''
            )
        else:
            return AmazonS3DatasourceAllOfConnection(
                uid = '',
        )
        """

    def testAmazonS3DatasourceAllOfConnection(self):
        """Test AmazonS3DatasourceAllOfConnection"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
