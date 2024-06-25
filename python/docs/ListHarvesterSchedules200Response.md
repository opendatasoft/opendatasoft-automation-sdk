# ListHarvesterSchedules200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_count** | **int** |  | [optional] 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[HarvesterSchedule]**](HarvesterSchedule.md) |  | [optional] 

## Example

```python
from opendatasoft_automation.models.list_harvester_schedules200_response import ListHarvesterSchedules200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListHarvesterSchedules200Response from a JSON string
list_harvester_schedules200_response_instance = ListHarvesterSchedules200Response.from_json(json)
# print the JSON string representation of the object
print(ListHarvesterSchedules200Response.to_json())

# convert the object into a dict
list_harvester_schedules200_response_dict = list_harvester_schedules200_response_instance.to_dict()
# create an instance of ListHarvesterSchedules200Response from a dict
list_harvester_schedules200_response_from_dict = ListHarvesterSchedules200Response.from_dict(list_harvester_schedules200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


