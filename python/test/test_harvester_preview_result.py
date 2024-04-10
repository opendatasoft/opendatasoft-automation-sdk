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

from openapi_client.models.harvester_preview_result import HarvesterPreviewResult

class TestHarvesterPreviewResult(unittest.TestCase):
    """HarvesterPreviewResult unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> HarvesterPreviewResult:
        """Test HarvesterPreviewResult
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `HarvesterPreviewResult`
        """
        model = HarvesterPreviewResult()
        if include_optional:
            return HarvesterPreviewResult(
                total_count = 42,
                results = [
                    openapi_client.models.harvester_preview_result_results_inner.HarvesterPreviewResult_results_inner(
                        id = 'georef-united-states-of-america-zc-point', 
                        title = 'US Zip Codes Points- United States of America', 
                        description = 'Contains most USPS zip codes (lat/long).', )
                    ]
            )
        else:
            return HarvesterPreviewResult(
                total_count = 42,
                results = [
                    openapi_client.models.harvester_preview_result_results_inner.HarvesterPreviewResult_results_inner(
                        id = 'georef-united-states-of-america-zc-point', 
                        title = 'US Zip Codes Points- United States of America', 
                        description = 'Contains most USPS zip codes (lat/long).', )
                    ],
        )
        """

    def testHarvesterPreviewResult(self):
        """Test HarvesterPreviewResult"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
