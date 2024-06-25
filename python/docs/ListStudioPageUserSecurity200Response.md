# ListStudioPageUserSecurity200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_count** | **int** |  | [optional] 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[UserSecurity3]**](UserSecurity3.md) |  | [optional] 

## Example

```python
from opendatasoft_automation.models.list_studio_page_user_security200_response import ListStudioPageUserSecurity200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListStudioPageUserSecurity200Response from a JSON string
list_studio_page_user_security200_response_instance = ListStudioPageUserSecurity200Response.from_json(json)
# print the JSON string representation of the object
print(ListStudioPageUserSecurity200Response.to_json())

# convert the object into a dict
list_studio_page_user_security200_response_dict = list_studio_page_user_security200_response_instance.to_dict()
# create an instance of ListStudioPageUserSecurity200Response from a dict
list_studio_page_user_security200_response_from_dict = ListStudioPageUserSecurity200Response.from_dict(list_studio_page_user_security200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


