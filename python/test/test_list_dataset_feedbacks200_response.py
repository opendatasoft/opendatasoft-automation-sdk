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

from openapi_client.models.list_dataset_feedbacks200_response import ListDatasetFeedbacks200Response

class TestListDatasetFeedbacks200Response(unittest.TestCase):
    """ListDatasetFeedbacks200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ListDatasetFeedbacks200Response:
        """Test ListDatasetFeedbacks200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListDatasetFeedbacks200Response`
        """
        model = ListDatasetFeedbacks200Response()
        if include_optional:
            return ListDatasetFeedbacks200Response(
                total_count = 56,
                next = '',
                previous = '',
                results = [
                    {"uid":"df_qf2hyt","record_id":"95969ddab924fc5db5e39c3fb2a7634f4d7dd51c","user":{"username":"john.doe"},"comment":"I like this record, it provides meanigful insights","is_archived":false,"values":{"username":{"value":"A missing value","type":"string"},"age":{"value":39,"type":"double"}}}
                    ]
            )
        else:
            return ListDatasetFeedbacks200Response(
        )
        """

    def testListDatasetFeedbacks200Response(self):
        """Test ListDatasetFeedbacks200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()