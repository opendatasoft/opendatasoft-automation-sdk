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

from opendatasoft_automation.models.studio_page_contents_inner import StudioPageContentsInner

class TestStudioPageContentsInner(unittest.TestCase):
    """StudioPageContentsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> StudioPageContentsInner:
        """Test StudioPageContentsInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `StudioPageContentsInner`
        """
        model = StudioPageContentsInner()
        if include_optional:
            return StudioPageContentsInner(
                version_name = 'draft',
                title = 'My Page',
                description = 'A page saying hello',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_by = opendatasoft_automation.models.related_user.Related user(
                    username = 'louise.data', )
            )
        else:
            return StudioPageContentsInner(
        )
        """

    def testStudioPageContentsInner(self):
        """Test StudioPageContentsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
