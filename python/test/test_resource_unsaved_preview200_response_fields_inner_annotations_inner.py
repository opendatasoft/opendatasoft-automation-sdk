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

from openapi_client.models.resource_unsaved_preview200_response_fields_inner_annotations_inner import ResourceUnsavedPreview200ResponseFieldsInnerAnnotationsInner

class TestResourceUnsavedPreview200ResponseFieldsInnerAnnotationsInner(unittest.TestCase):
    """ResourceUnsavedPreview200ResponseFieldsInnerAnnotationsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ResourceUnsavedPreview200ResponseFieldsInnerAnnotationsInner:
        """Test ResourceUnsavedPreview200ResponseFieldsInnerAnnotationsInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ResourceUnsavedPreview200ResponseFieldsInnerAnnotationsInner`
        """
        model = ResourceUnsavedPreview200ResponseFieldsInnerAnnotationsInner()
        if include_optional:
            return ResourceUnsavedPreview200ResponseFieldsInnerAnnotationsInner(
                name = '',
                args = [
                    ''
                    ]
            )
        else:
            return ResourceUnsavedPreview200ResponseFieldsInnerAnnotationsInner(
                name = '',
        )
        """

    def testResourceUnsavedPreview200ResponseFieldsInnerAnnotationsInner(self):
        """Test ResourceUnsavedPreview200ResponseFieldsInnerAnnotationsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()