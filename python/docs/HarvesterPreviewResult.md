# HarvesterPreviewResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_count** | **int** |  | 
**results** | [**List[HarvesterPreviewResultResultsInner]**](HarvesterPreviewResultResultsInner.md) |  | 

## Example

```python
from opendatasoft_automation.models.harvester_preview_result import HarvesterPreviewResult

# TODO update the JSON string below
json = "{}"
# create an instance of HarvesterPreviewResult from a JSON string
harvester_preview_result_instance = HarvesterPreviewResult.from_json(json)
# print the JSON string representation of the object
print(HarvesterPreviewResult.to_json())

# convert the object into a dict
harvester_preview_result_dict = harvester_preview_result_instance.to_dict()
# create an instance of HarvesterPreviewResult from a dict
harvester_preview_result_form_dict = harvester_preview_result.from_dict(harvester_preview_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


