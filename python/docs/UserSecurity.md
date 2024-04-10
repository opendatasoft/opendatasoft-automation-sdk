# UserSecurity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | [**RelatedUser**](RelatedUser.md) |  | [optional] 
**permissions** | [**List[PermissionEnum]**](PermissionEnum.md) | List of special permissions granted to the target. | [optional] 

## Example

```python
from openapi_client.models.user_security import UserSecurity

# TODO update the JSON string below
json = "{}"
# create an instance of UserSecurity from a JSON string
user_security_instance = UserSecurity.from_json(json)
# print the JSON string representation of the object
print(UserSecurity.to_json())

# convert the object into a dict
user_security_dict = user_security_instance.to_dict()
# create an instance of UserSecurity from a dict
user_security_form_dict = user_security.from_dict(user_security_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


