# DatasetProcessor

Processor attached to a dataset

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uid** | **str** | Unique identifier for the processor | [optional] [readonly] 
**type** | **str** | Type of the processor | 
**label** | **str** | Friendly label of the processor | 

## Example

```python
from opendatasoft_automation.models.dataset_processor import DatasetProcessor

# TODO update the JSON string below
json = "{}"
# create an instance of DatasetProcessor from a JSON string
dataset_processor_instance = DatasetProcessor.from_json(json)
# print the JSON string representation of the object
print(DatasetProcessor.to_json())

# convert the object into a dict
dataset_processor_dict = dataset_processor_instance.to_dict()
# create an instance of DatasetProcessor from a dict
dataset_processor_from_dict = DatasetProcessor.from_dict(dataset_processor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


