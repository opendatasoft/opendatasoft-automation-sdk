# UserGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uid** | **str** | The group identifier | [readonly] 
**title** | **str** | The group title | 
**description** | **str** | The group description | [optional] 
**user_count** | **float** | The count of users in the group | [optional] [readonly] 
**permissions** | [**List[Permission]**](Permission.md) | A list of permissions granted to the members of this group | [optional] 
**explore_limits** | [**ExploreLimits**](ExploreLimits.md) |  | [optional] 
**management_limits** | **object** |  | [optional] 
**created_at** | **datetime** |  | [optional] [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 
**created_by** | [**RelatedUserReadOnly**](RelatedUserReadOnly.md) |  | [optional] 
**updated_by** | [**RelatedUserReadOnly**](RelatedUserReadOnly.md) |  | [optional] 

## Example

```python
from opendatasoft_automation.models.user_group import UserGroup

# TODO update the JSON string below
json = "{}"
# create an instance of UserGroup from a JSON string
user_group_instance = UserGroup.from_json(json)
# print the JSON string representation of the object
print(UserGroup.to_json())

# convert the object into a dict
user_group_dict = user_group_instance.to_dict()
# create an instance of UserGroup from a dict
user_group_form_dict = user_group.from_dict(user_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


