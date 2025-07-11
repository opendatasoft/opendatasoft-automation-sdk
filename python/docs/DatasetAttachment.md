# DatasetAttachment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uid** | **str** | Unique identifier for the file | [optional] [readonly] 
**filename** | **str** |  | [readonly] 
**mimetype** | **str** |  | [optional] [readonly] 
**created_at** | **datetime** |  | [optional] [readonly] 

## Example

```python
from opendatasoft_automation.models.dataset_attachment import DatasetAttachment

# TODO update the JSON string below
json = "{}"
# create an instance of DatasetAttachment from a JSON string
dataset_attachment_instance = DatasetAttachment.from_json(json)
# print the JSON string representation of the object
print(DatasetAttachment.to_json())

# convert the object into a dict
dataset_attachment_dict = dataset_attachment_instance.to_dict()
# create an instance of DatasetAttachment from a dict
dataset_attachment_from_dict = DatasetAttachment.from_dict(dataset_attachment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


