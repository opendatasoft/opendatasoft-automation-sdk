# ListDatasetUserSecurity200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_count** | **int** |  | [optional] 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[DatasetUserSecurity]**](DatasetUserSecurity.md) |  | [optional] 

## Example

```python
from opendatasoft_automation.models.list_dataset_user_security200_response import ListDatasetUserSecurity200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListDatasetUserSecurity200Response from a JSON string
list_dataset_user_security200_response_instance = ListDatasetUserSecurity200Response.from_json(json)
# print the JSON string representation of the object
print(ListDatasetUserSecurity200Response.to_json())

# convert the object into a dict
list_dataset_user_security200_response_dict = list_dataset_user_security200_response_instance.to_dict()
# create an instance of ListDatasetUserSecurity200Response from a dict
list_dataset_user_security200_response_from_dict = ListDatasetUserSecurity200Response.from_dict(list_dataset_user_security200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


