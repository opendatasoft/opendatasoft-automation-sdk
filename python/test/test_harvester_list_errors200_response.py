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

from openapi_client.models.harvester_list_errors200_response import HarvesterListErrors200Response

class TestHarvesterListErrors200Response(unittest.TestCase):
    """HarvesterListErrors200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> HarvesterListErrors200Response:
        """Test HarvesterListErrors200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `HarvesterListErrors200Response`
        """
        model = HarvesterListErrors200Response()
        if include_optional:
            return HarvesterListErrors200Response(
                harvester = 'A fatal error occured. Please check the harvester configuration.',
                resources = {"remote_resource_id":"Could not harvest the dataset."}
            )
        else:
            return HarvesterListErrors200Response(
                harvester = 'A fatal error occured. Please check the harvester configuration.',
                resources = {"remote_resource_id":"Could not harvest the dataset."},
        )
        """

    def testHarvesterListErrors200Response(self):
        """Test HarvesterListErrors200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()