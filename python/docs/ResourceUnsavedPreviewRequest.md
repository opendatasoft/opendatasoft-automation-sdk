# ResourceUnsavedPreviewRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datasource** | [**Datasource**](Datasource.md) |  | 
**type** | **str** |  | 
**params** | **Dict[str, object]** |  | [optional] 

## Example

```python
from opendatasoft_automation.models.resource_unsaved_preview_request import ResourceUnsavedPreviewRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceUnsavedPreviewRequest from a JSON string
resource_unsaved_preview_request_instance = ResourceUnsavedPreviewRequest.from_json(json)
# print the JSON string representation of the object
print(ResourceUnsavedPreviewRequest.to_json())

# convert the object into a dict
resource_unsaved_preview_request_dict = resource_unsaved_preview_request_instance.to_dict()
# create an instance of ResourceUnsavedPreviewRequest from a dict
resource_unsaved_preview_request_from_dict = ResourceUnsavedPreviewRequest.from_dict(resource_unsaved_preview_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


