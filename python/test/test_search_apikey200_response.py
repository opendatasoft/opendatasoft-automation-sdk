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

from opendatasoft_automation.models.search_apikey200_response import SearchApikey200Response

class TestSearchApikey200Response(unittest.TestCase):
    """SearchApikey200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SearchApikey200Response:
        """Test SearchApikey200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SearchApikey200Response`
        """
        model = SearchApikey200Response()
        if include_optional:
            return SearchApikey200Response(
                found = True,
                result = opendatasoft_automation.models.api_key_schema.API key schema(
                    uid = 'ak_qf2hyt', 
                    label = 'My API Key', 
                    key = '63d534ca0c1806024215cfd99dba4ea188f55d4f1b53ac0b6eceb455', 
                    permissions = ["explore_restricted_dataset"], 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    user = opendatasoft_automation.models.related_user.Related user(
                        username = 'louise.data', ), 
                    revocation_status = opendatasoft_automation.models.api_key_revocation_status.APIKey_revocation_status(
                        revoked_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        revocation_reason = 'Explanation why the API Key has been revoked', ), 
                    is_revoked = True, )
            )
        else:
            return SearchApikey200Response(
        )
        """

    def testSearchApikey200Response(self):
        """Test SearchApikey200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
