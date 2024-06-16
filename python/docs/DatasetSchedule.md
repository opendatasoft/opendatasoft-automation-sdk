# DatasetSchedule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uid** | **str** |  | [optional] [readonly] 
**cron_schedule** | **str** | The schedule using the unix-cron string format | 

## Example

```python
from opendatasoft_automation.models.dataset_schedule import DatasetSchedule

# TODO update the JSON string below
json = "{}"
# create an instance of DatasetSchedule from a JSON string
dataset_schedule_instance = DatasetSchedule.from_json(json)
# print the JSON string representation of the object
print(DatasetSchedule.to_json())

# convert the object into a dict
dataset_schedule_dict = dataset_schedule_instance.to_dict()
# create an instance of DatasetSchedule from a dict
dataset_schedule_form_dict = dataset_schedule.from_dict(dataset_schedule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


