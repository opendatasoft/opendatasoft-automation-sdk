# GroupSecurity3


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group** | [**GroupSecurityGroup**](GroupSecurityGroup.md) |  | [optional] 
**permissions** | [**List[PermissionEnum3]**](PermissionEnum3.md) | List of special permissions granted to the target. | [optional] 

## Example

```python
from openapi_client.models.group_security3 import GroupSecurity3

# TODO update the JSON string below
json = "{}"
# create an instance of GroupSecurity3 from a JSON string
group_security3_instance = GroupSecurity3.from_json(json)
# print the JSON string representation of the object
print(GroupSecurity3.to_json())

# convert the object into a dict
group_security3_dict = group_security3_instance.to_dict()
# create an instance of GroupSecurity3 from a dict
group_security3_form_dict = group_security3.from_dict(group_security3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


