# InlineObject6FieldsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**original_name** | **str** |  | [optional] 
**label** | **str** |  | 
**type** | **str** |  | [optional] 
**annotations** | [**List[InlineObject6FieldsInnerAnnotationsInner]**](InlineObject6FieldsInnerAnnotationsInner.md) |  | [optional] 
**name** | **str** |  | 

## Example

```python
from opendatasoft_automation.models.inline_object6_fields_inner import InlineObject6FieldsInner

# TODO update the JSON string below
json = "{}"
# create an instance of InlineObject6FieldsInner from a JSON string
inline_object6_fields_inner_instance = InlineObject6FieldsInner.from_json(json)
# print the JSON string representation of the object
print(InlineObject6FieldsInner.to_json())

# convert the object into a dict
inline_object6_fields_inner_dict = inline_object6_fields_inner_instance.to_dict()
# create an instance of InlineObject6FieldsInner from a dict
inline_object6_fields_inner_from_dict = InlineObject6FieldsInner.from_dict(inline_object6_fields_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


