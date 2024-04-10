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

from openapi_client.models.list_dataset_user_security200_response import ListDatasetUserSecurity200Response

class TestListDatasetUserSecurity200Response(unittest.TestCase):
    """ListDatasetUserSecurity200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ListDatasetUserSecurity200Response:
        """Test ListDatasetUserSecurity200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListDatasetUserSecurity200Response`
        """
        model = ListDatasetUserSecurity200Response()
        if include_optional:
            return ListDatasetUserSecurity200Response(
                total_count = '18',
                next = '',
                previous = '',
                results = [
                    openapi_client.models.user_ruleset_schema.User ruleset schema(
                        security = openapi_client.models.dataset_security.DatasetSecurity(
                            is_data_visible = True, 
                            visible_fields = ["year","coty_code"], 
                            filter_query = 'year!=2022', 
                            api_calls_quota = openapi_client.models.dataset_security_api_calls_quota.DatasetSecurity_api_calls_quota(
                                unit = 'month', 
                                limit = 12000, ), ), 
                        permissions = [
                            'explore_restricted_dataset'
                            ], 
                        user = openapi_client.models.related_user.Related user(
                            username = 'louise.data', ), )
                    ]
            )
        else:
            return ListDatasetUserSecurity200Response(
        )
        """

    def testListDatasetUserSecurity200Response(self):
        """Test ListDatasetUserSecurity200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
