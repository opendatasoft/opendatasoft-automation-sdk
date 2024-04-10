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

from openapi_client.models.base_metadata_template import BaseMetadataTemplate

class TestBaseMetadataTemplate(unittest.TestCase):
    """BaseMetadataTemplate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BaseMetadataTemplate:
        """Test BaseMetadataTemplate
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BaseMetadataTemplate`
        """
        model = BaseMetadataTemplate()
        if include_optional:
            return BaseMetadataTemplate(
                name = 'my-custom-template',
                title = 'My custom template',
                is_active = True,
                is_always_active = False,
                is_system = False,
                var_schema = [
                    openapi_client.models.metadata_template_field.MetadataTemplateField(
                        name = 'my-custom-field', 
                        type = 'text', 
                        label = 'My custom field', 
                        help_text = '', 
                        is_hidden = False, 
                        self_suggest = False, 
                        is_filter = False, 
                        i18n = False, 
                        suggest_url = '', 
                        choices = [
                            ''
                            ], 
                        labels = {
                            'key' : {
                                'key' : ''
                                }
                            }, 
                        requirement_level = 'optional', )
                    ],
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                created_by = openapi_client.models.related_user.Related user(
                    username = 'louise.data', ),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_by = openapi_client.models.related_user.Related user(
                    username = 'louise.data', )
            )
        else:
            return BaseMetadataTemplate(
                name = 'my-custom-template',
                title = 'My custom template',
                is_active = True,
                var_schema = [
                    openapi_client.models.metadata_template_field.MetadataTemplateField(
                        name = 'my-custom-field', 
                        type = 'text', 
                        label = 'My custom field', 
                        help_text = '', 
                        is_hidden = False, 
                        self_suggest = False, 
                        is_filter = False, 
                        i18n = False, 
                        suggest_url = '', 
                        choices = [
                            ''
                            ], 
                        labels = {
                            'key' : {
                                'key' : ''
                                }
                            }, 
                        requirement_level = 'optional', )
                    ],
        )
        """

    def testBaseMetadataTemplate(self):
        """Test BaseMetadataTemplate"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
