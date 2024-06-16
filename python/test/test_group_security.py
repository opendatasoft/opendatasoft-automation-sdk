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

from opendatasoft_automation.models.group_security import GroupSecurity

class TestGroupSecurity(unittest.TestCase):
    """GroupSecurity unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GroupSecurity:
        """Test GroupSecurity
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GroupSecurity`
        """
        model = GroupSecurity()
        if include_optional:
            return GroupSecurity(
                group = opendatasoft_automation.models.group_security_group.GroupSecurity_group(
                    uid = 'content_designers', ),
                permissions = [
                    'manage_connection'
                    ]
            )
        else:
            return GroupSecurity(
        )
        """

    def testGroupSecurity(self):
        """Test GroupSecurity"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
