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

from openapi_client.models.ftpcsv_harvester import FTPCSVHarvester

class TestFTPCSVHarvester(unittest.TestCase):
    """FTPCSVHarvester unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FTPCSVHarvester:
        """Test FTPCSVHarvester
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FTPCSVHarvester`
        """
        model = FTPCSVHarvester()
        if include_optional:
            return FTPCSVHarvester(
                host = 'your-ftp-service.com',
                user = 'username',
                password = 'secret_password',
                directory = '',
                metadata_file = 'meta_filename.csv',
                metadata_join_key = 'source_dataset',
                download_resources = True,
                metadata_only = True
            )
        else:
            return FTPCSVHarvester(
                host = 'your-ftp-service.com',
                user = 'username',
                password = 'secret_password',
                metadata_file = 'meta_filename.csv',
        )
        """

    def testFTPCSVHarvester(self):
        """Test FTPCSVHarvester"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()