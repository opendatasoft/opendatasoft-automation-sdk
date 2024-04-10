# UserSecurity2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | [**RelatedUser**](RelatedUser.md) |  | [optional] 
**permissions** | [**List[PermissionEnum2]**](PermissionEnum2.md) | List of special permissions granted to the target. | [optional] 

## Example

```python
from openapi_client.models.user_security2 import UserSecurity2

# TODO update the JSON string below
json = "{}"
# create an instance of UserSecurity2 from a JSON string
user_security2_instance = UserSecurity2.from_json(json)
# print the JSON string representation of the object
print(UserSecurity2.to_json())

# convert the object into a dict
user_security2_dict = user_security2_instance.to_dict()
# create an instance of UserSecurity2 from a dict
user_security2_form_dict = user_security2.from_dict(user_security2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


