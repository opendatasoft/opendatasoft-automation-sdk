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

from openapi_client.models.extractor_parameters_inner import ExtractorParametersInner

class TestExtractorParametersInner(unittest.TestCase):
    """ExtractorParametersInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ExtractorParametersInner:
        """Test ExtractorParametersInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ExtractorParametersInner`
        """
        model = ExtractorParametersInner()
        if include_optional:
            return ExtractorParametersInner(
                type = '',
                is_mandatory = True,
                name = '',
                label = '',
                default = '',
                description = '',
                hidden = True,
                trim = '',
                choices = [
                    ''
                    ],
                can_create_field = True,
                impacts_guessed_parameters = True
            )
        else:
            return ExtractorParametersInner(
                type = '',
                is_mandatory = True,
                name = '',
        )
        """

    def testExtractorParametersInner(self):
        """Test ExtractorParametersInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
