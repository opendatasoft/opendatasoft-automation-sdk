# UpdateDatasetAlternativeExportRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | 
**type** | **str** |  | 
**description** | **str** |  | [optional] 

## Example

```python
from opendatasoft_automation.models.update_dataset_alternative_export_request import UpdateDatasetAlternativeExportRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateDatasetAlternativeExportRequest from a JSON string
update_dataset_alternative_export_request_instance = UpdateDatasetAlternativeExportRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateDatasetAlternativeExportRequest.to_json())

# convert the object into a dict
update_dataset_alternative_export_request_dict = update_dataset_alternative_export_request_instance.to_dict()
# create an instance of UpdateDatasetAlternativeExportRequest from a dict
update_dataset_alternative_export_request_from_dict = UpdateDatasetAlternativeExportRequest.from_dict(update_dataset_alternative_export_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


