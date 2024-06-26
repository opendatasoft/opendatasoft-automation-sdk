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

from opendatasoft_automation.models.list_dataset_schedules200_response import ListDatasetSchedules200Response

class TestListDatasetSchedules200Response(unittest.TestCase):
    """ListDatasetSchedules200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ListDatasetSchedules200Response:
        """Test ListDatasetSchedules200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListDatasetSchedules200Response`
        """
        model = ListDatasetSchedules200Response()
        if include_optional:
            return ListDatasetSchedules200Response(
                total_count = '',
                next = '',
                previous = '',
                results = [
                    opendatasoft_automation.models.schedule_schema.Schedule schema(
                        uid = 'sc_qf2hyt', 
                        cron_schedule = '0 * * * *', )
                    ]
            )
        else:
            return ListDatasetSchedules200Response(
        )
        """

    def testListDatasetSchedules200Response(self):
        """Test ListDatasetSchedules200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
