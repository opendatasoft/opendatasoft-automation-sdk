# DatasetFieldConfiguration

Field attached to a dataset

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uid** | **str** | Unique identifier for the field configuration | [optional] [readonly] 
**type** | **str** |  | 
**label** | **str** | Friendly label of the field configuration | 

## Example

```python
from opendatasoft_automation.models.dataset_field_configuration import DatasetFieldConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of DatasetFieldConfiguration from a JSON string
dataset_field_configuration_instance = DatasetFieldConfiguration.from_json(json)
# print the JSON string representation of the object
print(DatasetFieldConfiguration.to_json())

# convert the object into a dict
dataset_field_configuration_dict = dataset_field_configuration_instance.to_dict()
# create an instance of DatasetFieldConfiguration from a dict
dataset_field_configuration_from_dict = DatasetFieldConfiguration.from_dict(dataset_field_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


