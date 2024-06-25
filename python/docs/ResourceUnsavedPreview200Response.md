# ResourceUnsavedPreview200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fields** | [**List[ResourceUnsavedPreview200ResponseFieldsInner]**](ResourceUnsavedPreview200ResponseFieldsInner.md) |  | [optional] 
**records** | **List[object]** |  | [optional] 

## Example

```python
from opendatasoft_automation.models.resource_unsaved_preview200_response import ResourceUnsavedPreview200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceUnsavedPreview200Response from a JSON string
resource_unsaved_preview200_response_instance = ResourceUnsavedPreview200Response.from_json(json)
# print the JSON string representation of the object
print(ResourceUnsavedPreview200Response.to_json())

# convert the object into a dict
resource_unsaved_preview200_response_dict = resource_unsaved_preview200_response_instance.to_dict()
# create an instance of ResourceUnsavedPreview200Response from a dict
resource_unsaved_preview200_response_from_dict = ResourceUnsavedPreview200Response.from_dict(resource_unsaved_preview200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


