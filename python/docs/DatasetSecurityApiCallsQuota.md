# DatasetSecurityApiCallsQuota

Upper limit set on the number of API calls the target can make to this dataset in a given timeframe. Can be set to null for no specific quota.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unit** | **str** |  | [optional] 
**limit** | **float** |  | [optional] 

## Example

```python
from openapi_client.models.dataset_security_api_calls_quota import DatasetSecurityApiCallsQuota

# TODO update the JSON string below
json = "{}"
# create an instance of DatasetSecurityApiCallsQuota from a JSON string
dataset_security_api_calls_quota_instance = DatasetSecurityApiCallsQuota.from_json(json)
# print the JSON string representation of the object
print(DatasetSecurityApiCallsQuota.to_json())

# convert the object into a dict
dataset_security_api_calls_quota_dict = dataset_security_api_calls_quota_instance.to_dict()
# create an instance of DatasetSecurityApiCallsQuota from a dict
dataset_security_api_calls_quota_form_dict = dataset_security_api_calls_quota.from_dict(dataset_security_api_calls_quota_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


