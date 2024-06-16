# GroupSecurityGroup

The group targeted by this ruleset.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uid** | **str** |  | [optional] 

## Example

```python
from opendatasoft_automation.models.group_security_group import GroupSecurityGroup

# TODO update the JSON string below
json = "{}"
# create an instance of GroupSecurityGroup from a JSON string
group_security_group_instance = GroupSecurityGroup.from_json(json)
# print the JSON string representation of the object
print(GroupSecurityGroup.to_json())

# convert the object into a dict
group_security_group_dict = group_security_group_instance.to_dict()
# create an instance of GroupSecurityGroup from a dict
group_security_group_form_dict = group_security_group.from_dict(group_security_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


