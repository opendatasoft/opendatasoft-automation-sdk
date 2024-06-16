# GroupSecurity2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group** | [**GroupSecurityGroup**](GroupSecurityGroup.md) |  | [optional] 
**permissions** | [**List[PermissionEnum2]**](PermissionEnum2.md) | List of special permissions granted to the target. | [optional] 

## Example

```python
from opendatasoft_automation.models.group_security2 import GroupSecurity2

# TODO update the JSON string below
json = "{}"
# create an instance of GroupSecurity2 from a JSON string
group_security2_instance = GroupSecurity2.from_json(json)
# print the JSON string representation of the object
print(GroupSecurity2.to_json())

# convert the object into a dict
group_security2_dict = group_security2_instance.to_dict()
# create an instance of GroupSecurity2 from a dict
group_security2_form_dict = group_security2.from_dict(group_security2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


