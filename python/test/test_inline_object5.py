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

from opendatasoft_automation.models.inline_object5 import InlineObject5

class TestInlineObject5(unittest.TestCase):
    """InlineObject5 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InlineObject5:
        """Test InlineObject5
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InlineObject5`
        """
        model = InlineObject5()
        if include_optional:
            return InlineObject5(
                status = 'idle',
                previous = 'idle',
                next = 'idle',
                since = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                is_published = True,
                message = '',
                records_errors = [],
                params = {}
            )
        else:
            return InlineObject5(
        )
        """

    def testInlineObject5(self):
        """Test InlineObject5"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
