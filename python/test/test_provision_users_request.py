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

from opendatasoft_automation.models.provision_users_request import ProvisionUsersRequest

class TestProvisionUsersRequest(unittest.TestCase):
    """ProvisionUsersRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ProvisionUsersRequest:
        """Test ProvisionUsersRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ProvisionUsersRequest`
        """
        model = ProvisionUsersRequest()
        if include_optional:
            return ProvisionUsersRequest(
                username = 'louise.data',
                display_name = 'louise.data',
                first_name = 'Louise',
                last_name = 'Data',
                is_active = True,
                email = 'contact@email.com',
                is_ods = False,
                account_type = 'global',
                permissions = [explore_restricted_dataset, edit_domain],
                joined_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                last_seen_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                last_login_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                expires_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                explore_limits = opendatasoft_automation.models.explore_limits.ExploreLimits(
                    api_calls = opendatasoft_automation.models.explore_limits_api_calls.ExploreLimits_api_calls(
                        limit = 2000, 
                        unit = 'day', ), ),
                management_limits = {},
                gravatar_url = '//www.gravatar.com/avatar/6dde1de523fc80569f3dd80548e3eb9c?d=mm&s=80',
                groups = None,
                identity_providers = [
                    opendatasoft_automation.models.user_identity_providers_inner.User_identity_providers_inner(
                        uid = 'opendatasoft', )
                    ],
                identity_provider = opendatasoft_automation.models.provision_users_request_all_of_identity_provider.provision_users_request_allOf_identity_provider(
                    uid = 'opendatasoft', ),
                identity_provider_attributes = None
            )
        else:
            return ProvisionUsersRequest(
                email = 'contact@email.com',
                identity_provider = opendatasoft_automation.models.provision_users_request_all_of_identity_provider.provision_users_request_allOf_identity_provider(
                    uid = 'opendatasoft', ),
        )
        """

    def testProvisionUsersRequest(self):
        """Test ProvisionUsersRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
