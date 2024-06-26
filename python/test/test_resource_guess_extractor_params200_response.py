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

from opendatasoft_automation.models.resource_guess_extractor_params200_response import ResourceGuessExtractorParams200Response

class TestResourceGuessExtractorParams200Response(unittest.TestCase):
    """ResourceGuessExtractorParams200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ResourceGuessExtractorParams200Response:
        """Test ResourceGuessExtractorParams200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ResourceGuessExtractorParams200Response`
        """
        model = ResourceGuessExtractorParams200Response()
        if include_optional:
            return ResourceGuessExtractorParams200Response(
                extractor = 'csvfile',
                params = {"doublequote":true,"encoding":"utf-8","first_row_no":1,"headers_first_row":true,"separator":";"}
            )
        else:
            return ResourceGuessExtractorParams200Response(
        )
        """

    def testResourceGuessExtractorParams200Response(self):
        """Test ResourceGuessExtractorParams200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
