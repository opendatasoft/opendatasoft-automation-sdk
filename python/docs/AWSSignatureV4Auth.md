# AWSSignatureV4Auth


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_key_id** | **str** |  | 
**secret_access_key** | **str** | The access key. The API returns null to hide this sensitive value. | 
**region** | **str** |  | 

## Example

```python
from opendatasoft_automation.models.aws_signature_v4_auth import AWSSignatureV4Auth

# TODO update the JSON string below
json = "{}"
# create an instance of AWSSignatureV4Auth from a JSON string
aws_signature_v4_auth_instance = AWSSignatureV4Auth.from_json(json)
# print the JSON string representation of the object
print(AWSSignatureV4Auth.to_json())

# convert the object into a dict
aws_signature_v4_auth_dict = aws_signature_v4_auth_instance.to_dict()
# create an instance of AWSSignatureV4Auth from a dict
aws_signature_v4_auth_from_dict = AWSSignatureV4Auth.from_dict(aws_signature_v4_auth_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


