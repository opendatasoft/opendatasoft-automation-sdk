# APIKey


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uid** | **str** |  | [optional] [readonly] 
**label** | **str** |  | [optional] 
**key** | **str** |  | [optional] [readonly] 
**permissions** | [**List[Permission]**](Permission.md) | A list of permissions granted to this API Key | [optional] 
**created_at** | **datetime** |  | [optional] [readonly] 
**user** | [**RelatedUserReadOnly**](RelatedUserReadOnly.md) |  | [optional] 
**revocation_status** | [**APIKeyRevocationStatus**](APIKeyRevocationStatus.md) |  | [optional] 
**is_revoked** | **bool** |  | [optional] [readonly] 

## Example

```python
from openapi_client.models.api_key import APIKey

# TODO update the JSON string below
json = "{}"
# create an instance of APIKey from a JSON string
api_key_instance = APIKey.from_json(json)
# print the JSON string representation of the object
print(APIKey.to_json())

# convert the object into a dict
api_key_dict = api_key_instance.to_dict()
# create an instance of APIKey from a dict
api_key_form_dict = api_key.from_dict(api_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


