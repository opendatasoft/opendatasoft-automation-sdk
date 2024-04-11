# ListDatasetSchedules200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_count** | **int** |  | [optional] 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[DatasetSchedule]**](DatasetSchedule.md) |  | [optional] 

## Example

```python
from openapi_client.models.list_dataset_schedules200_response import ListDatasetSchedules200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListDatasetSchedules200Response from a JSON string
list_dataset_schedules200_response_instance = ListDatasetSchedules200Response.from_json(json)
# print the JSON string representation of the object
print(ListDatasetSchedules200Response.to_json())

# convert the object into a dict
list_dataset_schedules200_response_dict = list_dataset_schedules200_response_instance.to_dict()
# create an instance of ListDatasetSchedules200Response from a dict
list_dataset_schedules200_response_form_dict = list_dataset_schedules200_response.from_dict(list_dataset_schedules200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


