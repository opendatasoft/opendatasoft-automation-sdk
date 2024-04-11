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

from openapi_client.models.list_harvesters200_response import ListHarvesters200Response

class TestListHarvesters200Response(unittest.TestCase):
    """ListHarvesters200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ListHarvesters200Response:
        """Test ListHarvesters200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListHarvesters200Response`
        """
        model = ListHarvesters200Response()
        if include_optional:
            return ListHarvesters200Response(
                total_count = 56,
                next = '',
                previous = '',
                results = [
                    openapi_client.models.harvester_schema.Harvester schema(
                        uid = 'harvester-uid', 
                        type = '0', 
                        name = 'Harvester title', 
                        status = 'idle', 
                        version = 1, 
                        restrict_datasets_visibility = True, 
                        delete_missing_datasets = True, 
                        forced_metas = {"default":{"publisher":"Paris Open Data"}}, 
                        remote_datasets_count = 100, 
                        harvested_datasets_count = 98, 
                        published_datasets_count = 30, 
                        attached_datasets_count = 98, 
                        has_error = False, 
                        resource_errors_count = 2, 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        updated_by = openapi_client.models.related_user.Related user(
                            username = 'louise.data', ), 
                        last_started_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        last_success_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ]
            )
        else:
            return ListHarvesters200Response(
        )
        """

    def testListHarvesters200Response(self):
        """Test ListHarvesters200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()