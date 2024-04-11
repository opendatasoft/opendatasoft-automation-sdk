# ListUserGroups200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_count** | **int** |  | [optional] 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[UserGroup]**](UserGroup.md) |  | [optional] 

## Example

```python
from openapi_client.models.list_user_groups200_response import ListUserGroups200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListUserGroups200Response from a JSON string
list_user_groups200_response_instance = ListUserGroups200Response.from_json(json)
# print the JSON string representation of the object
print(ListUserGroups200Response.to_json())

# convert the object into a dict
list_user_groups200_response_dict = list_user_groups200_response_instance.to_dict()
# create an instance of ListUserGroups200Response from a dict
list_user_groups200_response_form_dict = list_user_groups200_response.from_dict(list_user_groups200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


