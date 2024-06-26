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

from opendatasoft_automation.models.awsiam_role_auth import AWSIAMRoleAuth

class TestAWSIAMRoleAuth(unittest.TestCase):
    """AWSIAMRoleAuth unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AWSIAMRoleAuth:
        """Test AWSIAMRoleAuth
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AWSIAMRoleAuth`
        """
        model = AWSIAMRoleAuth()
        if include_optional:
            return AWSIAMRoleAuth(
                ods_aws_account_id = '210987654321',
                external_id = 'ods-domain-2fa5c43c-35bf-4e1a-8da5-45f7cd8b4f6c',
                is_valid = True,
                role_arn = 'arn:aws:iam::012345678901:role/ODSRoleAuthMyDomain',
                region = 'eu-west-1'
            )
        else:
            return AWSIAMRoleAuth(
                region = 'eu-west-1',
        )
        """

    def testAWSIAMRoleAuth(self):
        """Test AWSIAMRoleAuth"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
