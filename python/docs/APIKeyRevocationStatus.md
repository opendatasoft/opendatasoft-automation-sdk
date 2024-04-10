# APIKeyRevocationStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**revoked_at** | **datetime** |  | [optional] 
**revocation_reason** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.api_key_revocation_status import APIKeyRevocationStatus

# TODO update the JSON string below
json = "{}"
# create an instance of APIKeyRevocationStatus from a JSON string
api_key_revocation_status_instance = APIKeyRevocationStatus.from_json(json)
# print the JSON string representation of the object
print(APIKeyRevocationStatus.to_json())

# convert the object into a dict
api_key_revocation_status_dict = api_key_revocation_status_instance.to_dict()
# create an instance of APIKeyRevocationStatus from a dict
api_key_revocation_status_form_dict = api_key_revocation_status.from_dict(api_key_revocation_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


