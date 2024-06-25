# UserSecurity3


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | [**RelatedUser**](RelatedUser.md) |  | [optional] 
**permissions** | [**List[PermissionEnum3]**](PermissionEnum3.md) | List of special permissions granted to the target. | [optional] 

## Example

```python
from opendatasoft_automation.models.user_security3 import UserSecurity3

# TODO update the JSON string below
json = "{}"
# create an instance of UserSecurity3 from a JSON string
user_security3_instance = UserSecurity3.from_json(json)
# print the JSON string representation of the object
print(UserSecurity3.to_json())

# convert the object into a dict
user_security3_dict = user_security3_instance.to_dict()
# create an instance of UserSecurity3 from a dict
user_security3_from_dict = UserSecurity3.from_dict(user_security3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


