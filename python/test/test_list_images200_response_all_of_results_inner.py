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

from opendatasoft_automation.models.list_images200_response_all_of_results_inner import ListImages200ResponseAllOfResultsInner

class TestListImages200ResponseAllOfResultsInner(unittest.TestCase):
    """ListImages200ResponseAllOfResultsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ListImages200ResponseAllOfResultsInner:
        """Test ListImages200ResponseAllOfResultsInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListImages200ResponseAllOfResultsInner`
        """
        model = ListImages200ResponseAllOfResultsInner()
        if include_optional:
            return ListImages200ResponseAllOfResultsInner(
                url = '/assets/theme_image/Acronym-Turquoise.svg'
            )
        else:
            return ListImages200ResponseAllOfResultsInner(
        )
        """

    def testListImages200ResponseAllOfResultsInner(self):
        """Test ListImages200ResponseAllOfResultsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
