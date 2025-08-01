# InlineObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **str** |  | [readonly] 
**message** | **str** |  | [readonly] 
**trace_id** | **str** |  | [optional] [readonly] 
**detail** | **object** | In some cases, contains additional information about the error. | [optional] [readonly] 

## Example

```python
from opendatasoft_automation.models.inline_object import InlineObject

# TODO update the JSON string below
json = "{}"
# create an instance of InlineObject from a JSON string
inline_object_instance = InlineObject.from_json(json)
# print the JSON string representation of the object
print(InlineObject.to_json())

# convert the object into a dict
inline_object_dict = inline_object_instance.to_dict()
# create an instance of InlineObject from a dict
inline_object_from_dict = InlineObject.from_dict(inline_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


