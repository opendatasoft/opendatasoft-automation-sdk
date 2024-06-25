# DatasetAlternativeExport

A dataset alternative export

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uid** | **str** | Unique identifier for the alternative export | [optional] [readonly] 
**title** | **str** |  | 
**description** | **str** |  | [optional] 
**mimetype** | **str** |  | [optional] [readonly] 
**type** | **str** |  | 
**created_at** | **datetime** |  | [optional] [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 

## Example

```python
from opendatasoft_automation.models.dataset_alternative_export import DatasetAlternativeExport

# TODO update the JSON string below
json = "{}"
# create an instance of DatasetAlternativeExport from a JSON string
dataset_alternative_export_instance = DatasetAlternativeExport.from_json(json)
# print the JSON string representation of the object
print(DatasetAlternativeExport.to_json())

# convert the object into a dict
dataset_alternative_export_dict = dataset_alternative_export_instance.to_dict()
# create an instance of DatasetAlternativeExport from a dict
dataset_alternative_export_from_dict = DatasetAlternativeExport.from_dict(dataset_alternative_export_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


