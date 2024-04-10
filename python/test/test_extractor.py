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

from openapi_client.models.extractor import Extractor

class TestExtractor(unittest.TestCase):
    """Extractor unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Extractor:
        """Test Extractor
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Extractor`
        """
        model = Extractor()
        if include_optional:
            return Extractor(
                type = 'jsonfile',
                label = 'JSON File',
                parameters = [
                    [{"type":"boolean","is_mandatory":false,"name":"extract_filename","label":"Extract filename","description":"Extract the filename in a field"},{"type":"string","is_mandatory":false,"name":"json_root","label":"JSON root","description":"Path to the JSON array that contains the objects that will become the dataset records"},{"type":"string","is_mandatory":false,"name":"json_object","label":"JSON object","description":"Relative path to the JSON object to extract"}]
                    ]
            )
        else:
            return Extractor(
                type = 'jsonfile',
                label = 'JSON File',
                parameters = [
                    [{"type":"boolean","is_mandatory":false,"name":"extract_filename","label":"Extract filename","description":"Extract the filename in a field"},{"type":"string","is_mandatory":false,"name":"json_root","label":"JSON root","description":"Path to the JSON array that contains the objects that will become the dataset records"},{"type":"string","is_mandatory":false,"name":"json_object","label":"JSON object","description":"Relative path to the JSON object to extract"}]
                    ],
        )
        """

    def testExtractor(self):
        """Test Extractor"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
