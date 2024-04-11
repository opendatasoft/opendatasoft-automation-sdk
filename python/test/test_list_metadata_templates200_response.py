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

from openapi_client.models.list_metadata_templates200_response import ListMetadataTemplates200Response

class TestListMetadataTemplates200Response(unittest.TestCase):
    """ListMetadataTemplates200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ListMetadataTemplates200Response:
        """Test ListMetadataTemplates200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListMetadataTemplates200Response`
        """
        model = ListMetadataTemplates200Response()
        if include_optional:
            return ListMetadataTemplates200Response(
                total_count = 56,
                next = '',
                previous = '',
                results = [
                    openapi_client.models.metadata_template_schema.Metadata template schema()
                    ]
            )
        else:
            return ListMetadataTemplates200Response(
        )
        """

    def testListMetadataTemplates200Response(self):
        """Test ListMetadataTemplates200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()