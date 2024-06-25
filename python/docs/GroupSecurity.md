# GroupSecurity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group** | [**GroupSecurityGroup**](GroupSecurityGroup.md) |  | [optional] 
**permissions** | [**List[PermissionEnum]**](PermissionEnum.md) | List of special permissions granted to the target. | [optional] 

## Example

```python
from opendatasoft_automation.models.group_security import GroupSecurity

# TODO update the JSON string below
json = "{}"
# create an instance of GroupSecurity from a JSON string
group_security_instance = GroupSecurity.from_json(json)
# print the JSON string representation of the object
print(GroupSecurity.to_json())

# convert the object into a dict
group_security_dict = group_security_instance.to_dict()
# create an instance of GroupSecurity from a dict
group_security_from_dict = GroupSecurity.from_dict(group_security_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


