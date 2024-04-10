# DatasetUserSecurity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**security** | [**DatasetSecurity**](DatasetSecurity.md) |  | [optional] 
**permissions** | **List[str]** | List of special permissions granted to the target. | [optional] 
**user** | [**RelatedUser**](RelatedUser.md) |  | 

## Example

```python
from openapi_client.models.dataset_user_security import DatasetUserSecurity

# TODO update the JSON string below
json = "{}"
# create an instance of DatasetUserSecurity from a JSON string
dataset_user_security_instance = DatasetUserSecurity.from_json(json)
# print the JSON string representation of the object
print(DatasetUserSecurity.to_json())

# convert the object into a dict
dataset_user_security_dict = dataset_user_security_instance.to_dict()
# create an instance of DatasetUserSecurity from a dict
dataset_user_security_form_dict = dataset_user_security.from_dict(dataset_user_security_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


