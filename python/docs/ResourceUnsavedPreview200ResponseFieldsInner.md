# ResourceUnsavedPreview200ResponseFieldsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**original_name** | **str** |  | [optional] 
**label** | **str** |  | 
**type** | **str** |  | [optional] 
**annotations** | [**List[ResourceUnsavedPreview200ResponseFieldsInnerAnnotationsInner]**](ResourceUnsavedPreview200ResponseFieldsInnerAnnotationsInner.md) |  | [optional] 
**name** | **str** |  | 

## Example

```python
from opendatasoft_automation.models.resource_unsaved_preview200_response_fields_inner import ResourceUnsavedPreview200ResponseFieldsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceUnsavedPreview200ResponseFieldsInner from a JSON string
resource_unsaved_preview200_response_fields_inner_instance = ResourceUnsavedPreview200ResponseFieldsInner.from_json(json)
# print the JSON string representation of the object
print(ResourceUnsavedPreview200ResponseFieldsInner.to_json())

# convert the object into a dict
resource_unsaved_preview200_response_fields_inner_dict = resource_unsaved_preview200_response_fields_inner_instance.to_dict()
# create an instance of ResourceUnsavedPreview200ResponseFieldsInner from a dict
resource_unsaved_preview200_response_fields_inner_form_dict = resource_unsaved_preview200_response_fields_inner.from_dict(resource_unsaved_preview200_response_fields_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


