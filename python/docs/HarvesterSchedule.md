# HarvesterSchedule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uid** | **str** |  | [readonly] 
**cron_schedule** | **str** | The schedule using the unix-cron string format | 
**timezone** | **str** | The schedule timezone | 

## Example

```python
from openapi_client.models.harvester_schedule import HarvesterSchedule

# TODO update the JSON string below
json = "{}"
# create an instance of HarvesterSchedule from a JSON string
harvester_schedule_instance = HarvesterSchedule.from_json(json)
# print the JSON string representation of the object
print(HarvesterSchedule.to_json())

# convert the object into a dict
harvester_schedule_dict = harvester_schedule_instance.to_dict()
# create an instance of HarvesterSchedule from a dict
harvester_schedule_form_dict = harvester_schedule.from_dict(harvester_schedule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


