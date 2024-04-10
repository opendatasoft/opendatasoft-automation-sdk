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

from openapi_client.models.ckan_harvester import CKANHarvester

class TestCKANHarvester(unittest.TestCase):
    """CKANHarvester unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CKANHarvester:
        """Test CKANHarvester
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CKANHarvester`
        """
        model = CKANHarvester()
        if include_optional:
            return CKANHarvester(
                url = 'https://www.hri.fi/api/3',
                limit = 56,
                offset = 56,
                sort = 'relevance desc'',
                api_key = '',
                group = 'education'',
                language = '',
                query = '',
                download_resources = True,
                metadata_only = True
            )
        else:
            return CKANHarvester(
                url = 'https://www.hri.fi/api/3',
        )
        """

    def testCKANHarvester(self):
        """Test CKANHarvester"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
