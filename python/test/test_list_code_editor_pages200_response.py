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

from openapi_client.models.list_code_editor_pages200_response import ListCodeEditorPages200Response

class TestListCodeEditorPages200Response(unittest.TestCase):
    """ListCodeEditorPages200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ListCodeEditorPages200Response:
        """Test ListCodeEditorPages200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListCodeEditorPages200Response`
        """
        model = ListCodeEditorPages200Response()
        if include_optional:
            return ListCodeEditorPages200Response(
                total_count = '18',
                next = '',
                previous = '',
                results = [
                    openapi_client.models.code_editor_page_schema.Code editor page schema(
                        slug = 'hello_world', 
                        title = {"en":"Hello world"}, 
                        description = 'A page saying hello', 
                        content = {"html":{"en":"<p>\n    Hello world\n</p>"},"css":{"en":""}}, 
                        template = 'custom.html', 
                        tags = ["My tag"], 
                        has_subdomain_copies = False, 
                        is_pushed_by_parent = False, 
                        is_restricted = True, 
                        is_archived = False, 
                        created_by = openapi_client.models.related_user.Related user(
                            username = 'louise.data', ), 
                        updated_by = openapi_client.models.related_user.Related user(
                            username = 'louise.data', ), 
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ]
            )
        else:
            return ListCodeEditorPages200Response(
        )
        """

    def testListCodeEditorPages200Response(self):
        """Test ListCodeEditorPages200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
