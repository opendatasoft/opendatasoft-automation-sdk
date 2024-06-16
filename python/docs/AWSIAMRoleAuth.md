# AWSIAMRoleAuth


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ods_aws_account_id** | **str** | The AWS account number that will assume the role. | [optional] [readonly] 
**external_id** | **str** | The identifier for the connection that will assume the role. | [optional] [readonly] 
**is_valid** | **bool** | The capability of assuming the role for the connection. Is set to true if the role is successfully assumed when the \&quot;role_arn\&quot; is set. | [optional] [readonly] 
**role_arn** | **str** | The identifier of the role to be assumed should be set to an empty string when the connection is created. It is expected to be updated by the user. | [optional] 
**region** | **str** |  | 

## Example

```python
from opendatasoft_automation.models.awsiam_role_auth import AWSIAMRoleAuth

# TODO update the JSON string below
json = "{}"
# create an instance of AWSIAMRoleAuth from a JSON string
awsiam_role_auth_instance = AWSIAMRoleAuth.from_json(json)
# print the JSON string representation of the object
print(AWSIAMRoleAuth.to_json())

# convert the object into a dict
awsiam_role_auth_dict = awsiam_role_auth_instance.to_dict()
# create an instance of AWSIAMRoleAuth from a dict
awsiam_role_auth_form_dict = awsiam_role_auth.from_dict(awsiam_role_auth_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


