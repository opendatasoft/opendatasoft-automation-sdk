# DatasetFile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uid** | **str** | Unique identifier for the file | [optional] [readonly] 
**filename** | **str** |  | [optional] [readonly] 
**mimetype** | **str** |  | [optional] [readonly] 
**created_at** | **datetime** |  | [optional] [readonly] 

## Example

```python
from opendatasoft_automation.models.dataset_file import DatasetFile

# TODO update the JSON string below
json = "{}"
# create an instance of DatasetFile from a JSON string
dataset_file_instance = DatasetFile.from_json(json)
# print the JSON string representation of the object
print(DatasetFile.to_json())

# convert the object into a dict
dataset_file_dict = dataset_file_instance.to_dict()
# create an instance of DatasetFile from a dict
dataset_file_form_dict = dataset_file.from_dict(dataset_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


