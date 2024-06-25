# AmazonS3AWSSignatureV4Auth


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_key_id** | **str** |  | 
**secret_access_key** | **str** | The access key. The API returns null to hide this sensitive value. | 
**region** | **str** |  | 

## Example

```python
from opendatasoft_automation.models.amazon_s3_aws_signature_v4_auth import AmazonS3AWSSignatureV4Auth

# TODO update the JSON string below
json = "{}"
# create an instance of AmazonS3AWSSignatureV4Auth from a JSON string
amazon_s3_aws_signature_v4_auth_instance = AmazonS3AWSSignatureV4Auth.from_json(json)
# print the JSON string representation of the object
print(AmazonS3AWSSignatureV4Auth.to_json())

# convert the object into a dict
amazon_s3_aws_signature_v4_auth_dict = amazon_s3_aws_signature_v4_auth_instance.to_dict()
# create an instance of AmazonS3AWSSignatureV4Auth from a dict
amazon_s3_aws_signature_v4_auth_from_dict = AmazonS3AWSSignatureV4Auth.from_dict(amazon_s3_aws_signature_v4_auth_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


